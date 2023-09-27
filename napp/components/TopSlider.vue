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
            class="rounded-md border dark:border-gray-700"
            :alt="slide.name"
            onerror="this.src='./noimage-960-540.jpg'"
          />

          <nuxt-link v-if="slide.path" :to="slide.path">  
            <div class="absolute top-0 right-0 z-50 w-full h-full">
              <div class="flex justify-end">
                <div class="relative mx-2 md:mx-4 md:my-2">
                  <span class="mdi mdi-16px mdi-link-variant text-whitw shadow-2xl"></span>
                </div>
              </div>
            </div>
          </nuxt-link>

          <a :href="slide.link" target="blank" v-if="slide.link">  
            <div class="absolute top-0 right-0 z-50 w-full h-full">
              <div class="flex justify-end">
                <div class="relative mx-2 md:mx-4 md:my-2">
                  <span class="mdi mdi-16px mdi-link-variant text-whitw shadow-2xl"></span>
                </div>
              </div>
            </div>
          </a>

        </div> 
        
      </SwiperSlide>
      
      <div class="absolute bottom-0 right-0 z-50 p-3">
        <SwiperControls />
      </div>
      
    </Swiper>

  </div>
</template>
