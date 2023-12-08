<script setup>

  const config = useRuntimeConfig()
  const tmp_id = useCookie('tmp_id')
  const productsStore = useProductsStore()
  const notificationsStore = useNotificationsStore()

  const delCompProd = (id) => {
    console.log('ID ', id)
    $fetch(`${ config.public.baseURL }u/uwatch/`, {
      method: 'DELETE',
      headers: { "Authorization": tmp_id.value, },
      body: { "comp": id }
    })
  }

  const getPropValue = (props, name) => {
    let value = null
    props.forEach((el) => {
      if (el.name === name) {
        value = el.value
      }
    })
    return value
  }



</script>

<template>
  <div>
    <AppHeader />

    <div class="container mx-auto py-2 px-4 max-w-6xl lg:px-8">

      <div class="">
        <transition name="fade" mode="out-in">
          <div id="comp-data" v-if="productsStore.comp.length > 0" class="">

            <div class="">

              <transition-group tag="div" name="left-emergence" class="grid grid-cols-2 lg:grid-cols-4 gap-4">
                <div v-for="product in productsStore.comp.slice(-4)" :key="product.id" class="">

                  <ProductSmall :product="product" />
                  <div class="flex items-center justify-end mt-2">
                    <button @click="productsStore.addProduct('comp', product); notificationsStore.pushToast({id: product.id, type: 'success', text: 'Товар удалён из сравнения'}); delCompProd(product.id)" class="text-sm">Удалить из сравнения</button>
                  </div>

                </div>
              </transition-group>
            </div>


            <div class="bg-white rounded-md dark:bg-gray-800 border border-gray-200 dark:border-gray-700 my-4">
              <div class="px-2 py-4 bg-gray-200 dark:bg-gray-700 border-b border-gray-200 dark:border-gray-600">
                <p class="text-base">Сравнение характеристик:</p>
              </div>

              <div v-for="prop in productsStore.comp[0].propstrmodel" :key="prop.id" class="group dark:hover:bg-gray-700 duration-500 transition-all py-2">


                <div class="border-b border-gray-200 dark:border-gray-700 dark:group-hover:border-gray-600 transition-all">
                  <p class="text-sm dark:text-gray-400 font-semibold px-4 py-1">{{ prop.name }}</p>
                </div>

                <div class="grid grid-cols-2 lg:grid-cols-4 items-center gap-4">
                  <div v-for="product in productsStore.comp.slice(0, 4)" :key="product.id">
                    <div class="px-4 my-2">
                      <div v-if="getPropValue(product.propstrmodel, prop.name)">
                        <p class="text-sm dark:text-gray-100">{{ getPropValue(product.propstrmodel, prop.name) }}</p>
                      </div>
                      <div v-else>
                        <p class="text-sm dark:text-gray-100 mdi mdi-minus"></p>
                      </div>
                    </div>
                    
                  </div>            
                </div>

              </div>
            </div>



          </div>

          <div v-else class="bg-white dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700">
            <div class="flex items-center justify-center min-h-[50vh]">
              <p class="text-base">Нет товаров в сравнении</p>
            </div>
          </div>

        </transition>


      </div>


      
    </div>

    <AppFooter />
  
  </div>
</template>