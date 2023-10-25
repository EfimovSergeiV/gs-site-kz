<script setup>
  import cities from '@/cities.ts'

  const config = useRuntimeConfig()
  // const router = useRouter()

  const shopStore = useShopStore()
  const clientStore = useClientStore()
  // const notificationsStore = useNotificationsStore()


  const sendRequest = async () => {
    if ( (clientStore.client.city) && (clientStore.client.contact) ) {
      const { data: response } = await useFetch(`${ config.public.baseURL }o/request-price/`, {
        method: 'POST',
        body: {
          city: clientStore.client.city,
          contact: clientStore.client.contact,
          product: `id: ${ productsStore.requestPrice.id } vc: ${ productsStore.requestPrice.vcode } name: ${ productsStore.requestPrice.name }`,
        }
        
      });

      notificationsStore.pushToast({ id: 1, type: 'success', text: 'Запрос на стоимость товара успешно отправлен!' })
      productsStore.clearRequestPrice()

      // order.value = await response.value
      // productsStore.clearCartProducts()
      // clientStore.saveClientData(clientData)

    } else {
      errorMsg.value = 'Ошибка: Для отправки запроса заполните все поля.'
    }
  }

  const changeCity = () => {
    /// Сделать проверку на пустое поле
    clientStore.client.city = selectedCity.value
    clientStore.locationModal = false
    
    /// Пробуем найти подходящий магазин
    shopStore.shops.forEach((shop) => {
      if (shop.city.toLowerCase() === selectedCity.value.toLowerCase()) {
        clientStore.client.adress = shop
      }
    })
  }

  const searchCountries = computed(() => {
    if (searchTerm.value === '') {
      return []
    }

    let matches = 0

    return cities.filter(country => {
      if (
        country.toLowerCase().includes(searchTerm.value.toLowerCase())
        && matches < 10
      ) {
        matches++
        return country
      }
    })
  })

  const searchTerm = ref('')
  const selectedCity = ref(null)
  

</script>



<template>

  <div class="fixed z-40 w-full h-full bg-gray-500/50 backdrop-blur-sm">
    <div class="flex items-center justify-center h-full">
      <div class="h-full w-full flex items-center justify-center">
        

        <div class="container mx-auto px-4 lg:max-w-4xl lg:px-8">
          <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <div class="">

              <div class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-700">
                <h3 class="text-xl font-semibold text-gray-800 dark:text-white">
                  Выбрать город <span class="text-gray-700 dark:text-gray-300"> {{` - ` + selectedCity }}</span>
                </h3>
                <button @click="clientStore.locationModal = false" type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="defaultModal">
                  <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                  <span class="sr-only">Закрыть окно</span>
                </button>
              </div>


              <div class="px-4 py-8  min-h-[20rem]">


                <div class="">
                  <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-700 dark:text-gray-400">Найти город</label>
                  <div class="relative">
                    <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                      <p class="text-gray-700 dark:text-gray-400 mdi mdi-map-marker-radius"></p>
                    </div>
                    <input v-model="searchTerm" type="search" id="search-city" class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-600 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Москва">
                  </div> 
                </div>


                
                <div class="flex flex-wrap gap-2 py-2">
                  <button 
                    v-for="(city, pk) in ['Москва','Санкт-Петербург','Псков','Смоленск','Петрозаводск','Великие луки',]" :key="pk"
                    @click="selectedCity = city"
                    class="bg-white dark:bg-gray-800 rounded-xl border hover:border-gray-300 dark:border-gray-700 border-gray-200 hover:dark:border-gray-700 transition-all shadow-md">
                    <div class="flex items-center justify-center py-1 px-4">
                      <p  class="text-[10px] md:text-xs text-gray-700 dark:text-gray-300">{{ city }}</p>
                    </div>
                  </button>
                </div>


                <div class="py-2">
                  <div class="flex flex-wrap gap-2">
                    <transition-group name="fade" mode="out-in">
                      <button 
                        v-for="(city, pk) in searchCountries" :key="pk"
                        @click="selectedCity = city; searchTerm = city"
                        class="bg-white dark:bg-gray-800 rounded-full border hover:border-gray-300 dark:border-gray-700 border-gray-200 hover:dark:border-gray-700 transition-all shadow-md">
                        <div class="flex items-center justify-center py-1.5 px-6">
                          <p  class="text-[10px] md:text-xs text-gray-700 dark:text-gray-300">{{ city }}</p>
                        </div>
                      </button>
                    </transition-group>
                  </div>
                </div>




              </div>


              <div class="grid grid-cols-1 items-end justify-between p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-700">
                

                <div class="flex justify-center gap-2 w-full md:justify-end px-2">
                  

                  <button @click="changeCity">
                    <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                      <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                        <p class="px-5 py-2.5">Сменить город</p>
                      </div>
                    </div>
                  </button>
                                    
                  <button @click="clientStore.locationModal = false" data-modal-toggle="defaultModal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Закрыть окно</button>
                </div>
              </div>


            </div>


          </div>
        </div>


      </div>        
    </div>
  </div>
</template>