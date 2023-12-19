<script setup>
  const config = useRuntimeConfig()
  // const countStore = useCountStore()

  const { data: widebanners } = await useFetch(`${ config.public.baseURL }c/widebanners/`)
  

</script>


<template>
  <div class="">
    
    <Swiper
      class="rounded-md relative w-full"
      :height="300"
      :modules="[SwiperAutoplay, SwiperEffectCreative]"
      :slides-per-view="1"
      :loop="true"
      :effect="'creative'"
      :autoplay="{
        delay: 8000,
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
      <SwiperSlide v-for="slide in widebanners" :key="slide.id" class="">
        <div class="rounded-md">

          <img
            :src="slide.image"
            style="width: 100%;"
            width="1024px"
            height="320px"
            class="rounded-md border bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700"
            :alt="slide.name"
          />

          <nuxt-link v-if="slide.path" :to="slide.path">  
            <div class="absolute top-0 right-0 z-40 w-full h-full">
              <div class="flex justify-end">
                <div class="relative mx-2 md:mx-4 md:my-2">
                  <span class="mdi mdi-16px mdi-link-variant text-whitw shadow-2xl"></span>
                </div>
              </div>
            </div>
          </nuxt-link>

          <a :href="slide.link" target="blank" v-if="slide.link">  
            <div class="absolute top-0 right-0 z-40 w-full h-full">
              <div class="flex justify-end">
                <div class="relative mx-2 md:mx-4 md:my-2">
                  <span class="mdi mdi-16px mdi-link-variant text-whitw shadow-2xl"></span>
                </div>
              </div>
            </div>
          </a>

        </div> 
        
      </SwiperSlide>
      
      <div class="absolute bottom-0 right-0 z-40 p-3">
        <SwiperControls class="bg-gray-100/80 rounded-full border border-gray-200/50 hover:border-gray-300 dark:border-gray-600/50 dark:hover:border-gray-500 dark:bg-gray-700/80 transition-all duration-500 px-1" />
      </div>
      
    </Swiper>

  </div>
</template>
