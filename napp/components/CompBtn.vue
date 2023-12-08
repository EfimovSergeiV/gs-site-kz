<script setup>
  const config = useRuntimeConfig()
  const tmp_id = useCookie('tmp_id')
  const props = defineProps(['product'])
  const productsStore = useProductsStore()
  const notificationsStore = useNotificationsStore()

  const addCompProd = (id) => {
    $fetch(`${ config.public.baseURL }u/uwatch/`, {
      method: 'POST',
      headers: { "Authorization": tmp_id.value, },
      body: { "comp": id }
    })
  }

  const delCompProd = (id) => {
    console.log('ID ', id)
    $fetch(`${ config.public.baseURL }u/uwatch/`, {
      method: 'DELETE',
      headers: { "Authorization": tmp_id.value, },
      body: { "comp": id }
    })
  }

</script>


<template>
  <div class="">
    <div class="w-5 h-5 flex items-center justify-center border-2 border-blue-600 rounded-md cursor-pointer">
      <div v-if="productsStore.productInComp(props.product.id)" class="">
        <button @click="productsStore.addProduct('comp', props.product); notificationsStore.pushToast({id: props.product.id, type: 'success', text: 'Товар удалён из сравнения'}); delCompProd(props.product.id)" class="mdi mdi-check-bold text-gray-700 dark:text-gray-300"></button>
      </div>
      <div v-else class="">
        <button @click="productsStore.addProduct('comp', props.product); notificationsStore.pushToast({id: props.product.id, type: 'success', text:' Товар добавлен к сравнению'}); addCompProd(props.product.id)" class="w-5 h-5"></button>
      </div>
    </div>
  </div>
</template>