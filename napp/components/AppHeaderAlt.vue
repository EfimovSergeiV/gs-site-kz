<script setup>
  import cities from '~/cities.ts';

  const config = useRuntimeConfig()
  const route = useRoute()
  const colorMode = useColorMode()

  const shopStore = useShopStore()
  const clientStore = useClientStore()
  // const route = useRoute()

  const { signIn, signOut, token, data, status, lastRefreshedAt } = useAuth()
  const { data: cts } = await useFetch(`${ config.public.baseURL }c/ct/`)

  
  const searchProduct = ref('')
  const searchCity = ref('')
  const searchCountries = computed(() => {
    if (searchCity.value === '') {
      return []
    }

    let matches = 0
    return cities.filter(city => {
      if (
        city.toLowerCase().includes(searchCity.value.toLowerCase())
        && matches < 10
      ) {
        matches++
        return city
      }
    })

  })

</script>


<template>


  <div class="container mx-auto max-w-6xl px-4 lg:px-8">


    <div id="navbar" class="py-4">

      <div class="grid grid-cols-1 gap-2 md:flex items-center justify-between">

        <div class="flex items-center justify-between">
          <div class="md:hidden">
            <div id="mobile-color-mode">
              <button v-if="$colorMode.preference === 'system'" @click="$colorMode.preference = 'dark'" class="bg-blue-600 py-1 border border-gray-100/10 dark:border-gray-500/50 rounded-md transition-all duration-500 w-full h-full flex items-center">
                <div class="flex items-center gap-2 text-gray-100">
                  <span class="px-2 mdi mdi-laptop border-r border-gray-100/50"></span>
                  <p class="text-xs pr-2"> Сменить тему</p>
                </div>
              </button>
              <button v-if="$colorMode.preference === 'dark'" @click="$colorMode.preference = 'light'" class="bg-gray-800 py-1 border border-gray-100/50 dark:border-gray-500/50 rounded-md transition-all duration-500 w-full h-full flex items-center">
                <div class="flex items-center gap-2 text-gray-100">
                  <span class="px-2 mdi mdi-weather-night border-r border-gray-100/50"></span>
                  <p class="text-xs pr-2"> Ночной режим</p>
                </div>
              </button>
              <button v-if="$colorMode.preference === 'light'" @click="$colorMode.preference = 'system'" class="bg-gray-100 py-1 border border-gray-100/10 dark:border-gray-500/50 rounded-md transition-all duration-500 w-full h-full flex items-center">
                <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300">
                  <span class="px-2 mdi mdi-white-balance-sunny border-r border-gray-300"></span>
                  <p class="text-xs pr-2"> Дневной режим</p>
                </div>
              </button>
            </div>

          </div>
          <ul class="flex items-center rounded-md flex-row space-x-2 md:space-x-3 justify-end transition-all">

            <transition name="right-emergence">
              <li v-if="shopStore.shop.telegram">
                <a class="" :href="shopStore.shop.telegram" target="_blank">
                  <div class="bg-white w-7 h-7 flex items-center justify-center rounded-md border border-white/10">
                    <img src="/telegr-logo.webp" class="w-5" />
                  </div>
                </a>
              </li>
            </transition>
            <transition name="right-emergence">
              <li v-if="shopStore.shop.whatsapp">
                <a class="" :href="shopStore.shop.whatsapp" target="_blank">
                  <div class="bg-white w-7 h-7 flex items-center justify-center rounded-md border border-white/10">
                    <img src="/WhatsApp-logo.webp" class="w-8" />
                  </div>
                </a>
              </li>
            </transition>
            <transition name="right-emergence">
              <li v-if="shopStore.shop.viber">
                <a class="" :href="shopStore.shop.viber" target="_blank">
                  <div class="bg-white w-7 h-7 flex items-center justify-center rounded-md border border-white/10">
                    <img src="/viber-logo.webp" class="w-5" />
                  </div>
                </a>
              </li>
            </transition>
          </ul>

          <div v-if="shopStore.shop.mobile" class="flex justify-end">
            <a :href="`tel:${shopStore.mobile.replace('(', '').replace(')', '').replace(/ /ig, '')}`" class="text-sm md:text-xl font-bold text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100 transition-all"> {{ shopStore.shop.mobile }}</a>
          </div>
        </div>


        <div class="md:hidden">
          <div class="flex items-center justify-center -mt-2">
            <nuxt-link :to="{ name: 'index'}" class="">
              <img
                class=" select-none max-h-[6rem]"
                src="/images/blue-svar.webp"
              />      
            </nuxt-link>                  
          </div>            
        </div>


        <div class="grid grid-cols-2 md:flex gap-2 mt-2 md:mt-0">
          <div class="text-gray-300 rounded-lg bg-blue-500 hover:bg-blue-600 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
            <div class="grid grid-cols-1 px-6 py-2 md:py-1 bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
              <a :href="`tel:${shopStore.shop.phone.replace('(', '').replace(')', '').replace(/ /ig, '')}`" class="text-center text-sm md:text-base font-semibold text-gray-100 hover:text-white transition-all"> {{ shopStore.shop.phone }}</a>
            </div>        
          </div>

          <div class="text-gray-100 rounded-lg bg-blue-500 hover:bg-blue-600 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
            <div class="grid grid-cols-1 px-6 py-2 md:py-1 bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
              <a href="mailto:zakaz@glsvar.ru" target="blank" class="text-center text-sm md:text-base font-semibold text-gray-100 hover:text-white transition-all">zakaz@glsvar.ru</a>
            </div>        
          </div>
        </div>

      </div>
    </div>



    <div id="mobile-profile" class="md:hidden grid grid-cols-3 gap-2 mb-4">
      <button @click="clientStore.locationModal = true" class="py-1 cursor-pointer bg-blue-600 border border-gray-100/10 dark:border-gray-500/50 rounded-lg transition-all duration-500">
        <div class="flex items-center gap-2 text-gray-100">
          <span class="px-2 mdi mdi-map-marker-radius border-r border-gray-100/50"></span>
          <p v-if="clientStore.client.city.length < 10" class="text-xs ">{{ clientStore.client.city }}</p>
          <p v-else class="text-xs " :title="clientStore.client.city" >{{ clientStore.client.city.slice(0, 10) }} ...</p>
        </div>
      </button>
      <div class="">

        <nuxt-link :to="{ name: 'lk-name', params: { name: data.username} }"  v-if="status === 'authenticated'" class=" bg-blue-600 border border-gray-100/10 dark:border-gray-500/50 rounded-lg transition-all duration-500 w-full h-full flex items-center">
          <div class="flex items-center gap-2 text-gray-100 h-full w-full">
            <span class="px-2 mdi mdi-account border-r border-gray-100/50"></span>
            <p class="text-xs "> Личный кабинет</p>
          </div>
        </nuxt-link>
        <button  v-else @click="clientStore.registerModal = true" class=" bg-blue-600 border border-gray-100/10 dark:border-gray-500/50 rounded-lg transition-all duration-500 w-full h-full flex items-center">
          <div class="flex items-center gap-2 text-gray-100 h-full w-full">
            <span class="px-2 mdi mdi-account border-r border-gray-100/50"></span>
            <p class="text-xs "> Регистрация</p>
          </div>
        </button>

      </div>
      <div class="py-1 bg-blue-600 border border-gray-100/10 dark:border-gray-500/50 rounded-lg transition-all duration-500">
                  
        <button @click="clientStore.loginModal = true" v-if="status === 'unauthenticated'" class="w-full h-full">
          <div class="flex items-center gap-2 text-gray-100">
            <span class="px-2 mdi mdi-login-variant border-r border-gray-100/50"></span>
            <p class="text-xs "> Войти</p>
          </div>
        </button>

        <button v-else @click="signOut()" class="w-full h-full">
          <div class="flex items-center gap-2 text-gray-100">
            <span class="px-2 mdi mdi-login-variant border-r border-gray-100/50"></span>
            <p class="text-xs "> Выйти</p>
          </div>
        </button>
      </div>
    </div>



    <div id="header" class="">
      <div class="grid grid-cols-1 md:flex gap-4 justify-between relative">
        <div class="w-full min-w-[22rem] max-w-[24rem] grid grid-cols-1 content-between order-2 md:order-1">

          <div class="hidden md:block">
            <div class="flex items-center justify-center -mt-5 py-4 md:py-0">
              <nuxt-link :to="{ name: 'index'}" class="">
                <img
                  class=" select-none"
                  src="/images/blue-svar.webp"
                />      
              </nuxt-link>                  
            </div>            
          </div>


          <div class="bg-white dark:bg-gray-800 px-1 py-2 grid grid-cols-1 gap-4 rounded-md border dark:border-gray-700">

            <div class="hidden md:block">
              <div class="grid grid-cols-2 gap-x-2 gap-y-2">
                <button @click="clientStore.locationModal = true" class="py-1 cursor-pointer bg-gray-100 dark:bg-gray-600 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500">
                  <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300">
                    <span class="px-2 mdi mdi-map-marker-radius border-r border-gray-300"></span>
                    <p v-if="clientStore.client.city.length < 16" class="text-sm ">{{ clientStore.client.city }}</p>
                    <p v-else class="text-sm " :title="clientStore.client.city" >{{ clientStore.client.city.slice(0, 16) }} ...</p>
                  </div>
                </button>

                <div id="color-mode">
                  <button v-if="$colorMode.preference === 'system'" @click="$colorMode.preference = 'dark'" class="bg-gray-100 dark:bg-gray-600 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300">
                      <span class="px-2 mdi mdi-laptop border-r border-gray-300"></span>
                      <p class="text-sm "> Сменить тему</p>
                    </div>
                  </button>
                  <button v-if="$colorMode.preference === 'dark'" @click="$colorMode.preference = 'light'" class="bg-gray-100 dark:bg-gray-600 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300">
                      <span class="px-2 mdi mdi-weather-night border-r border-gray-300"></span>
                      <p class="text-sm "> Ночной режим</p>
                    </div>
                  </button>
                  <button v-if="$colorMode.preference === 'light'" @click="$colorMode.preference = 'system'" class="bg-gray-100 dark:bg-gray-600 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300">
                      <span class="px-2 mdi mdi-white-balance-sunny border-r border-gray-300"></span>
                      <p class="text-sm "> Дневной режим</p>
                    </div>
                  </button>
                </div>

                <div class="">

                  <nuxt-link :to="{name: 'lk-name', params: { name: data.username}}"  v-if="status === 'authenticated'" class=" bg-gray-100 dark:bg-gray-600 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300 h-f3ll w-full">
                      <span class="px-2 mdi mdi-account border-r border-gray-300"></span>
                      <p class="text-sm "> Личный кабинет</p>
                    </div>
                  </nuxt-link>
                  <button  v-else @click="clientStore.registerModal = true" class=" bg-gray-100 dark:bg-gray-600 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300 h-f3ll w-full">
                      <span class="px-2 mdi mdi-account border-r border-gray-300"></span>
                      <p class="text-sm "> Регистрация</p>
                    </div>
                  </button>

                </div>

                <div class="py-1 bg-gray-100 dark:bg-gray-600 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500">
                  
                  <button @click="clientStore.loginModal = true" v-if="status === 'unauthenticated'" class="w-full h-full">
                    <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300">
                      <span class="px-2 mdi mdi-login-variant border-r border-gray-300"></span>
                      <p class="text-sm "> Войти</p>
                    </div>
                  </button>

                  <button v-else @click="signOut()" class="w-full h-full">
                    <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300">
                      <span class="px-2 mdi mdi-login-variant border-r border-gray-300"></span>
                      <p class="text-sm "> Выйти</p>
                    </div>
                  </button>
                </div>
              </div>
            </div>


            <div class="">
              <div class="group">
                <div class="cursor-pointer h-full text-gray-100 bg-blue-500 hover:bg-blue-600 rounded-md border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                  <div class="bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-md py-2">
                    <div class="cursor-pointer">
                      <div class="mdi mdi-24px mdi- menu flex items-center justify-center">
                        <p class="text-lg px-2 uppercase "> Открыть каталог</p>
                      </div>
                    </div>
                  </div>
                </div>

                <div v-if=" route.path !== '/cts'" class="py-4 absolute w-full left-0 z-40 invisible group-hover:visible ease-in-out transition-opacity duration-100 opacity-0 group-hover:opacity-100">
                  <div class="bg-white/90 dark:bg-gray-700/90 border border-gray-100 dark:border-gray-700 backdrop-blur-md rounded-t-md rounded-b-2xl">
                    <div class="px-2 py-2">
                      <div class="columns-1 xl:columns-3 lg:columns-4">
                        <div v-for="ct in cts" :key="ct.id" class="break-inside-avoid-column">
                          <div class="">
                            <div class="py-2 ">
                              <div class="bg-gray-100/90 dark:bg-gray-800/80 border border-gray-200 dark:border-gray-500 rounded-md py-2 px-2">
                                <div class="py-2">
                                  <nuxt-link :to="{ name: 'prods', query: { ct: ct.id } }" class=" text-gray-700 dark:text-gray-100 text-base transition-all">{{ ct.name }}</nuxt-link>              
                                </div>
                                <div>
                                  <ul>
                                    <li v-for="sct in ct.inserted" :key="sct.id" class="inline-block ">
                                      <nuxt-link :to="{ name: 'prods', query: { ct: sct.id } }" class="text-gray-700 mr-3 text-sm hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100 transition-all">{{ sct.name }}</nuxt-link>
                                    </li>
                                  </ul>
                                </div>                                  
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="flex items-center justify-end">
                        <nuxt-link :to="{ name: 'cts' }" class="border border-gray-500 text-gray-100 bg-blue-600 hover:bg-blue-600 rounded-md  border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                          <div class="bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-md h-full w-full px-8 py-2">
                            <p>Перейти в каталог</p>
                          </div>
                        </nuxt-link>
                      </div>
                    </div>
                  </div>  
                </div>
              </div>
            </div>
          </div>
        </div>


        <div class="w-[680px] lg:w-[700px] order-1 md:order-2">
          <TopSlider />
        </div>

      </div>

    </div>


  </div>
</template>