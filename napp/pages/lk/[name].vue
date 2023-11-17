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
          
          <div class="flex px-4 py-4">
            <div class="grid grid-cols-1 w-[240px] gap-2">

              <div class="text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                  <p class="text-white text-sm w-full text-center py-1.5">Профиль</p>
                </div>
              </div>
              <div class="text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                  <p class="text-white text-sm w-full text-center py-1.5">Корзина</p>
                </div>
              </div>
              <div class="text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                  <p class="text-white text-sm w-full text-center py-1.5">Избранное</p>
                </div>
              </div>
              <div class="text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                  <p class="text-white text-sm w-full text-center py-1.5">В сравнении</p>
                </div>
              </div>
            </div>


            <div class="">

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