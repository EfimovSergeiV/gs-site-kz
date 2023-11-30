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
      body: { "comp": id }
    })
  }


</script>


<template>
  <div class="">
    <AppHeader />
    <AppNavbar />

    <div class="container mx-auto max-w-6xl px-4 lg:px-8 py-2">


      <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md">
        <div class="p-4 min-h-screen">

          <p class="text-xs">{{ productsStore.like }}</p>

        </div>
      </div>
    </div>
    
    <AppFooter />
  
  </div>
</template>