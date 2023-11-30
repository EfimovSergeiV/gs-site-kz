<script setup>
  const config = useRuntimeConfig()
  const tmp_id = useCookie('tmp_id')
  const productsStore = useProductsStore()
  const notificationsStore = useNotificationsStore()

  const delLikeProd = (id) => {
    console.log('ID ', id)
    $fetch(`${ config.public.baseURL }u/uwatch/`, {
      method: 'DELETE',
      headers: { "Authorization": tmp_id.value, },
      body: { "like": id }
    })
  }


</script>


<template>
  <div class="">
    <AppHeader />
    <AppNavbar />

    <div class="container mx-auto max-w-6xl px-4 lg:px-8 py-2">

      <div v-if="productsStore.like.length > 0" class="">
        <div class="grid grid-cols-1 gap-y-4 gap-x-4 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4">
          <transition-group name="fade">
            <div class="" v-for="product in productsStore.like" :key="product.id">
              <ProductCard :product="product" />
            </div>            
          </transition-group>
        </div>
      </div>

      <div v-else class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md">
        <div class="flex items-center justify-center min-h-[50vh]">

          <p class="">Нет товаров в избранном</p>

        </div>
      </div>
    </div>
    
    <AppFooter />
  
  </div>
</template>