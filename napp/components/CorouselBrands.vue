<script setup>
  const productsStore = useProductsStore()
  const config = useRuntimeConfig()

  const { data: brands } = await useFetch(`${ config.public.baseURL }c/brands/`)

  // const filteredCarouselBrands = (brands) => {
  //   const truebrand = []
  //   brands.forEach((element) => {
  //     if (element.carousel === true) {
  //       truebrand.push(element)
  //     }
  //   })
  //   return truebrand

  // }

</script>


<template>
  <div class="container mx-auto max-w-6xl px-4 lg:px-8 py-2">

    <!-- 
      :autoplay="{
          delay: 4000,
          disableOnInteraction: false
        }" 
    -->

    <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-sm px-2">
      <!-- <Swiper
        class=""
        :modules="[SwiperAutoplay]"
        :slides-per-view="5"
        :loop="true"
        :spaceBetween="10"

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
      
        <SwiperSlide v-for="brand in filteredCarouselBrands(brands)" :key="brand.id">
          <nuxt-link :to="{ name: 'prods', query: { brnd: brand.id, page: 1 }}" class="flex items-center justify-center bg-gray-100 h-12 md:h-20 rounded-md shadow-md shadow-black/50 my-2">
            <img
              :src="brand.image"
              class=" w-[142px]"
            />                 
          </nuxt-link>
        </SwiperSlide>

      </Swiper> -->
    </div>

  </div>
</template>