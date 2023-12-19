<script setup>
  const props = defineProps(['banners','latest'])


</script>


<template>
  <div  class="container mx-auto max-w-6xl py-2 px-4 lg:px-8">


    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">


      <div class="w-full">
        <div class="grid grid-cols-2 gap-4 h-full content-stretch">
          <div v-for="product in latest.slice(0, 4)" :key="product.id">

            <div class="bg-white w-full h-full rounded-md">
 
              <div class="grid grid-cols-1 h-full">
                <nuxt-link :to="{ name: 'product-id', params: { id: product.id }}" class="grid grid-cols-1 content-between">
                  <div class="flex items-center justify-start px-2">
                    
                    <div class="text-red-700 flex items-center gap-1">
                      <span class="mdi mdi-18px mdi-alert-decagram"></span>
                      <p class="text-xs font-semibold ">Новинка</p>
                    </div>
                    
                  </div>
                  <div class="flex items-center justify-center lg:justify-start">
                    <div class="flex gap-2 px-2 lg:px-4">
                      <img :src="product.preview_image" :alt="product.name" class="h-14 md:h-16" />
                      <div class="flex items-center justify-start w-full">
                        <p v-if="product.price" class="text-gray-600 font-bold text-sm md:text-xl">{{ product.price.toLocaleString() }} <span class=" text-sm md:text-lg">тг</span></p>  
                        <p v-else class="text-gray-700 font-bold text-xs">Стоимость по запросу</p>
                      </div>
                    </div>
                  </div>
                              
                  <div class="flex items-center justify-end pb-1 px-4 min-h-[36px]">
                    <p class="text-xs font-semibold text-gray-600 dark:text-gray-700 text-right">{{ product.name }}</p>
                  </div>
                </nuxt-link>
              </div>

            </div>
          </div>

        </div>
      </div>



      <div class="hidden lg:block h-full">
        <Swiper
          class="rounded-md relative w-full h-full"
          :modules="[]"
          :slides-per-view="1"
          :loop="true" >
       
          <SwiperSlide v-for="slide in props.banners" :key="slide.id" class="">
            <nuxt-link :to="slide.link">
              <img
                :src="slide.image"
                class="rounded-md w-full h-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700"
              />             
            </nuxt-link>
          </SwiperSlide>
          <div class="absolute bottom-0 right-0 z-40 p-3">
            <SwiperControls class="bg-gray-100/80 rounded-full border border-gray-200/50 hover:border-gray-300 dark:border-gray-600/50 dark:hover:border-gray-500 dark:bg-gray-700/80 transition-all duration-500 px-1" />
          </div>
        </Swiper>
      </div>


    </div>
  </div>
</template>
