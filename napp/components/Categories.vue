<script setup>
  const config = useRuntimeConfig()

  const { data: cts, pending, error } = await useFetch(`${ config.public.baseURL }c/ct/`)

</script>



<template>
  <div class="container mx-auto px-4 py-2 max-w-6xl lg:px-8">
    <div class="">


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
            
            <div class="">
              
              <div class="grid grid-cols-4 gap-2">
                <div v-for="ct in cts" :key="ct.id" class="break-inside-avoid-column">
                  <div class="">


                    <div class="">
                      
                      <div class="bg-white border border-gray-200 dark:border-gray-700 rounded-md py-2 px-2">
                        <div class="grid grid-cols-1 gap-4">
                          <div class="flex justify-center">
                            <img v-if="ct.icon" :src="`/${ct.icon}`" class="h-16" />
                          </div>
                          
                          <div class="flex justify-center">
                            <nuxt-link :to="{ name: 'prods', query: { ct: ct.id } }" class=" text-gray-700 text-xl transition-all">{{ ct.name }}</nuxt-link>              
                          </div>
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