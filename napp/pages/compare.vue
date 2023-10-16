<script setup>

  const productsStore = useProductsStore()


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
    <AppNavbar />

    <div class="container mx-auto py-2 px-4 max-w-6xl lg:px-8">

      <div class="">
        <transition name="fade" mode="out-in">
          <div id="comp-data" v-if="productsStore.comp.length > 0" class="">

            <div class="">


              <transition-group tag="div" name="left-emergence" class="grid grid-cols-2 lg:grid-cols-4 gap-4">

                
                <div v-for="product in productsStore.comp.slice(0, 4)" :key="product.id" class="">
                  <ProductSmall :product="product" />
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

          <div id="comp-leer" v-else class="bg-white dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700 min-h-[70vh]">
            <div class="flex gap-4 items-center justify-center h-full">

              <div class="flex items-center gap-8 my-8">
                <div class="grid gap-2 grid-cols-1">
                  <div class="mx-4 text-center">
                    <p class="text-2xl">У вас нет товаров для сравнения</p>
                  </div>
                  <div class="border-b border-gray-700 dark:border-gray-300"></div>
                  <div class="mx-4 text-center">
                    <nuxt-link :to="{ name: 'cts' }" class="text-sm hover:underline hover:text-gray-900 dark:hover:text-gray-100 ">Перейти в каталог</nuxt-link>
                  </div>
                </div>
                <div>
                  <p class="mdi mdi-close-outline text-3xl md:text-6xl"></p>
                </div>
              </div>

            </div>  
          </div>

        </transition>


      </div>


      
    </div>

    <AppFooter />
  
  </div>
</template>