<script setup>
  const config = useRuntimeConfig()
  const tmp_id = useCookie('tmp_id')
  const productsStore = useProductsStore()  
  const { signIn, token, data, status, lastRefreshedAt } = useAuth()

  const { data: session } = await useFetch(`${ config.public.baseURL }u/session/`, {
    method: 'POST',    
    headers: {
      "Authorization": token.value,
    },
    body: {
      "tmp_id": tmp_id.value
    }
  }).catch((error) => error.data)
  
  /// Обновляем сессию на полученную из профиля
  tmp_id.value = session.value.tmp_id

  /// Получаем данные о просмотренных товарах
  if (session.value) {
    const { data: tmp_data } = await useFetch(`${ config.public.baseURL }u/uwatch/`, {
      headers: {
        "Authorization": session.value.tmp_id,
      }
    }).catch((error) => error.data)
    productsStore.restoreState(tmp_data.value)
  }



</script>


<template>
  <div class="">
    <AppHeader />
    <AppNavbar />

    <div class="container mx-auto max-w-6xl px-4 py-2 lg:px-8">
      <div class="bg-white dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700">


        <div v-if="status === 'authenticated'" class="min-h-[50vh]">
          
          <div class="grid grid-cols-1 lg:flex gap-4 px-4 py-4">
            <div class="flex lg:flex-col gap-4 lg:w-[220px] lg:py-8">
              
              <nuxt-link :to="{ name: 'cts' }" class="">Каталог</nuxt-link>
              <nuxt-link :to="{ name: 'cart' }" class="">Корзина</nuxt-link>
              <nuxt-link :to="{ name: 'lk' }" class="">Избранное</nuxt-link>
              <nuxt-link :to="{ name: 'compare' }" class="">В сравнении</nuxt-link>
             
            </div>

            <div class="grid grid-cols-1 md:flex gap-4 w-full">
              <div class="bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 p-2 rounded-md md:w-[520px] shadow-md shadow-black/20">
                <p class="border-b border-gray-600 px-0.5">Данные профиля</p>
                <div class="py-6">
                  <div class="grid grid-cols-2 items-center gap-4">
                    <p class="text-sm">Логин:</p>
                    <p class="">{{ data.username }}</p>                    
                  </div>
                  <div class="grid grid-cols-2 items-center gap-4">
                    <p class="text-sm">Имя</p>
                    <p class="">{{ data.first_name }}</p>                    
                  </div>
                  <div class="grid grid-cols-2 items-center gap-4">
                    <p class="text-sm">Фамилия</p>
                    <p class="">{{ data.last_name }}</p>                    
                  </div>
                  <div class="grid grid-cols-2 items-center gap-4">
                    <p class="text-sm">Электронная почта</p>
                    <p class="">{{ data.email }}</p>                    
                  </div>
                  <div class="grid grid-cols-2 items-center gap-4">
                    <p class="text-sm">Номер телефона</p>
                    <p class="">{{ data.phone }}</p>                    
                  </div>
                  <div class="grid grid-cols-2 items-center gap-4">
                    <p class="text-sm">Город/адрес</p>
                    <p class="">{{ data.adress }}</p>                    
                  </div>
                </div>
              </div>

              <div class="grid grid-cols-1 h-[420px] gap-4 w-full">
                <div class="bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md shadow-md shadow-black/20 p-2">
                  <p class="border-b border-gray-600 px-0.5">История заказов</p>
                  <div class="flex items-center justify-center h-full w-full">
                    <p class="text-sm">Заказы не найдены</p>
                  </div>
                </div>
                <div class="bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md shadow-md shadow-black/20 p-2">
                  <p class="border-b border-gray-600 px-0.5">Акции и скидки</p>
                  <div class="flex items-center justify-center h-full w-full">
                    <p class="text-sm">Акции и скидки не найдены</p>
                  </div>
                </div>
              </div>              
            </div>



          </div>


          <div v-if="productsStore.viewed.length > 0" class="px-4 py-2">
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

        <div v-else class=" min-h-[50vh]">
          <div class="px-4 py-2">
            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 gap-4">
              <p class="">Вы не авторизованны</p>
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