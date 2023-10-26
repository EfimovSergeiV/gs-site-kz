<script setup>
  const config = useRuntimeConfig()
  // const router = useRouter()

  const productsStore = useProductsStore()
  // const notificationsStore = useNotificationsStore()

  // const props = defineProps(['product'])


</script>



<template>

  <div class="fixed z-50 w-full h-full bg-gray-500/50 backdrop-blur-sm">
    <div class="flex items-center justify-center h-full">
      <div class="h-full w-full flex items-center justify-center">
        

        <div class="container mx-auto px-4 lg:max-w-4xl lg:px-8">
          <div class="relative bg-white rounded-lg shadow">
            <div class="">

              <div class="flex justify-between items-start px-4 py-2 rounded-t border-b border-gray-200">
                <button @click="productsStore.clearProductImages" type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-700 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" data-modal-toggle="defaultModal">
                  <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                  <span class="sr-only">Закрыть окно</span>
                </button>
              </div>

              <div class="bg-white">
                <div class="h-[28rem]">
                  <Swiper
                    class="rounded-md relative h-[28rem] flex items-center justify-center"
                    :modules="[SwiperAutoplay, SwiperEffectCreative]"
                    :slides-per-view="1"
                    :loop="true"
                    :effect="'creative'"
                    :autoplay="{
                      delay: 10000,
                      disableOnInteraction: true
                    }"
                    :creative-effect="{
                      prev: {
                        shadow: false,
                        translate: ['-20%', 0, -1]
                      },
                      next: {
                        translate: ['100%', 0, 0]
                      }
                    }"
                  >
                    <SwiperSlide v-for="slide in productsStore.productImages" :key="slide.id" class="">
                      <nuxt-link :to="slide.link">
                        <img

                          :src="slide.image"
                          class="w-[34rem]"
                        />             
                      </nuxt-link>
                    </SwiperSlide>
                    <div v-if="productsStore.productImages.length > 1" class="absolute bottom-0 right-0 z-40 p-3">
                      <SwiperControls />
                    </div>
                  </Swiper>
                </div>
              </div>


              <div class="grid grid-cols-1 items-end justify-between px-6 py-2 space-x-2 rounded-b border-t border-gray-200">
                <div class="flex justify-center gap-2 w-full md:justify-end">
                                    
                  <button @click="productsStore.clearProductImages" data-modal-toggle="defaultModal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 ">Закрыть окно</button>
                </div>
              </div>


            </div>


          </div>
        </div>


      </div>        
    </div>
  </div>
</template>