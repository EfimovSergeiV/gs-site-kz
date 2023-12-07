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


  const { data: extra } = await useFetch(`${ config.public.baseURL }u/user-data/`, {
    method: 'GET',    
    headers: {
      "Authorization": token.value,
    },}).catch((error) => error.data)

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
              <nuxt-link :to="{ name: 'compare' }" class="">Обратная связь</nuxt-link>
             
            </div>

            <div class="grid grid-cols-1 md:flex gap-4 w-full">
              <div class="bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 p-2 rounded-md md:w-[520px] shadow-md shadow-black/20">
                <p class="border-b border-gray-300 dark:border-gray-600 px-0.5">Данные профиля</p>
                <div class="">



                  <div class="py-2">
                    <p class="text-sm">Вы:</p>
                    <div class="flex gap-2 items-center justify-center">
                      <p class="">{{ data.first_name }}</p>
                      <p class="">{{ data.last_name }}</p>
                    </div>
                  </div>

                  <div class="py-2">
                    <p class="text-sm">Город/адрес:</p>
                    <div class="flex gap-2 items-center justify-center">
                      <p class="">{{ data.adress }}</p>  
                    </div>
                  </div>

                  <div class="py-2">
                    <p class="text-sm">Данные для входа:</p>
                    <div class="grid grid-cols-1 my-4 border-l-2 border-gray-300 dark:border-gray-600">
                      <p class=""><span class="text-sm px-4">Логин:</span>{{ data.username  }}</p>
                      <p class="text-xs py-2 px-4">сменить пароль</p>
                    </div>
                  </div>



                  <div class="py-2">
                    <p class="text-sm">Ваши контакты:</p>
                    <div class="grid grid-cols-1 my-4 border-l-2 border-gray-300 dark:border-gray-600">
                      <p class=""><span class="text-sm px-4">тел:</span>{{ data.phone }}</p>
                      <p class=""><span class="text-sm px-4">email:</span>{{ data.email }}</p>
                    </div>
                  </div>

                </div>
              </div>

              <div class="grid grid-cols-1 gap-4 w-full">
                <div class="bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md shadow-md shadow-black/20 p-2">
                  <p class="border-b border-gray-300 dark:border-gray-600 px-0.5">История заказов</p>

                  <div id="" v-if="extra.userdata.orders.length > 0" class=" h-[160px] w-full">
                    <div class="flex flex-wrap gap-2 justify-start py-4">
                      <div v-for="order in extra.userdata.orders" :key="order.id" class="">
                        <div class="bg-white dark:bg-gray-800 rounded-xl border hover:border-gray-300 dark:border-gray-700 border-gray-200 hover:dark:border-gray-700 transition-all shadow-md">
                          
                          <div class="flex items-center justify-center py-1 px-4">
                            <nuxt-link :to="{ name: 'order', hash: `#${ order.region_code }` }" class="text-[10px] md:text-xs">{{ order.region_code }}</nuxt-link>
                          </div>
                        
                        </div>
                      </div>          
                    </div>
                  </div>

                  <div v-else class="flex items-center justify-center h-[160px] w-full">
                    <p class="text-sm">Заказы не найдены</p>
                  </div>
                </div>

                <div class="bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md shadow-md shadow-black/20 p-2">
                  <div class="">
                    <p class="py-2 px-0.5">Избранные товары</p>
                    <div v-if="productsStore.like.length > 0" class="">
                      <Swiper
                        class=""
                        :modules="[]"
                        :slidesPerView="'auto'"
                        :loop="true"
                        :spaceBetween="10"
                      >
                      
                        <SwiperSlide  v-for="product in productsStore.like" :key="product.id" class="">
                          <ProductSmall :product="product" />
                        </SwiperSlide>

                        <div class="absolute bottom-0 right-0 py-1 px-1 z-40">
                          <SwiperControls class="bg-gray-100 rounded-full border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 dark:bg-gray-700 transition-all duration-500 px-1" />
                        </div>

                      </Swiper>                  
                    </div>
                    <div v-else class="">
                      <div class="h-full w-full flex items-center justify-center">
                        <p class="text-sm py-4">Нет товаров</p>
                      </div>
                    </div>
                  </div>
                </div>




                <!-- <div class="relative bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md shadow-md shadow-black/20 p-2">
                  <p class=" px-0.5">Избранные товары</p>
                  <div class="mt-4">

                    <div v-if="productsStore.like.length > 0" class="">
                      <Swiper
                        class=""
                        :modules="[]"
                        :slidesPerView="'auto'"
                        :loop="true"
                        :spaceBetween="10"
                      >
                      
                        <SwiperSlide  v-for="product in productsStore.like" :key="product.id" class="">
                          <ProductSmall :product="product" />
                        </SwiperSlide>

                        <div class="absolute bottom-0 right-0 py-1 px-1 z-40">
                          <SwiperControls class="bg-gray-100 rounded-full border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 dark:bg-gray-700 transition-all duration-500 px-1" />
                        </div>

                      </Swiper>
                    </div>

                    <p v-else class="text-sm">Нет товаров</p>

                  </div>
                </div> -->
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