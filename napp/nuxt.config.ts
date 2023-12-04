import cfg from "./conf"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  app: {
    head: {
      title: 'Главный сварщик',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        // { 
        //   hid: 'description', 
        //   name: 'description', 
        //   content: 'Купить высококачественное сварочное оборудование. Мы являемся официальным дистрибьютором ведущих брендов. Большой выбор, гарантия качества, доставка по всей России.' 
        // },
        // { 
        //   hid: 'keywords', 
        //   name: 'keywords', 
        //   content: 'сварочное оборудование, оборудование для сварки, купить электроды, купить проволоку, купить источник, купить сварочный инвертор' 
        // },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
      ]
    },

    pageTransition: { name: 'page', mode: 'out-in' },

    // pageTransition: {
    //   name: 'fade',
    //   mode: 'out-in' // default
    // },
    // layoutTransition: {
    //   name: 'slide',
    //   mode: 'out-in' // default
    // }
  },

  // nitro: {
  //   experimental: {
  //     wasm: true
  //   }
  // },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/color-mode',
    '@sidebase/nuxt-auth',
    'nuxt-lodash',
    'nuxt-gtag',
    '@artmizu/yandex-metrika-nuxt',
    '@pinia/nuxt',
    'nuxt-swiper',
  ],

  // Auth module
  build: {
    transpile: ['jsonwebtoken']
  },
  auth: {
    baseURL: cfg.BASE_URL,
    provider: {
      type: 'local',
      
      endpoints: {
        signIn: { path: 'auth/', method: 'post' },
        signOut: { path: 'logout/', method: 'post' },
        signUp: { path: 'register/', method: 'post' },
        getSession: { path: 'u/profile/', method: 'get' }
      },

      // pages: {
      //   login: '/'
      // },
      token: {
        // signInResponseTokenPointer: '/token/accessToken'
        maxAgeInSeconds: 60 * 60 * 24 * 14,
      },
      sessionDataType: { id: 'string', email: 'string', name: 'string', role: 'admin | guest | account', subscriptions: "{ id: number, status: 'ACTIVE' | 'INACTIVE' }[]" }
    },
    session: {
      // Whether to refresh the session every time the browser window is refocused.
      enableRefreshOnWindowFocus: true,

      // Whether to refresh the session every `X` milliseconds. Set this to `false` to turn it off. The session will only be refreshed if a session already exists.
      enableRefreshPeriodically: false  ///5000
    },
    globalAppMiddleware: {
      isEnabled: false
    }
  },


  pinia: {
    autoImports: [
      // automatically imports `defineStore`
      'defineStore', // import { defineStore } from 'pinia'
      ['defineStore', 'definePiniaStore'], // import { defineStore as definePiniaStore } from 'pinia'
    ],
  },

  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || cfg.BASE_URL,
    },
  },

  imports: {
    dirs: ['stores'],
  },

  css: [
    '~/assets/css/tailwind.css',
    '~/assets/css/main.css',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  colorMode: {
    classSuffix: ''
  },

  // auth: {
  //   origin: 'process.env.ORIGIN',
  //   enableGlobalAppMiddleware: true
  // },

  plugins: [
    { src: '~/plugins/bg-scroll.js', mode: 'client' },
    { src: '~/plugins/navbar.js', mode: 'client' },
  ],

  lodash: {
    prefix: "_",
    prefixSkip: ["string"],
    upperAfterPrefix: false,
    exclude: ["map"],
    alias: [
      ["camelCase", "stringToCamelCase"], // => stringToCamelCase
      ["kebabCase", "stringToKebab"], // => stringToKebab
      ["isDate", "isLodashDate"], // => _isLodashDate
    ],
  },

  gtag: {
    id: cfg.gtmId
  },

  yandexMetrika: {
    id: cfg.yandexMetrika,
  }


})
