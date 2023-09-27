<script setup>
  const props = defineProps(['product'])
  const productsStore = useProductsStore()
  const notificationsStore = useNotificationsStore()

</script>


<template>
  <div class="">
    <div class="w-5 h-5 flex items-center justify-center border-2 border-blue-600 rounded-md cursor-pointer">
      <div v-if="productsStore.productInComp(props.product.id)" class="">
        <button @click="productsStore.addProduct('comp', props.product); notificationsStore.pushToast({id: props.product.id, type: 'success', text: 'Товар удалён из сравнения'})" class="mdi mdi-check-bold text-gray-700 dark:text-gray-300"></button>
      </div>
      <div v-else class="">
        <button @click="productsStore.addProduct('comp', props.product); notificationsStore.pushToast({id: props.product.id, type: 'success', text:' Товар добавлен к сравнению'})" class="w-5 h-5"></button>
      </div>
    </div>
  </div>
</template>