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
  <div class="container mx-auto max-w-6xl px-4 lg:px-8 ">


    <div class="relative mb-1">
      <div class="grid grid-cols-1 md:flex gap-4">
        <div class="min-w-[345px]">

          <div class="h-full grid grid-cols-1 content-end between">

            <div class="flex items-center justify-center">
              <div class="py-10 w-[345px]">
                <nuxt-link :to="{ name: 'index' }">
                  <img src="/images/blue-svar.webp" class="max-h-[4rem]" />
                  <p class="text-2xl font-semibold italic text-end px-4 text-gray-700 dark:text-gray-300"><span class="text-xs ml-4">интернет магазин</span> GLSVAR.KZ</p>
                </nuxt-link>
              </div>
            </div>


            <div class="grid grid-cols-1 gap-2">
              <div class="grid grid-cols-2 gap-x-2 gap-y-2">
                <button @click="clientStore.locationModal = true" class="py-1 cursor-pointer bg-gray-100 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500">
                  <div class="flex items-center gap-2 text-gray-700">
                    <span class="px-2 mdi mdi-map-marker-radius border-r border-gray-300"></span>
                    <p v-if="clientStore.client.city.length < 16" class="text-sm ">{{ clientStore.client.city }}</p>
                    <p v-else class="text-sm " :title="clientStore.client.city" >{{ clientStore.client.city.slice(0, 16) }} ...</p>
                  </div>
                </button>

                <div id="color-mode">
                  <button v-if="$colorMode.preference === 'system'" @click="$colorMode.preference = 'dark'" class="bg-gray-100 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 ">
                      <span class="px-2 mdi mdi-laptop border-r border-gray-300"></span>
                      <p class="text-sm "> Сменить тему</p>
                    </div>
                  </button>
                  <button v-if="$colorMode.preference === 'dark'" @click="$colorMode.preference = 'light'" class="bg-gray-100  shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 ">
                      <span class="px-2 mdi mdi-weather-night border-r border-gray-300"></span>
                      <p class="text-sm "> Ночной режим</p>
                    </div>
                  </button>
                  <button v-if="$colorMode.preference === 'light'" @click="$colorMode.preference = 'system'" class="bg-gray-100  shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 ">
                      <span class="px-2 mdi mdi-white-balance-sunny border-r border-gray-300"></span>
                      <p class="text-sm "> Дневной режим</p>
                    </div>
                  </button>
                </div>

                <div class="">
                  <nuxt-link :to="{name: 'lk-name', params: { name: data.username}}"  v-if="status === 'authenticated'" class=" bg-gray-100  shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 h-full w-full">
                      <span class="px-2 mdi mdi-account border-r border-gray-300"></span>
                      <p class="text-sm "> Личный кабинет</p>
                    </div>
                  </nuxt-link>
                  <button  v-else @click="clientStore.registerModal = true" class=" bg-gray-100 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500 w-full h-full flex items-center">
                    <div class="flex items-center gap-2 text-gray-700 h-full w-full">
                      <span class="px-2 mdi mdi-account border-r border-gray-300"></span>
                      <p class="text-sm "> Регистрация</p>
                    </div>
                  </button>
                </div>

                <div class="py-1 bg-gray-100 shadow-lg shadow-black/30 border border-gray-100/10 dark:border-white/20 rounded-lg transition-all duration-500">
                  
                  <button @click="clientStore.loginModal = true" v-if="status === 'unauthenticated'" class="w-full h-full">
                    <div class="flex items-center gap-2 text-gray-700 ">
                      <span class="px-2 mdi mdi-login-variant border-r border-gray-300"></span>
                      <p class="text-sm "> Войти</p>
                    </div>
                  </button>

                  <button v-else @click="signOut()" class="w-full h-full">
                    <div class="flex items-center gap-2 text-gray-700 ">
                      <span class="px-2 mdi mdi-login-variant border-r border-gray-300"></span>
                      <p class="text-sm "> Выйти</p>
                    </div>
                  </button>
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

                  <div v-if=" route.path !== '/cts'" class="py-2 absolute w-full left-0 z-40 invisible group-hover:visible ease-in-out transition-opacity duration-100 opacity-0 group-hover:opacity-100">
                    <div class="bg-gray-300 dark:bg-gray-700 border border-gray-100 dark:border-gray-700 backdrop-blur-md rounded-t-sm rounded-b-md">
                      <div class="px-2 py-2">
                        <div class="grid grid-cols-4 gap-2">
                          <div v-for="ct in cts" :key="ct.id" class="break-inside-avoid-column">
                            <div class="">
                              <div class="">
                                <div class="bg-white border border-gray-200 dark:border-gray-700 rounded-md py-2 px-2">
                                  <div class="grid grid-cols-1 gap-4">
                                    <div class="flex justify-center">
                                      <img v-if="ct.icon" :src="`/${ct.icon}`" class="h-16" />
                                    </div>
                                    
                                    <div class="flex justify-center">
                                      <nuxt-link :to="{ name: 'prods', query: { ct: ct.id } }" class=" text-gray-700 text-xl transition-all">{{ ct.name }}</nuxt-link>              
                                    </div>
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

                        <div class="flex items-center justify-end px-6 pt-2">
                          <nuxt-link :to="{ name: 'cts' }">
                            <p class="text-xl">Перейти в категории</p>
                          </nuxt-link>
                        </div>

                      </div>
                    </div>  
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- <a href="https://maps.app.goo.gl/yh6zuQBe2mQJ5Xyr8" target="blank">
          <p class="text-gray-600 dark:text-gray-200 text-base "> ул. Топоркова 35, Рудный, 111500</p>
        </a> -->

        <div class="">          
          <div class="flex items-end h-full">
            <div class="grid grid-cols-1">
              

              <div class="flex justify-end gap-6 uppercase font-semibold py-2">
                <div class="before:block before:absolute before:-inset-2 before:-skew-y-3 hover:text-white hover:before:bg-blue-600 transition-all duration-300 relative inline-block my-2">
                  <nuxt-link :to="{ name: 'lk-name', params: { name: 'guest' } }" class="relative">Избранное</nuxt-link>
                </div>
                <div class="before:block before:absolute before:-inset-2 before:-skew-y-3 hover:text-white hover:before:bg-blue-600 transition-all duration-700 relative inline-block my-2">
                  <nuxt-link :to="{ name: 'compare' }" class="relative ">Товары в сравнении</nuxt-link>
                </div>
                <div class="before:block before:absolute before:-inset-2 before:-skew-y-3 hover:text-white hover:before:bg-blue-600 transition-all duration-300 relative inline-block my-2">
                  <nuxt-link :to="{ name: 'cart' }" class="relative ">Корзина</nuxt-link>
                </div>
                <div class="before:block before:absolute before:-inset-2 before:-skew-y-3 hover:text-white hover:before:bg-blue-600 transition-all duration-300 relative inline-block my-2">
                  <nuxt-link :to="{ name: 'about' }" class="relative ">О нас</nuxt-link>
                </div>

              </div>


              <div class="hidden md: block">
                <div class="grid grid-cols-1 gap-2 py-2">
                  <div class="flex items-end justify-end gap-8">

                    <div class="grid grid-cols-1 gap-0.5 justify-end items-end">
                      <div class=" flex items-end justify-end bg-blue-400">
                        <a :href="`tel:+77084238070`" class="text-center text-lg text-gray-600 dark:text-gray-200 hover:text-white transition-all"> +7 708 423 8070</a>
                      </div>
                      <div class=" flex items-start justify-end bg-blue-400">
                        <a href="mailto:zakaz@glsvar.kz" target="_blank" class="text-center text-sm  text-gray-600 dark:text-gray-200 hover:text-white">zakaz@glsvar.kz</a>          
                      </div>
                    </div>

                    <div class="">
                      <div class="grid grid-cols-1 gap-0.5 justify-end items-end">
                        <div class=" flex items-end justify-start bg-blue-400">
                          <p class="text-gray-600 dark:text-gray-200 text-sm ">Главный сварщик. Казахстан,</p>
                        </div>
                        <div class=" flex items-start justify-start bg-blue-400">
                          <p class="text-gray-600 dark:text-gray-200 text-lg "> ул. Топоркова 35, Рудный, 111500</p>
                        </div>                        


                      </div>

                    </div>
                    


                  </div>
                </div>
              </div>
              <div class="w-full">
                <TopSlider />
              </div>
              

              <div class="mt-2">
                <input 
                  v-model="search" 
                  type='search'
                  id="phone"
                  placeholder="Поиск по каталогу"
                  class="bg-gray-50 border border-gray-300 text-gray-700 font-semibold dark:text-gray-700 text-sm 
                  uppercase rounded-md focus:ring-gray-300/0 focus:border-gray-300 block 
                  w-full pl-12 p-2 dark:bg-white dark:border-gray-700 dark:placeholder-gray-500
                  ring-0 dark:focus:ring-gray-600/0 dark:focus:border-gray-700" >
              </div>


            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>