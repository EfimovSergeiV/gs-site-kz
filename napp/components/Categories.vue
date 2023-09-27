<script setup>
  const config = useRuntimeConfig()

  const { data: cts, pending, error } = await useFetch(`${ config.public.baseURL }c/ct/`)

</script>



<template>
  <div class="container mx-auto px-4 py-2 max-w-6xl lg:px-8">
    <div class="bg-white border-gray-200 shadow-sm border dark:bg-gray-800 dark:border-gray-700 rounded-md">


      <p v-if="pending">Загрузка данных...</p>
      <div v-else-if="error">
        <div class="my-6 lg:my-10">
          <pre>Ошибка: Данные не получены </pre>
          <pre class="text-xs">{{ error.data }}</pre>
        </div>
      </div>


      <div v-else  class="">

        <div class="">
          <div class="">
            
            <div class="px-2 py-2">
              
              <div class="columns-1 xl:columns-3 lg:columns-4">
                <div v-for="ct in cts" :key="ct.id" class="break-inside-avoid-column">
                  <div class="">


                    <div class="py-2 ">
                      
                      <div class="bg-gray-100/90 dark:bg-gray-700 border border-gray-200 dark:border-gray-700 rounded-md py-2 px-2">
                        <div class="py-2">
                          <nuxt-link :to="{ name: 'prods', query: { ct: ct.id } }" class=" text-gray-700 dark:text-gray-100 text-base transition-all">{{ ct.name }}</nuxt-link>              
                        </div>

                        <div>
                          <ul>
                            <li v-for="sct in ct.inserted" :key="sct.id" class="inline-block ">
                              <nuxt-link :to="{ name: 'prods', query: { ct: sct.id } }" class="text-gray-700 mr-3 text-sm hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100 transition-all">{{ sct.name }}</nuxt-link>
                            </li>
                          </ul>
                        </div>                                  
                      </div>





                    </div>


                  </div>
                </div>
              </div>
              
            </div>

            
          </div>  
        </div>

      </div>
    </div>

  </div>
</template>