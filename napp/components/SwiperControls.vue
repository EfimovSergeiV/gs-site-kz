<script setup lang="ts">
	const swiper = useSwiper()
</script>

<template>
  <div class="">
    <button @click="swiper.slidePrev()" class="mdi mdi-arrow-left-bold text-gray-600 dark:text-white mdi-24px w-8 h-8"></button>
    <button @click="swiper.slideNext()" class="mdi mdi-arrow-right-bold text-gray-600 dark:text-white mdi-24px w-8 h-8 duration-500 transition-all"></button>		
  </div>
</template>
