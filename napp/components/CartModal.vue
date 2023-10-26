<script setup>
  const config = useRuntimeConfig()
  const router = useRouter()

  const productsStore = useProductsStore()
  // const notificationsStore = useNotificationsStore()


  const goCart = () => {
    productsStore.showCartModal()
    setTimeout(() => {
      console.log('go cart')
      router.push({ name: 'cart' })
    }, 500)
  }

  // watch на удаление последнего товара из корзины и скрытие модальки

</script>



<template>

  <div class="fixed z-50 w-full h-full bg-gray-500/50 backdrop-blur-sm">
    <div class="flex items-center justify-center h-full">
      <div class="h-full w-full flex items-center justify-center">
        

        <div class="container mx-auto px-4 lg:max-w-4xl lg:px-8">
          <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <div class="">

              <div class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-700">
                <h3 class="text-xl font-semibold text-gray-800 dark:text-white">
                  Товар добавлен в корзину
                </h3>
                <button @click="productsStore.showCartModal" type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="defaultModal">
                  <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                  <span class="sr-only">Закрыть окно</span>
                </button>
              </div>


              <div class="p-6 space-y-6 h-96 overflow-y-auto">
                
                <div class="overflow-x-auto w-full">
                  <div class="">

                    <div class="grid gap-2 px-2 py-2 border-b border-gray-300 dark:border-gray-700">
                      <div class="flex text-gray-600 dark:text-gray-100">
                        <div class="flex justify-center w-24"><p class="text-sm">Изображение</p></div>
                        <div class="flex justify-center w-1/2"><p class="text-sm">Наименование</p></div>
                        <div class="flex justify-center w-32"><p class="text-sm">Количество</p></div>
                        <div class="flex justify-center w-32"><p class="text-sm">Наличие</p></div>
                        <div class="flex justify-center w-32"><p class="text-sm">Стоимость</p></div>
                        <div class="flex justify-center w-20"><p class="text-sm">Удалить</p></div>
                      </div>
                    </div>

                    <div class="grid gap-2 text-gray-700 dark:text-gray-300">
                      <transition-group tag="div" name="left-emergence">
                        <div v-for="product in productsStore.cart" :key="product.id" class="my-4 border-t border-gray-300 dark:border-gray-700">
                          <div class="flex items-center gap-2">
                            <div class="flex justify-center items-center w-24 bg-white rounded-md">
                              <img :src="product.preview_image" :alt="product.name" width="235px" height="177px" class="rounded-md w-20 py-2" />
                            </div>
                            <div class="flex justify-center w-1/2">
                              <p class="text-sm text-center">{{ product.name }}</p>
                            </div>
                            <div class="flex justify-center w-32">
                              <button  @click="productsStore.changeQuantity(product, 'del')" class="mdi mdi-minus cursor-pointer"></button>
                              <div class="mx-2"><p>{{ product.quantity }}</p></div>
                              <button @click="productsStore.changeQuantity(product, 'add')" class="mdi mdi-plus cursor-pointer"></button>
                            </div>
                            <div class="flex justify-center w-32">
                              <p v-if="product.status === 'stock'" class="text-sm">в наличии</p>
                              <p v-if="product.status === 'order'" class="text-sm">под заказ</p>
                            </div>
                            <div class="flex justify-center w-32"><p class="text-sm">{{ product.price.toLocaleString() }} руб/шт</p></div>
                            <div class="flex justify-center w-20">
                              <button @click="productsStore.addProduct('cart', product)" class="mdi mdi-24px mdi-close cursor-pointer"></button>
                            </div>
                          </div>
                        </div>
                      </transition-group>
                    </div>
                  </div>
                </div>
              </div>


              <div class="grid grid-cols-1 items-end justify-between p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-700">
                <div class="">
                  <div class="flex items-center mb-4">
                    <input id="default-checkbox" type="checkbox" v-model="productsStore.cartAlertBlock" class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-700">
                    <label for="default-checkbox" class="ml-2 text-sm font-medium text-gray-700 dark:text-gray-300 cursor-pointer">Не показывать больше</label>
                  </div>
                </div>
                <div class="flex justify-center gap-2 w-full md:justify-end">
                  <button @click="productsStore.showCartModal">
                    <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                      <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                        <p class="px-5 py-2.5">Продолжить покупки</p>
                      </div>
                    </div>
                  </button>                  
                  
                  <button @click="goCart" data-modal-toggle="defaultModal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Перейти в корзину</button>
                </div>
              </div>


            </div>


          </div>
        </div>


      </div>        
    </div>
  </div>
</template>