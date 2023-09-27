<script setup>
  import { onMounted } from 'vue'

  const config = useRuntimeConfig()
  // const route = useRoute()
  // const colorMode = useColorMode()

  const shopStore = useShopStore()
  const productsStore = useProductsStore()
  const clientStore = useClientStore()
  // const notificationsStore = useNotificationsStore()

  const { signIn, signOut, token, data, status, lastRefreshedAt } = useAuth()
  const { data: shops } = await useFetch(`${ config.public.baseURL }c/shops/`)


  shopStore.writeShops(shops)

  onMounted(() => {
    if ("geolocation" in navigator) {
      /* местоположение доступно */
      navigator.geolocation.getCurrentPosition(position => {
        let location = {
          "latitude": position.coords.latitude, 
          "longitude": position.coords.longitude 
        }

        shopStore.sendCoordinates(location)

        // this.sendCoordinates(location)
      });
    } else {
      /* местоположение НЕ доступно */
    }

  })

</script>

<template>
  <div class="">


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
          <AppFooter />
        </div>
      </div>


      <div class="">
        <div class="fixed z-40 bottom-60 md:bottom-54 right-20 hover:right-24 transition-all duration-500">
          <div class="relative">
            <div class="absolute z-50">
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
        <div class="fixed z-40 bottom-16 -right-[110px] hover:right-0 focus:right-0 transition-all duration-500">
          <div class="relative">
            <div class="">
              <div class=" bg-blue-600 group rounded-l-md cursor-pointer transition-all duration-500">
                <div class="flex items-center justify-center">
                  <div class="grid grid-cols-4 items-center gap-4 py-2 px-2">
                    <p class="mdi mdi-arrow-left-circle text-gray-200"></p>
                    <a class="" title="WhatsApp" :href="shopStore.shop.whatsapp" target="_blank">
                      <img src="/WhatsApp-logo.webp" class="w-5" />
                    </a>
                    <a class="" title="Telegramm" :href="shopStore.shop.telegram" target="_blank">
                      <img src="/telegr-logo.webp" class="w-5" />
                    </a>
                    <a class="" title="Viber" :href="shopStore.shop.viber" target="_blank">
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
</template>