<script setup>
  const productsStore = useProductsStore()
  const props = defineProps(['product','related','analogue'])


</script>



<template>
  <div class="">

    <div class="mx-auto px-4 max-w-6xl lg:px-8 py-2">

      <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 p-2 mb-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <div class="">
            <div class="flex h-full min-h-[340px] bg-white rounded-md cursor-zoom-in relative" @click="productsStore.showProductImages(product.prod_img)">
              <div class="flex gap-4">


                <div class="px-3 py-3">
                  <div v-for="image in props.product.prod_img.slice(0, 4)" :key="image.id" class="w-[80px] h-[80px] rounded-md bg-white flex items-center justify-center">
                    <img :src="image.image" class="" />
                  </div>
                </div>


              </div>
              <div class="flex items-center justify-center w-full">
                <div class="bg-white p-4">
                  <img :src="props.product.preview_image" :alt="props.product.name" />
                </div>
              </div>

              <div v-if="props.product.brand" class="absolute top-0 right-0">
                <div class="px-4 py-2">
                  <img :src="props.product.brand.image" class="h-24" />
                </div>
                
              </div>

            </div>
          </div>

          <div class="">
            <div class="grid grid-cols-1 md:flex gap-2">
              <div class="flex items-center justify-end w-full md:order-last">
                <span class="flex gap-1 items-center text-xs">код товара:<p class="text-sm"> {{ props.product.vcode }}</p></span>
              </div>

              <div class="flex gap-2">
                <div class="border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 bg-gray-100 dark:bg-gray-700 rounded-md py-1 px-4 transition-all">
                  <div class="flex gap-2">
                    <CompBtn cls="px-5 py-2.5" :product="product" />
                    <p class="text-sm">Сравнить</p>
                  </div>
                </div>

                <div class="border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 bg-gray-100 dark:bg-gray-700 rounded-md py-1 px-4 transition-all">
                  <div class="flex items-center">
                    <div v-for="i in Math.ceil(props.product.rating)" :key="i" class="">
                      <svg aria-hidden="true" class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    </div>
                    <div v-for="i in 5 - Math.ceil(props.product.rating)" :key="i" class="">
                      <svg aria-hidden="true" class="w-5 h-5 text-gray-300 dark:text-gray-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    </div>
                  </div>
                </div>                
              </div>

            </div>

            <div class="py-4">
              <p class="text-base">{{ product.name }}</p>
            </div>

            <div class="border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 bg-gray-100 dark:bg-gray-700 transition-all px-4 py-2 rounded-md shadow-md shadow-black/20">
              
              <div class="flex justify-between items-center my-2">
                
                <div class="">
                  <div v-if="props.product.price" class="flex gap-1 items-center justify-end">
                    <p class="text-3xl font-bold dark:text-gray-300">{{ props.product.price.toLocaleString() }}</p>
                    <p class="text-3xl dark:text-gray-300 px-1">тг</p>
                  </div>                  
                  <p v-else class="text-sm font-bold dark:text-gray-300">Стоимость по запросу</p>
                </div>

                <div class="grid grid-cols-1 gap-4">
                  <div class="flex items-center justify-end">
                    <CartBtn v-if="props.product.price" :product="product" />    
                    
                    <button v-else @click="productsStore.addRequestPrice(product)" class="">
                      <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                        <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                          <p class="text-white text-base w-32 md:w-52 py-2.5">Запросить</p>
                        </div>
                      </div>
                    </button>

                                    
                  </div>
                </div>
              </div>

              <div class="flex justify-between items-center my-2">
                <div class="flex justify-end my-2">
                  <p v-if="props.product.status === 'stock'" class="text-sm">в наличии</p>
                  <p v-if="props.product.status === 'order'" class="text-sm">под заказ</p>
                </div>
                <div class="flex items-center justify-end">
                  <div class="flex gap-2">
                    <LikeBtn cls="px-5 py-2.5" :product="product"/>
                    <p class="text-sm">В избранное</p>
                  </div>
                </div>
              </div>
            </div>



            <div class="my-2">
              <p class="text-sm">Аналоги</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
              <div v-for="prod_analogue in analogue" :key="prod_analogue.id" class="">
                <ProductSmall :product="prod_analogue" />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-if="props.related.length > 0" class="pb-4">
        <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md p-2">
          <p class="my-2">Сопутствующие товары</p>
          <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-2">
            <div v-for="prod_related in related" :key="prod_related.id" class="">
              <ProductSmall :product="prod_related" />
            </div>
          </div>
        </div>
      </div>
      <div class="">


        <div class="grid grid-cols-1 md:flex gap-4">
          <div class="md:w-[400px] bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md p-2">
            <div class="">
              <p class="text-base">Документы:</p>
              <div v-if="props.product.prod_doc.length > 0 || props.product.prod_link.length > 0" class="grid grid-cols-1 gap-2 py-2">
                <div class="" v-for="file in props.product.prod_doc" :key="file.id">
                  <a class="text-sm mx-2" :href="file.doc" target="_blank">{{ file.name }}</a>
                </div>
                <div class="" v-for="doc in props.product.prod_link" :key="doc.id">
                  <a class="text-sm mx-2" :href="doc.url" target="_blank">{{ doc.name }}</a>
                </div>
              </div>
              <div v-else class="flex items-center justify-center h-full py-6">
                <p class=" text-sm text-gray-400 dark:text-gray-500">Ничего нет</p>
              </div>
            </div>
          </div>
          <div class="w-full">
            <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md p-2 mb-4 h-full">
              <p class="text-base">Характеристики:</p>
              <div v-if="props.product.propstrmodel.length > 0" class="columns-1 gap-8 py-2">
                <div v-for="param in props.product.propstrmodel" :key="param.id" class="border-b border-gray-300 hover:border-gray-400 dark:border-gray-700 dark:hover:border-gray-600">
                  <div class="flex justify-between">
                    <div class=""><small>{{ param.name }} :</small></div>
                    <div class="text-right"><small>{{ param.value }}</small></div>                
                  </div>
                </div>
              </div>
              <div v-else class="flex items-center justify-center py-6">
                <p class=" text-sm text-gray-400 dark:text-gray-500">Ничего нет</p>
              </div>
            </div>
          </div>

        </div>

        <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md p-2 mt-4">
          <p class="text-base my-2">Описание:</p>
          <div class="text-sm px-2 py-6" v-html="props.product.description"></div> 
        </div>        

      </div>
    </div>

  </div>
</template>
