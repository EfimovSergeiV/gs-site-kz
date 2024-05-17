<script setup>
  const ctx = useNuxtApp()
  const config = useRuntimeConfig()
  const router = useRouter()

  const productsStore = useProductsStore()
  const clientStore = useClientStore()  
  const notificationsStore = useNotificationsStore()



  const fields = [
      { keyword:"legaladress", placeholder:"Россия, Москва, 117312, ул. Вавилова, д. 123", title:"Юридический адрес"},
      { keyword:"company", placeholder:"ООО Полное название компании", title:"Полное наименование"},
      { keyword:"inn", placeholder:"3664069397", title:"ИНН" },
      { keyword:"kpp", placeholder:"12356789", title:"КПП" },
      { keyword:"okpo", placeholder:"12345678", title:"ОКПО (необязательно)" },
      { keyword:"bankname", placeholder:"ПАО Сбербанк", title:"Наименование банка" },
      { keyword:"currentacc", placeholder:"12312123112341234567", title:"Расчетный счет (необязательно)" },
      { keyword:"corresponding", placeholder:"12312123112341234567", title:"Корреспондентский счет (необязательно)" },
      { keyword:"bic", placeholder:"123456789", title:"БИК (необязательно)" },
  ]

  const phoneValidate = computed(() => {
    const re = /^(?:\+7|7|8)[-\s]?\d{3}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$/
    if (clientStore.client.phone) {
      return clientStore.client.phone.search(re) !== -1
    } else {
      return false
    }
  })
  
  const emailValidate = computed(() => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    if (clientStore.client.email) {
      return clientStore.client.email.search(re) !== -1
    } else {
      return false
    }
  })

  const order = ref(null)
  const errorMsg = ref(null)

  const sendOrder = async () => {
    if ( (phoneValidate.value || emailValidate.value) ) {
      const { data: response } = await useFetch(`${ config.public.baseURL }o/order/`, {
        method: 'POST',
        body: {
          shop_id: clientStore.client.id,
          region_code: 'KZ',
          person: clientStore.client.person,
          phone: clientStore.client.phone,
          email: clientStore.client.email,
          comment: clientStore.client.comment,
          delivery: clientStore.client.delivery,    
          adress: 'ул. Топоркова 35, Рудный',   //clientStore.client.adress.adress,

          entity: clientStore.client.entity,
          company: clientStore.client.company,
          legaladress: clientStore.client.legaladress,
          inn: clientStore.client.inn,
          kpp: clientStore.client.kpp,
          okpo: clientStore.client.okpo,
          bankname: clientStore.client.bankname,
          currentacc: clientStore.client.currentacc,
          corresponding: clientStore.client.corresponding,
          bic: clientStore.client.bic,

          client_product: productsStore.cart,
        }
        
      });


      if ( productsStore.cartTotalPrice > 38000 ) {
        clientStore.order = response.value.order
        ctx.$metrika.reachGoal('EXPENSIVE_ORDER')

      } else {
        await router.push({ name: 'order', hash: `#${ response.value.order }` })
      }
      
      productsStore.clearCartProducts()

    } else {
      errorMsg.value = 'Ошибка: Укажите как с вами связаться.'
      notificationsStore.pushToast({ id: 1, type: 'error', text: 'Ошибка: Проверте правильно ли заполнены обязательные поля.' })
    }
  }


</script>



<template>
  <div class="container mx-auto px-4 py-2 max-w-6xl lg:px-8">

    <div id="cart-set" class="">


      <div v-if="(productsStore.cart.length > 0)" class="bg-white border-gray-200 border dark:border-gray-700 dark:bg-gray-800 rounded-md p-1">

        <div class="overflow-x-auto w-full">
          <div class="">

            <div class="grid gap-2 px-2 py-4">
              <div class="flex lg:items-center lg:gap-2">
                <div class="flex justify-center w-24"><p class="text-sm">Изображение</p></div>
                <div class="flex justify-center w-1/2"><p class="text-sm">Наименование</p></div>
                <div class="flex justify-center w-32"><p class="text-sm">Количество</p></div>
                <div class="flex justify-center w-32"><p class="text-sm">Наличие</p></div>
                <div class="flex justify-center w-32"><p class="text-sm">Стоимость</p></div>
                <div class="flex justify-center w-20"><p class="text-sm">Удалить</p></div>
              </div>
            </div>

            <div class="grid gap-2 px-1">
              <transition-group tag="div" name="left-emergence">
                <div v-for="product in productsStore.cart" :key="product.id" class="my-4">
                  <div class="flex items-center gap-2">
                    <div class="flex justify-center items-center w-24 bg-white rounded-md">
                      <img :src="product.preview_image" class="rounded-md w-20" />
                    </div>
                    <div class="flex justify-center w-1/2">
                      <p class="text-sm">{{ product.name }}</p>
                    </div>
                    <div class="flex justify-center w-32">
                      <button  @click="productsStore.changeQuantity(product, 'del')" class="mdi mdi-minus cursor-pointer"></button>
                      <div class="mx-2"><p>{{ product.quantity }}</p></div>
                      <button @click="productsStore.changeQuantity(product, 'add')" class="mdi mdi-plus cursor-pointer"></button>
                    </div>
                    <div class="flex justify-center w-32">
                      <p v-if="product.status === 'order'" class="text-sm text-right font-medium text-gray-900 dark:text-gray-200">под заказ</p>
                      <p v-else class="text-sm text-right font-medium text-gray-900 dark:text-gray-200">в наличии</p>
                      
                    </div>
                    <div class="flex justify-center w-32"><p class="text-sm">{{ product.price.toLocaleString() }} тг</p></div>
                    <div class="flex justify-center w-20">
                      <button @click="productsStore.addProduct('cart', product)" class="mdi mdi-24px mdi-close cursor-pointer"></button>
                    </div>
                    
                  </div>
                  
                </div>
              </transition-group>
            </div>
          </div>         
        </div>

        <div class="py-2 px-2">
          <p class="">Итог: <span class="font-semibold pl-2">{{ productsStore.cartTotalPrice.toLocaleString() }}</span> <span>тг</span></p>
        </div>

      </div>

      <div v-else class="flex justify-center bg-white border-gray-200 border dark:border-gray-700 dark:bg-gray-800 rounded-md">
        <div class="py-8 hidden">
          <div class="flex items-center gap-8">
            <div class="grid gap-2 grid-cols-1">
              <div class="mx-4 text-center">
                <p class="text-xl">Ваша корзина пуста</p>
              </div>
              <div class="border-b border-gray-700 dark:border-gray-300"></div>
              <div class="mx-4 text-center">
                <nuxt-link :to="{ name: 'cts' }" class="text-sm hover:underline hover:text-gray-900 dark:hover:text-gray-100 ">Перейти в каталог</nuxt-link>
              </div>
            </div>
            <div>
              <p class="mdi mdi-close-outline mdi-36px"></p>
            </div>          
          </div>          
        </div>
        <div class="flex items-center justify-center min-h-[50vh]">
              <p class="text-xl"> Ваша корзина пуста</p>
            </div>
      </div>


    </div>


    <div id="client-info" class="">
      <div class="mt-4">
        <div class="bg-white border-gray-200 border dark:border-gray-700 dark:bg-gray-800 p-4 rounded-md">

          <div class="flex items-center justify-between">
            <div class="">
              1. Данные покупателя
            </div>
            <div class="flex justify-end gap-4">

              <ul class="grid gap-6 w-full md:grid-cols-2">
                <li>
                  <input type="radio" id="hosting-small" name="person" v-model="clientStore.client.entity" :value="false" class="hidden peer" required>
                  <label for="hosting-small" class="text-gray-700 dark:text-gray-300 peer-checked:text-gray-900 dark:peer-checked:text-gray-100 peer-checked:border-b-2 border-blue-500 select-none text-sm cursor-pointer inline-flex justify-between items-center px-2 py-1 w-full transition-all ease-in duration-75">                           
                    <div class="block">
                      <div class="w-full">Физическое лицо</div>
                    </div>
                  </label>
                </li>
                <li>
                  <input type="radio" id="hosting-big" name="person" v-model="clientStore.client.entity" :value="true" class="hidden peer">
                  <label for="hosting-big" class="text-gray-700 dark:text-gray-300 peer-checked:text-gray-900 dark:peer-checked:text-gray-100 peer-checked:border-b-2 border-blue-500 select-none text-sm cursor-pointer inline-flex justify-between items-center px-2 py-1 w-full transition-all ease-in duration-75">
                    <div class="block">
                      <div class="w-full">Юридическое лицо</div>
                    </div>
                  </label>
                </li>
              </ul>
            </div>
          </div>


          <div class="grid md:grid-cols-2 gap-4">

            <div class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">Имя (необязательно)</label>
              <div class="relative">
                <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <p class="mdi mdi-account"></p>
                </div>
                <input v-model="clientStore.client.person" type="text" id="person" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Иван Иванов">
              </div>
            </div>
            <div class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">Электронная почта (необязательно)</label>
              <div class="relative">
                <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <p class="mdi mdi-email"></p>
                </div>
                <input v-model="clientStore.client.email" type="text" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@domen.com">
              </div>
            </div>
            <div class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">Номер телефона</label>
              <div class="relative">
                <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <p class="mdi mdi-phone"></p>
                </div>
                <input v-model="clientStore.client.phone" type="text" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="+7 (987) 654 32 10">
              </div> 
            </div>

          </div>


        </div>
      </div>

      <div v-if="clientStore.client.entity" class="mt-4">
        <div class="bg-white border-gray-200 border dark:border-gray-700 dark:bg-gray-800 p-4 rounded-md transition-all duration-300">
          <p class="">Дополнительные поля для юр.лиц:</p>
          
          <div class="grid md:grid-cols-3 gap-4">
            <div v-for="(field, pk) in fields" :key="pk" class="">
              <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">{{ field.title }}</label>
              <div class="relative">
                <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <p class="mdi mdi-phone"></p>
                </div>
                <input v-model="clientStore.client[field.keyword]" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" :placeholder="field.placeholder">
              </div> 
            </div>
          </div>

        </div>
      </div>

    </div>


    <div id="selected-shop" class="">

      <div class="mt-4">
        <div class="bg-white border-gray-200 border dark:border-gray-700 dark:bg-gray-800 p-4 rounded-md">

          <div class="flex items-center justify-between">
            <div class="">
              2. Способ получения
            </div>
            <div class="flex justify-end gap-4">
              <ul class="flex justify-end items-center gap-4 w-full md:grid-cols-2">
                <li>
                  <input type="radio" id="pickup" name="delivery" v-model="clientStore.client.delivery" :value="false" class="hidden peer" required>
                  <label for="pickup" class="text-gray-700 dark:text-gray-300 peer-checked:text-gray-900 dark:peer-checked:text-gray-100 peer-checked:border-b-2 border-blue-500 select-none text-sm cursor-pointer inline-flex justify-between items-center px-2 py-1 w-full transition-all ease-in duration-75">                           
                    <div class="block">
                      <div class="w-full">Самовывоз из магазина</div>
                    </div>
                  </label>
                </li>
                <li>
                  <input disabled type="radio" id="delivery" name="delivery" v-model="clientStore.client.delivery" :value="true" class="hidden peer">
                  <label for="delivery" class="text-gray-700 dark:text-gray-300 peer-checked:text-gray-900 dark:peer-checked:text-gray-100 peer-checked:border-b-2 border-blue-500 select-none text-sm cursor-not-allowed inline-flex justify-between items-center px-2 py-1 w-full transition-all ease-in duration-75">
                    <div class="block">
                      <div class="w-full">Доставка ТК</div>
                    </div>
                  </label>
                </li>
              </ul>
            </div>

          </div>


          <div class="border dark:border-gray-700 rounded-md bg-gray-50 dark:bg-gray-700">
            <div class="">
              <div class="grid lg:grid-cols-2 justify-items-stretch items-center ">

                <div class="justify-self-center mx-2 my-2" v-if="clientStore.client.adress">
                  <div class="" v-if="clientStore.client.adress.phone">
                    <div class="flex items-center">
                      <div class="border-r">
                        <a class="text-base md:text-2xl mx-2" :href="'tel:' + clientStore.client.adress.phone.replace(/[^+\d]/g, '')">{{ clientStore.client.adress.phone }}</a>
                      </div>
                      <div class="mx-2">
                        <p class="text-xs font-bold mt-1">{{ clientStore.client.adress.wday }}</p>
                        <p class="text-xs font-bold">{{ clientStore.client.adress.wend }}</p>   
                      </div>
                    </div>
                  </div>
                </div>
              </div>

            </div>
            <div class="">
              <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d9607.746256144887!2d63.1143089!3d52.9855424!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x43cd03eb0088f70d%3A0xfaaebd2d312ed8f7!2z0JPQu9Cw0LLQvdGL0Lkg0KHQstCw0YDRidC40Lo!5e0!3m2!1sru!2sru!4v1695649108350!5m2!1sru!2sru" width="100%" height="300" frameborder="0" loading="lazy" class="rounded-md"></iframe>
            </div>
          </div>

          <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-900 dark:text-gray-400">Комментарий к заказу (необязательно)</label>
          <textarea v-model="clientStore.client.comment" id="message" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-md border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Напишите что-нибудь..."></textarea>

          <div class="flex justify-end items-center my-2">
            <p class="text-xs text-red-600 dark:text-red-500">{{ errorMsg }}</p>
          </div>

          <div class="flex justify-end items-center my-4">
            <button @click="sendOrder" class="">
              <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                  <p class="text-white text-base w-52 py-1.5">Сделать заказ</p>
                </div>
              </div>
            </button>              
          </div>

        </div>
      </div>

    </div>


  </div>
</template>