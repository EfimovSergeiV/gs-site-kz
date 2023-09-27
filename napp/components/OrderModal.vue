<script setup>
  const productsStore = useProductsStore()
  const clientStore = useClientStore()


</script>


<template>
  <div id="order-modal" class="fixed z-50 w-full h-full bg-gray-500/50 backdrop-blur-sm">
    <div class="flex items-center justify-center h-full">
      <div class="h-full w-full flex items-center justify-center">
        

        <div class="container mx-auto px-4 lg:max-w-4xl lg:px-8">
          <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <div class="">

              <div class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-700">
                <h3 class="text-xl font-semibold text-gray-800 dark:text-white">
                  Ваш заказ успешно принят
                </h3>
                <button @click="clientStore.order = null" type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="defaultModal">
                  <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                  <span class="sr-only">Закрыть окно</span>
                </button>
              </div>


              <div class="flex items-center justify-center px-4 py-8 min-h-[20rem] ">
                <div class="grid grid-cols-1 gap-16">

                  <div class="text-center grid grid-cols-1 gap-2 ">
                    <p class="text-gray-700 dark:text-gray-300 text-xl"> Номер вашего заказа {{ clientStore.order }}</p>
                    <p class="text-gray-700 dark:text-gray-300"> Мы свяжемся с вами в ближайшее время</p>                    
                  </div>




                  <div class="flex items-center justify-center gap-4 py-2">
                    <button id="order-success" @click="clientStore.order = null" data-modal-toggle="defaultModal" type="button" class="text-gray-700 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Закрыть окно</button>

                    <nuxt-link id="link-order-data" :to="{ name: 'order', hash: `#${ clientStore.order }` }" @click="clientStore.order = null" class="text-center">
                      <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                        <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                          <p class="text-white text-base w-52 py-2">Страница заказа</p>
                        </div>
                      </div>
                    </nuxt-link>
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