<script setup>
  import { onMounted } from 'vue'

  const config = useRuntimeConfig()
  const route = useRoute()
  const tmp_id = useCookie('tmp_id')
  // const colorMode = useColorMode()

  const shopStore = useShopStore()
  const productsStore = useProductsStore()
  const clientStore = useClientStore()
  // const notificationsStore = useNotificationsStore()

  const { signIn, signOut, token, data, status, lastRefreshedAt } = useAuth()
  // const { data: shops } = await useFetch(`${ config.public.baseURL }c/shops/`)


  // shopStore.writeShops(shops)

  onMounted( async () => {

    /// Присваиваем клиенту временыый идентификатор
    if ( tmp_id.value ) {
      /// Проверяем, если устарел (нет в базе), получаем новый
      const watcher = await $fetch(`${ config.public.baseURL }u/uwatch/`, {
        method: 'PUT', body: { "tmp_id": tmp_id.value }
      }).catch((error) => error.data)
      if ( watcher.tmp_id ) {
        console.log(watcher, 'IF WATCHER')
        tmp_id.value = watcher.tmp_id
      }
      console.log(watcher)
    } else {
      /// Если tmp_id не найден, получаем новый
      const watcher = await $fetch(`${ config.public.baseURL }u/uwatch/`, { method: 'PUT' }).catch((error) => error.data)
      tmp_id.value = watcher.tmp_id
    }

    /// Получаем данные о просмотренных товарах
    const tmp_data = await $fetch(`${ config.public.baseURL }u/uwatch/`, {
      headers: {
        "Authorization": tmp_id.value,
      }
    }).catch((error) => error.data)
    productsStore.restoreState(tmp_data)


    clientStore.getLocateFromIP()
    if ("geolocation" in navigator) {
      /* Определяем местоположение по координатам */
      navigator.geolocation.getCurrentPosition(position => {
        let location = {
          "lat": position.coords.latitude, 
          "long": position.coords.longitude 
        }

        clientStore.sendCoordinates(location)

        // this.sendCoordinates(location)
      });
    } else {
      /* Местоположение не доступно */
    }

  })

</script>

<template>
  <div class="">

    <div class="">
      <div id="navbar" class="bg-gray-300 dark:bg-gray-800 text-gray-700 dark:text-gray-300 border-b border-gray-400 dark:border-gray-700 fixed hidden w-full z-40">
        
        <div class="container mx-auto px-4 max-w-6xl lg:px-8">
          <div class="flex justify-end gap-4 md:gap-4 uppercase font-semibold py-2">
            <div class="hidden md:block before:block before:absolute before:-inset-2 before:-skew-y-3 transition-all duration-0 relative my-2">
              <nuxt-link :to="{ name: 'index' }" class="relative text-xs md:text-base">Главная</nuxt-link>
            </div>
            <div class="before:block before:absolute before:-inset-2 before:-skew-y-3 transition-all duration-0 relative inline-block my-2">
              <nuxt-link :to="{ name: 'lk' }" class="relative text-xs md:text-base">Избранное</nuxt-link>
            </div>
            <div class="before:block before:absolute before:-inset-2 before:-skew-y-3 transition-all duration-0 relative inline-block my-2">
              <nuxt-link :to="{ name: 'compare' }" class="relative text-xs md:text-base">В сравнении</nuxt-link>
            </div>
            <div class="before:block before:absolute before:-inset-2 before:-skew-y-3 text-white before:bg-blue-600 transition-all duration-0 relative inline-block my-2 px-2">
              <nuxt-link :to="{ name: 'cart' }" class="relative text-xs md:text-base">Корзина ( {{ productsStore.cart.length }} )</nuxt-link>
            </div>
            <div class="before:block before:absolute before:-inset-2 before:-skew-y-3 transition-all duration-0 relative inline-block my-2">
              <nuxt-link :to="{ name: 'about' }" class="relative text-xs md:text-base">О нас</nuxt-link>
            </div>
          </div>
        </div>
        
      </div>
    </div>


    <transition name="fade" mode="in-out">
      <CartModal v-if="productsStore.cartAlert" />
    </transition>
    <transition name="fade" mode="in-out">
      <OrderModal v-if="clientStore.order" />
    </transition>
    <transition name="fade" mode="in-out">
      <RequestPrice v-if="productsStore.requestPrice" />
    </transition>
    <transition name="fade" mode="in-out">
      <ProductImageModal v-if="productsStore.productImages" />
    </transition>
    <transition name="fade" mode="in-out">
      <WriteUsModal v-if="shopStore.writeUsModal" />
    </transition>
    <transition name="fade" mode="in-out">
      <Toasts />
    </transition>
    <transition name="fade" mode="in-out">
      <LocationModal v-if="clientStore.locationModal" />
    </transition>
    <transition name="fade" mode="in-out">
      <LoginModal v-if="clientStore.loginModal && status === 'unauthenticated'" />
    </transition>
    <transition name="fade" mode="in-out">
      <RegisterModal v-if="clientStore.registerModal" />
    </transition>


    <div class="bg-gradient-to-r from-gray-300 to-gray-100 dark:from-gray-900 dark:to-gray-800 text-gray-700 dark:text-gray-300">
      
      <div id="background-page" class="bg-fixed bg-no-repeat bg-[center_100px] bg-cover bg-[url('images/footer-bg.webp')] dark:bg-[url('images/footer-dark-bg.webp')] min-h-screen">        
        <div class="">
          <slot />
          
        </div>
      </div>

      <div  v-if=" route.path !== '/banner'" class="">
        <div class="">
          <div class="fixed z-10 bottom-60 md:bottom-54 right-20 hover:right-24 transition-all duration-500">
            <div class="relative">
              <div class="absolute z-40">
                <div class="-rotate-90 bg-blue-600 px-4 pb-12 group rounded-md w-44 cursor-pointer" @click="shopStore.showWriteUsModal">
                  <div class="flex items-center justify-center group-hover:text-gray-100 text-gray-300 font-bold transition-all duration-500">
                    <div class="">
                      <p class="text-sm mx-2">Напишите нам</p>
                    </div>
                    <div class="rotate-90">
                      <p class="mdi mdi-24px mdi-message-text-outline"></p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>


        <div class="">
          <div class="fixed z-10 bottom-16 -right-[126px] hover:right-0 focus:right-0 transition-all duration-500">
            <div class="relative">
              <div class="">
                <div class=" bg-blue-600 group rounded-l-md cursor-pointer transition-all duration-500">
                  <div class="flex items-center justify-center">
                    <div class="grid grid-cols-4 items-center gap-4 px-1">
                      <p class="mdi mdi-24px mdi-cellphone-link text-gray-200 pl-0.5"></p>
                      <a class="" title="WhatsApp" href="shopStore.shop.whatsapp" target="_blank">
                        <img src="/WhatsApp-logo.webp" class="w-5" />
                      </a>
                      <a class="" title="Telegramm" href="shopStore.shop.telegram" target="_blank">
                        <img src="/telegr-logo.webp" class="w-5" />
                      </a>
                      <a class="" title="Viber" href="shopStore.shop.viber" target="_blank">
                        <img src="/viber-logo.webp" class="w-5" />
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>


      </div>



    </div>
  </div>
</template>