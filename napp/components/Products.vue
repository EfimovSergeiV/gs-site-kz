<script setup>
  const props = defineProps(['products'])

</script>


<template>
  
  <div class="min-h-screen">
    <div class="container mx-auto py-2 px-4 max-w-6xl lg:px-8">

      <div class="">
        <div class="grid grid-cols-1 gap-y-4 gap-x-4 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4">
          <div class="" v-for="product in props.products.results" :key="product.id">

            <ProductCard :product="product" />

          </div>
        </div>
      </div>

    </div>
  </div>

</template>