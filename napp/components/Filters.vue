<script setup>
  const route = useRoute()
  const router = useRouter()
  // const config = useRuntimeConfig()
  
  const notificationsStore = useNotificationsStore()
  const props = defineProps(['brands','props'])

  
  const filters = ref({ "brnd": [],})

  const applyFilter = () => {
    notificationsStore.statusFilterComponent()
    router.push({
      name: 'prods',
      query: {
        ...route.query,
        ...filters.value,
        page: 1
      },
    })
  }

  const clearFilter = () => {
    filters.value["brnd"] = []
    props.props.forEach(element => filters.value[element.prop_alias] = [])
    applyFilter()
  }

  onMounted(() => {
    /// Присваиваем всем свойствам тип массива 
    /// Пробегаем по роутеру, закидываем в массивы параметры фильтров
    if ("brnd" in route.query) {
      if (typeof route.query["brnd"] === 'string') {
        filters.value["brnd"].push(route.query["brnd"])
      } else {
        filters.value["brnd"] = route.query["brnd"]
      }
    }

    props.props.forEach(element => {
      filters.value[element.prop_alias] = []
      if ( element.prop_alias in route.query ) {
        if (typeof route.query[element.prop_alias] === 'string') {
          filters.value[element.prop_alias].push(route.query[element.prop_alias])
        } else {
          filters.value[element.prop_alias] = route.query[element.prop_alias]
        }
      }
    })
  })

</script>



<template>
 
  <div class="bg-gradient-to-br from-gray-300 to-gray-200 dark:from-gray-900 dark:to-gray-800 w-s creen md:w-[420px] h-screen overflow-y-auto border-r border-gray-300 dark:border-gray-700">
    <div class="p-4 relative">


      <div class="flex items-center justify-between">
        <div class=""><p class="">Фильтр по товарам</p></div>
        <div class=""><button @click="notificationsStore.statusFilterComponent" class="mdi mdi-24px mdi-close cursor-pointer"></button></div>
      </div>

      <div class="overflow-y-auto">

        <div class="py-2">
          <div class="break-inside-avoid-column border border-gray-300 hover:border-gray-400 dark:border-gray-700 dark:hover:border-gray-600 rounded-md p-1 duration-700 transition-all">
            
            <div id="checkbox-form my-2">
              <p class="text-sm mb-2 m-1">Производитель</p>


              <div class="flex flex-wrap">
                <div class="flex items-center mr-4 p-1" v-for="brand in props.brands" :key="brand.id">

                  <input 
                    :id="brand.id"
                    :value="brand.id"
                    type="checkbox"
                    v-model="filters.brnd" 
                    class="w-4 h-4 
                      rounded text-gray-700 focus:ring-0 
                      focus:ring-gray-300 ring-offset-gray-300 bg-gray-700 border-gray-300
                      dark:focus:ring-gray-700 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-700
                    " >
                  <label :for="brand.id" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">{{ brand.brand }}</label>
                
                </div>
              
              </div>                      
            </div>

          </div>
        </div>



        <div class="" v-for="prop in props.props" :key="prop.id">
          
          <div class="py-2" v-if="prop.propwidget == 'value'">
            <div class="break-inside-avoid-column border border-gray-300 hover:border-gray-400 dark:border-gray-700 dark:hover:border-gray-600 rounded-md p-1 duration-700 transition-all">
              
              <div id="checkbox-form my-2">
                <p class="text-sm mb-2 m-1">{{ prop.name }}</p>
                <div class="flex flex-wrap">
                  <div class="flex items-center mr-4 p-1" v-for="ops in prop.prop_ops" :key="ops.id">
                    
                    <input 
                      :id="ops.id" 
                      v-model="filters[prop.prop_alias]" 
                      :value="ops.opskey" 
                      type="checkbox" 
                      class="w-4 h-4 
                        rounded text-gray-700 focus:ring-0 
                        focus:ring-gray-300 ring-offset-gray-300 bg-gray-700 border-gray-300
                        dark:focus:ring-gray-700 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-700"
                        >
                    <label :for="ops.id" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">{{ ops.ops }}</label>


                  </div>
                
                </div>                      
              </div>

            </div>
          </div>

        </div>
      </div>

    </div>    

    <div class="absolute bottom-0 right-0 w-full">
      <div class="bg-gray-300 dark:bg-gray-800">
        <div class="flex justify-end p-4">
          <button @click="clearFilter" class="text-base mx-2 mdi mdi-filter-variant-minus text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100"> Очистить</button>
          <button @click="applyFilter" class="text-base mx-2 mdi mdi-filter-variant-plus text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100"> Применить</button>
        </div>                
      </div>
    </div>

  </div>
</template>