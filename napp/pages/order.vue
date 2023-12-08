<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()

  const { data: orderinfo, pending: pendingorder, error: errorder } = await useFetch(`${ config.public.baseURL }o/orderinfo/${ route.hash.slice(1,) }`)
// const sendRequest = async () => {
//     if ( (clientStore.client.city) && (clientStore.client.contact) ) {
//       const { data: response } = await useFetch(`${ config.public.baseURL }o/request-price/`, {
//         method: 'POST',
//         body: {
//           city: clientStore.client.city,
//           contact: clientStore.client.contact,
//           product: `id: ${ productsStore.requestPrice.id } vc: ${ productsStore.requestPrice.vcode } name: ${ productsStore.requestPrice.name }`,
//         }
        
//       });

//       notificationsStore.pushToast({ id: 1, type: 'success', text: 'Запрос на стоимость товара успешно отправлен!' })
//       productsStore.clearRequestPrice()

//       // order.value = await response.value
//       // productsStore.clearCartProducts() 
//       // clientStore.saveClientData(clientData)

//          o/orderinfo/PSK1156363/

//     } else {
//       errorMsg.value = 'Для отправки запроса заполните все поля.'
//     }
//   }
</script>


<template>

  <div class="">
    <!-- <AppHeader />
    <AppNavbar />


    <div class="container mx-auto px-4 py-2 max-w-6xl lg:px-8">
      
      <div class="bg-white dark:bg-gray-800 rounded-md border dark:border-gray-700 px-4 py-4 min-h-[65vh]">
        <div v-if="orderinfo">
          <div class=" py-6">
            <p class="my-2">Номер заказа: <span class="font-semibold ml-2">{{ orderinfo.order_number }}</span></p>
            <p class="my-2">Статус: <span class="font-semibold ml-2" v-if="orderinfo.status === 'notprocessed'">В обработке</span><span class=" ml-2" v-else>Обработан</span></p>
            <p class="my-2">Сумма по позициям: <span class="font-semibold ml-2">{{ orderinfo.position_total }}</span> тг</p>
            <p class="my-2" v-if="orderinfo.delivery_summ">Доставка: <span class="font-semibold ml-2">{{ orderinfo.delivery_summ }}</span></p>
            <p class="my-2">Итог заказа: <span class="font-semibold ml-2">{{ orderinfo.total }}</span> тг</p>            
          </div>

          
          <div class=" py-2">
            <p class="text-sm">Позиции заказа:</p>
            <div class="grid grid-cols-1 gap-2 py-4">

              <div v-for="product in orderinfo.client_product" :key="product.id" class="bg-white dark:bg-gray-700 px-2 py-2 border border-gray-200 dark:border-gray-700 rounded-md flex items-center gap-6">
                <img :src="product.preview_image" class="h-14 rounded-md bg-white px-2" />
                <p class="text-sm">{{ product.vcode }}</p>
                <nuxt-link :to="{ name: 'product-id', params: { id: product.product_id } }">{{ product.name }}</nuxt-link>
                <p>{{ product.price }} x {{ product.quantity }}</p>
              </div>
              
            </div>
          </div>

        </div>

        <div v-else>
          <p>Заказ не найден</p>
        </div>        
      </div>


    </div>
    
    <AppFooter /> -->


  </div>
</template>