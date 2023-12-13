<script setup>
  const productsStore = useProductsStore()
  const config = useRuntimeConfig()

  const { data: recommends, pending, error} = await useFetch(`${ config.public.baseURL }c/recommend/`)


</script>

<template>
  <div class="container py-2 mx-auto px-4 max-w-6xl lg:px-8">
    <div class="p-2 bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-sm relative">
      <div class="">
        <blockquote class="text-2xl font-semibold italic text-center text-gray-700 dark:text-gray-300">
          
          <span class="px-4">ЕСЛИ НУЖНО</span>
          <span class="before:block before:absolute before:-inset-2 before:-skew-y-3 before:bg-blue-600 relative inline-block my-4 lg:my-2">
            <span class="relative text-white"> СВАРОЧНОЕ ОБОРУДОВАНИЕ </span>
          </span>
          <span class="px-4">,ЗАКАЗЫВАЙТЕ ОНЛАЙН </span>
          <p class="mt-1">НА GLSVAR.KZ!</p>
          
        </blockquote>
      </div>

      <div class="mb-1">
        <p class="">Рекомендуем:</p>
      </div>

      <div class="">
        <Swiper
          class=""
          :modules="[]"
          :slidesPerView="'auto'"
          :loop="true"
          :spaceBetween="10"
        >
        
          <SwiperSlide  v-for="product in recommends" :key="product.id" class="">
            <ProductSmall :product="product" />
          </SwiperSlide>

          <div class="absolute bottom-0 right-0 py-1 px-1 z-40">
            <SwiperControls class="bg-gray-100 rounded-full border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 dark:bg-gray-700 transition-all duration-500 px-1" />
          </div>

        </Swiper>
      </div>


    </div>
  </div>
</template>

<style scoped>
.swiper-slide {
  width: 260px;
}
</style>