<script setup>
  const { data: brands } = await useFetch('https://api.glsvar.ru/c/brands/')

  const filteredCarouselBrands = (brands) => {
    const truebrand = []
    brands.forEach((element) => {
      if (element.carousel === true) {
        truebrand.push(element)
      }
    })
    return truebrand

  }

</script>


<template>
  <div class="container mx-auto max-w-6xl px-4 lg:px-8 py-2">

    <div class="bg-gray-400 rounded-md border dark:border-gray-500 dark:bg-gray-600 shadow-md px-4 py-2">
      <Swiper
        class=""

        :modules="[SwiperAutoplay]"
        :slides-per-view="5"
        :autoplay="{
          delay: 4000,
          disableOnInteraction: false
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
        <SwiperSlide v-for="brand in filteredCarouselBrands(brands)" :key="brand.id">
          <nuxt-link :to="{ name: 'prods', query: { brnd: brand.id, page: 1 }}" class="flex items-center justify-center">
            <img
              :src="brand.image"
              class="w-14 md:w-20 lg:w-24"
            />                 
          </nuxt-link>
        </SwiperSlide>

      </Swiper>
    </div>

  </div>
</template>