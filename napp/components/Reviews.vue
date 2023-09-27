<script setup>
  const props = defineProps(['reviews'])

  const myMethod = () => {
    // Логика метода
    console.log('Вызван метод');
  };


  const startAnimation = (image) => {
    image.show_image = image.image;
  }
  const stopAnimation = (image) => {
    image.show_image = image.static_image;
  }

</script>

<template>
  <div class="">

    <div class="container mx-auto px-4 py-2 max-w-6xl lg:px-8">
      <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md">
        <div class="px-2 mt-2">
          <div class="flex gap-2">
            <div class="flex items-center justify-center px-4 py-0.5 border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 bg-gray-100 dark:bg-gray-700 transition-all rounded-md shadow-sm shadow-black/30">
              <nuxt-link :to="{ name: 'reviews' }" class="text-sm text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-200">Обзоры</nuxt-link>
            </div>
            <div class="flex items-center justify-center px-4 py-0.5 border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 bg-gray-100 dark:bg-gray-700 transition-all rounded-md shadow-sm shadow-black/30">
              <p class="text-sm text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-200">Статьи</p>
            </div>
          </div>
        </div>

        <div class="px-2 py-2">

          <div class="grid grid-cols-2 md:grid-cols-4 gap-2">

            <div v-for="image in props.reviews.slice(0, 3)" :key="image.id"  class="">
              <div @mouseover="startAnimation(image)" @mouseout="stopAnimation(image)" class=" h-full cursor-pointer border border-gray-200 hover:border-gray-300 dark:border-gray-600 dark:hover:border-gray-500 bg-gray-100 dark:bg-gray-700 transition-all rounded-md shadow-sm shadow-black/30">
                <div class="rounded-md transition-all duration-700">
                  <nuxt-link :to="{ name: 'reviews-id', params: { id: image.id } }" class="">
                    <img :src="image.show_image" alt="Your WebP Image" class=" transition-all duration-700 rounded-md hh-36 rounded-bl-xl rounded-br-xl" />
                    <div class="px-1 py-4">
                      <p class="text-xs">{{ image.name }}</p>
                    </div>
                  </nuxt-link>
                </div>
              </div>
            </div>

            <div  class="">
              <div  class=" h-full cursor-pointer border border-gray-200 hover:border-gray-300 dark:border-gray-700 dark:hover:border-gray-500 bg-gray-100 dark:bg-gray-700 transition-all rounded-md shadow-sm shadow-black/30">
                <div class="rounded-md transition-all duration-700">
                  <nuxt-link :to="{ name: 'articles-id', params: { id: 1 } }" class="">
                    <img src="/prod-img/mig200_LZdS49o.webp" alt="Your WebP Image" class=" transition-all duration-700 rounded-md hh-36 rounded-bl-xl rounded-br-xl" />
                    <div class="px-1 py-4">
                      <p class="text-xs">Как выбрать сварочный аппарат</p>
                    </div>
                  </nuxt-link>                
                </div>
              </div>
            </div>

          </div>


        </div>

      </div>


    </div>

  </div>
</template>