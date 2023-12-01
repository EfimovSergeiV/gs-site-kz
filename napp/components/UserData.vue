<script setup>
  const config = useRuntimeConfig()
  const tmp_id = useCookie('tmp_id')
  const productsStore = useProductsStore()

  const selected = ref('random')

  const buttons = ref(
    [
      { key: 'viewed', title: 'Вы смотрели' },
      { key: 'like', title: 'Вам понравилось' },
      { key: 'comp', title: 'В сравнении' },
      { key: 'articles', title: 'Статьи' },
    ]
  )

  const { data: random } = await useFetch(`${ config.public.baseURL }c/random/`)

  const products = ref()


  onMounted( async () => {
    console.log('mounted work ', products.value)
    if (!products.value) {
      products.value = []
      for (const product in random.value) {
        setTimeout(() =>  products.value.push(random.value[product]), product * 100);        
      }
    }
  })


  const changeProducts = (key) => {
    products.value = []
    if (key === 'random') {
      for (const product in random.value) {
        setTimeout(() =>  products.value.push(random.value[product]), product * 100);        
      }
    } else {
      for (const product in productsStore[key]) {
        setTimeout(() =>  products.value.push(productsStore[key][product]), product * 100);        
      }      
    }

  }

</script>


<template>
  <div id="user-data-view" class="">
    <div class="container mx-auto px-4 py-2 max-w-6xl lg:px-8">


      <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md">
        
        <div class="px-2 mt-2">
          <div class="flex flex-row flex-wrap gap-2">
            
            
            <div v-for="button in buttons" :key="button.key" class="">
              <div :id="`${button.key}-active`" v-if="selected === button.key" class="flex items-center justify-center px-4 py-0.5 border border-gray-200 hover:border-gray-300 dark:border-gray-500 bg-gray-200 dark:bg-gray-600 transition-all rounded-md shadow-sm shadow-black/30">
                <button @click="selected = key; changeProducts('random')" class="text-xs md:text-sm text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-200">{{ button.title }}</button>
              </div>
              <div v-else :id="`${button.key}-nonactive`" class="flex items-center justify-center px-4 py-0.5 border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 bg-gray-100 dark:bg-gray-700 transition-all rounded-md shadow-sm shadow-black/30">
                <button @click="selected = button.key; changeProducts(button.key)" class="text-xs md:text-sm text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-200">{{ button.title }}</button>
              </div>
            </div>              
            

          </div>
        </div>

        <div class="px-2 py-2">
          <div class="h-36">
            
            <div v-if="products && products.length > 0" class="">
              <transition name="fade" mode="out-in">
                <Swiper
                  class=""
                  :modules="[]"
                  :slidesPerView="'auto'"
                  :loop="true"
                  :spaceBetween="10"
                >


                  <SwiperSlide :id="`slide-${product.id}`" v-for="product in products" :key="product.id" class="">

                    <div id="product-small" class="grid grid-cols-1 content-between bg-gray-100 rounded-md border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 dark:bg-gray-700 transition-all shadow-md p-2 h-36">
                      <nuxt-link :to="{ name: 'product-id', params: { id: product.id } }">
                        <div class="flex items-center justify-between gap-2">
                          <div class="">
                            <p class="text-xs">{{ product.name.slice(0,80) }}</p>
                          </div>
                          <div class="">
                            <div class="flex items-center justify-center bg-white w-[80px] h-[60px] rounded-md">
                              <img :src="product.preview_image" width="70" :alt="product.name" />
                            </div>
                          </div>
                        </div>                  
                      </nuxt-link>

                      <div v-if="selected in ['like', 'comp',]" class="flex items-center justify-end">
                        <button class="text-xs">Удалить из списка</button>
                      </div>

                      <div class="flex items-center gap-4">
                        <div class="">

                          <CartBtnSmall v-if="product.price" cls="px-4 py-2" :product="product" />
                          <button @click="productsStore.addRequestPrice(product)" v-else class="">
                            <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                              <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                                <p class="text-white text-sm w-36 md:w-24 py-1.5">Запросить</p>
                              </div>
                            </div>
                          </button>
                          
                        </div>
                        <div class="">
                          <div v-if="product.price" class="flex gap-1 justify-end">
                            <p class="text-base font-bold dark:text-gray-300">{{ product.price.toLocaleString() }}</p>
                            <p class="text-base font-bold dark:text-gray-300">тг</p>
                          </div>        
                          <p v-else class="text-xs text-right dark:text-gray-300">Стоим. по запросу</p>
                        </div>
                      </div>
                    </div>
                  </SwiperSlide>





                  <div class="absolute bottom-0 right-0 py-1 px-1 z-40">
                    <SwiperControls class="bg-gray-100 rounded-full border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 dark:bg-gray-700 transition-all duration-500 px-1" />
                  </div>

                </Swiper>
              </transition>
            </div>
          

            <div v-else class="px-2 py-2">
              <div class="h-36 flex items-center justify-center">
                <p class="text-sm text-gray-500 dark:text-gray-500">Тут пока ничего нет</p>
              </div>
            </div>

          </div>
        </div>

        
      </div>


    </div>
  </div>
</template>

<style scoped>
.swiper-slide {
  width: 260px;
}
</style>