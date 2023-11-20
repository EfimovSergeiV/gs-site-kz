<script setup>
  const { signIn, token, data, status, lastRefreshedAt } = useAuth()

  const productsStore = useProductsStore()

</script>

<template>
  <div class="">
    <AppHeader />
    <AppNavbar />

    <div class="container mx-auto max-w-6xl px-4 py-2 lg:px-8">
      <div class="bg-white dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700">
        <div v-if="productsStore.like.length > 0" class=" min-h-[50vh]">
          <div class="px-4 py-2">
            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 gap-4">
              <div v-for="product in productsStore.like" :key="product.id">
                <ProductCard :product="product" />
              </div>
            </div>
          </div>
        </div>

        <div v-else class="min-h-[50vh]">
          
          <div class="grid grid-cols-1 lg:flex gap-4 px-4 py-4">
            <div class="flex lg:flex-col gap-4 lg:w-[220px]">

            <!-- 
              <div class="py-4">
                <p class="">Ваш профиль</p>
              </div> 
            -->
              
              <nuxt-link to="#" class="">Каталог</nuxt-link>
              <nuxt-link to="#" class="">Корзина</nuxt-link>
              <nuxt-link to="#" class="">Избранное</nuxt-link>
              <nuxt-link to="#" class="">В сравнении</nuxt-link>
             
            </div>

            <div class="grid grid-cols-1 md:flex gap-4 w-full">
              <div class="border border-gray-700 p-2 rounded-md md:w-[520px]">
                <p class="">Данные профиля</p>
              </div>

              <div class="grid grid-cols-1 h-[420px] gap-4 w-full">
                <div class="border border-gray-700 rounded-md p-2">
                  <p class="">История заказов</p>
                </div>
                <div class="border border-gray-700 rounded-md p-2">
                  <p class="">Акции и скидки</p>
                </div>
              </div>              
            </div>



          </div>


          <div class="px-4 py-2">
            <p class="py-4"> Вы недавно смотрели</p>

            <div class="">
              <Swiper
                class=""
                :modules="[]"
                :slidesPerView="'auto'"
                :loop="true"
                :spaceBetween="10"
              >
              
                <SwiperSlide  v-for="product in productsStore.viewed" :key="product.id" class="">
                  <ProductCard :product="product" />
                </SwiperSlide>

                <div class="absolute bottom-0 right-0 py-1 px-1 z-40">
                  <SwiperControls class="bg-gray-100 rounded-full border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 dark:bg-gray-700 transition-all duration-500 px-1" />
                </div>

              </Swiper>
            </div>


          </div>


        </div>
      </div>
    </div>

    <AppFooter />

  </div>
</template>

<style scoped>
.swiper-slide {
  width: 260px;
}
</style>