<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps({
  error: Object as () => NuxtError
})
</script>

<template>

  <div class="">

    <NuxtLayout>
      <AppHeader />


        <div class="container mx-auto px-4 max-w-6xl lg:px-8 py-2">
          <div class="bg-gray-100 dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700 px-4 py-2 relative">

            <div class="flex items-center justify-center min-h-[40vh]">
              
              <!-- <h1>{{ error }}</h1> -->
              
              <div v-if="error?.statusCode === 404" class="grid grid-cols-1 md:flex items-center gap-14">
                <p class="text-center text-9xl">404!</p>            
                
                <div class="grid grid-cols-1 gap-4">
                  <p class="text-xl uppercase">Страницы больше не существует</p>
                  <nuxt-link :to="{ name : 'index'}">перейти на главную</nuxt-link>
                </div>
              </div>
              <div v-else class="grid grid-cols-1 justify-center items-center gap-6">
                <div class="grid grid-cols-1 justify-center items-center gap-2">
                  <p class="text-center text-6xl">Ошибка {{ error?.statusCode }}</p>
                  <p class="text-xl text-center uppercase">Страница не найдена</p>                  
                </div>

                <nuxt-link :to="{ name : 'index'}" class="text-center text-lg">перейти на главную</nuxt-link>
              </div>
            
            </div>

          </div>
        </div>

        <AppFooter />
    </NuxtLayout>
  </div>
</template>