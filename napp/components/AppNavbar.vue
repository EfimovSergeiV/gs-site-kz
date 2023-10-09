<script setup>
  import debounce from "lodash.debounce";


  const config = useRuntimeConfig()
  const { signIn, signOut, token, data, status, lastRefreshedAt } = useAuth()
  // const { data: products } = await useFetch(`${ config.public.baseURL }c/neues/`) /// for debug styles

  const search = ref('')
  const products = ref([])

  const debouncedHandler = debounce(async query => {


        const { data: prods }  = await useFetch(`${ config.public.baseURL }c/search/`, {
          method: 'POST',
          body: {
            name: search
          }
        }).then(
          console.log(prods)
          // products.value = ( await prods.value )
        ).catch(
          console.log('Bad request')
        )
        
               

  



  }, 300);

  watch(search, (searchRequest) => {
    debouncedHandler()
  })


</script>


<template>
  <div class="">
    <div class="container mx-auto py-2 px-4 max-w-6xl lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 bg-white dark:bg-gray-800 border dark:border-gray-700 px-2 py-2 rounded-md">
        
        <div class="w-full">
          <div class="relative w-full group">
            <div class="flex absolute inset-y-0 left-0 items-center  pointer-events-none">
              <p class="mdi mdi-24px mdi-store-search px-3 text-gray-700 dark:text-gray-700"></p>
            </div>
            <input 
              v-model="search" 
              type='search'
              id="phone"
              disabled
              placeholder="Поиск по каталогу"
              class="bg-gray-50 border border-gray-300 text-gray-700 font-semibold dark:text-gray-700 text-sm 
              uppercase rounded-lg focus:ring-gray-300/0 focus:border-gray-300 block 
              w-full pl-12 p-2 dark:bg-white dark:border-gray-700 dark:placeholder-gray-500
              ring-0 dark:focus:ring-gray-600/0 dark:focus:border-gray-700" >
            
              <div v-if="search.length > 1" class="absolute py-2 z-30 w-full invisible group-hover:visible ease-in-out transition-opacity duration-100 opacity-0 group-hover:opacity-100">
              <div class="bg-white/90 dark:bg-gray-700/80 border border-gray-100 dark:border-gray-700 backdrop-blur-md rounded-md py-2 px-2 min-h-[80px]">
                <div class="px-2 h-96 overflow-y-auto my-2">
                  <div v-if="search.length > 3 && products.length === 0" class="">
                    <p class="">Ничего не найдено</p>
                  </div>
                  <div v-if="search.length === 0" class="">
                    <p class="">Введите запрос</p>
                  </div>
                  <transition-group name="fade">
                    <div class="px-2 py-2 my-1 bg-gray-100 dark:bg-gray-800 border border-gray-200 hover:border-gray-300 dark:border-gray-500 hover:dark:border-gray-400 rounded-md transition-all" v-for="product in products" :key="product.id">
                      <nuxt-link :to="{ name: 'product-id', params: { id: product.id }}" class="">
                        <div class="flex gap-4">
                          <div class="">
                            <img class="bg-white w-20 p-1 rounded-md" :src="product.preview_image" />
                          </div>
                          <div class="">
                            <p class="text-sm">{{ product.name }}</p>
                            <p v-if="product.price > 0" class="">{{ product.price.toLocaleString() }} <span class="text-xs">〒</span></p>
                            <p v-else class="text-xs">Стоимость по запросу</p>
                          </div>
                        </div>
                      </nuxt-link>
                    </div>
                  </transition-group>
                </div>
              </div>              
            </div>
          </div> 
        </div>

        <div class="grid grid-cols-2 md:flex items-center gap-2 ">
          
          <nuxt-link :to="{ name: 'lk-name', params: { name: data.username} }"  v-if="status === 'authenticated'" class="bg-blue-500 hover:bg-blue-600 flex items-center h-full w-full border dark:border-gray-100/10 rounded-lg transition-all duration-700">
            <div class="flex items-center gap-2 text-gray-100 bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg h-full w-full min-h-[2rem]">
              <span class="px-2 mdi mdi-star border-r border-gray-100/50"></span>
              <p class="text-sm"> Избранное</p>
            </div>
          </nuxt-link>
          <nuxt-link :to="{ name: 'lk-name', params: { name: 'guest' } }" v-else class="bg-blue-500 hover:bg-blue-600 flex items-center h-full w-full border dark:border-gray-100/10 rounded-lg transition-all duration-700">
            <div class="flex items-center gap-2 text-gray-100 bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg h-full w-full min-h-[2rem]">
              <span class="px-2 mdi mdi-star border-r border-gray-100/50"></span>
              <p class="text-sm"> Избранное</p>
            </div>
          </nuxt-link>


          <nuxt-link :to="{ name: 'compare' }" class="bg-blue-500 hover:bg-blue-600 flex items-center h-full w-full border dark:border-gray-100/10 rounded-lg transition-all duration-700">
            <div class="flex items-center gap-2 text-gray-100 bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg h-full w-full min-h-[2rem]">
              <span class="px-2 mdi mdi-align-horizontal-right border-r border-gray-100/50"></span>
              <p class="text-sm "> Сравнение</p>
            </div>
          </nuxt-link>
          <nuxt-link :to="{ name: 'cart' }" class="bg-blue-500 hover:bg-blue-600 flex items-center h-full w-full border dark:border-gray-100/10 rounded-lg transition-all duration-700">
            <div class="flex items-center gap-2 text-gray-100 bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg h-full w-full min-h-[2rem]">
              <span class="px-2 mdi mdi mdi-cart border-r border-gray-100/50"></span>
              <p class="text-sm "> Корзина</p>
            </div>
          </nuxt-link>
          <nuxt-link :to="{ name: 'about' }" class="bg-blue-500 hover:bg-blue-600 flex items-center h-full w-full border dark:border-gray-100/10 rounded-lg transition-all duration-700">
            <div class="flex items-center gap-2 text-gray-100 bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg h-full w-full min-h-[2rem]">
              <span class="px-2 mdi mdi-store-marker border-r border-gray-100/50"></span>
              <p class="text-sm "> Магазины</p>
            </div>
          </nuxt-link>
        </div>


      </div>
    </div>
  </div>
</template>