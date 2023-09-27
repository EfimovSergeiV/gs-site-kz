<script setup lang="ts">
	const swiper = useSwiper()
</script>

<template>
  <div class="flex items-center justify-end bg-blue-700/60 hover:bg-blue-700/90 duration-500 transition-all rounded-lg border border-gray-300/10">
    <button @click="swiper.slideNext()" class="mdi mdi-arrow-left-bold text-gray-100 mdi-18px w-8 h-8"></button>
    <button @click="swiper.slidePrev()" class="mdi mdi-arrow-right-bold text-gray-100 mdi-18px w-8 h-8 duration-500 transition-all"></button>		
  </div>
</template>
