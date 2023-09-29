<script setup>
  const { signIn, token, data, status, lastRefreshedAt } = useAuth()

  const productsStore = useProductsStore()

</script>

<template>
  <div class="">
    <AppHeader />
    <AppNavbar />

    <div class="container mx-auto max-w-6xl px-4 py-2 lg:px-8">
      <div class="bg-white dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700">
        <div v-if="productsStore.like.length > 0" class=" min-h-[50vh]">
          <div class="px-4 py-2">
            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 gap-4">
              <div v-for="product in productsStore.like" :key="product.id">
                <ProductCard :product="product" />
              </div>
            </div>
          </div>
        </div>

        <div v-else class="flex items-center justify-center min-h-[50vh]">
          <p class="text-base">Нет товаров в избранном</p>
        </div>        
      </div>
    </div>

    <AppFooter />

  </div>
</template>