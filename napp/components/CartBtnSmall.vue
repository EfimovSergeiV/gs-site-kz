<script setup>
  const props = defineProps(['product'])
  const productsStore = useProductsStore()
  const notificationsStore = useNotificationsStore()

</script>


<template>
  <div class="">
      
    <button @click="productsStore.addProduct('cart', props.product)" class="">
      <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
        <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
          
          <transition name="fade" mode="out-in">
            <div v-if="productsStore.productInCart(props.product.id)">
              <p class="text-white text-sm w-36 md:w-24 py-1.5">В корзине</p>
            </div>
            <div v-else>
              <p class="text-white text-sm w-36 md:w-24 py-1.5">Купить</p>
            </div>
          </transition>

        </div>
      </div>
    </button>

  </div>
</template>