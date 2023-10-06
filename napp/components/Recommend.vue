<script setup>
  const productsStore = useProductsStore()
  const config = useRuntimeConfig()

  const { data: recommends, pending, error} = await useFetch(`${ config.public.baseURL }c/recommend/`)


</script>

<template>
  <div class="container py-2 mx-auto px-4 max-w-6xl lg:px-8">
    <div class="p-2 bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-sm">
      <div class="">
        <blockquote class="text-2xl font-semibold italic text-center text-gray-700 dark:text-gray-300">
          
          <span class="px-4">ЕСЛИ НУЖНО</span>
          <span class="before:block before:absolute before:-inset-2 before:-skew-y-3 before:bg-blue-600 relative inline-block my-2">
            <span class="relative text-white"> СВАРОЧНОЕ ОБОРУДОВАНИЕ </span>
          </span>
          <span class="px-4">,ЗАКАЗЫВАЙТЕ ОНЛАЙН </span>
          <p class="mt-1">НА GLSVAR.KZ!</p>
          
        </blockquote>
      </div>
      <!-- <div class="grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
        <div v-for="product in recommends" :key="product.id" class="">
          <ProductSmall :product="product" />
        </div>
      </div> -->



      <div class="">

        <!-- <swiper
          :slidesPerView="4"
          :spaceBetween="10"
          :pagination="{
            clickable: true,
          }"
          :modules="'pagination'"
          class=""
        >

          <swiper-slide v-for="product in recommends" :key="product.id">
            <ProductSmall :product="product" />
          </swiper-slide>


        </swiper> -->

        <Swiper
          :modules="[SwiperPagination]"
          :slides-per-view="'auto'"
          :slidesPerView="4"
          :spaceBetween="10"
          :loop="true"
          :creative-effect="{
            prev: {
              shadow: false,
              translate: ['-20%', 0, -1],
            },
            next: {
              translate: ['100%', 0, 0],
            },
          }"
        >

        
          <SwiperSlide v-for="product in recommends" :key="product.id" class=" min-w-[280px]">
            <ProductSmall :product="product" />
          </SwiperSlide>
          <SwiperControls />
          
        </Swiper>

      </div>



    </div>
  </div>
</template>