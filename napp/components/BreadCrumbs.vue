<script setup>
  const props = defineProps(['breadcrumbs'])

</script>


<template>
  <div class="mx-auto px-4 max-w-6xl lg:px-8 my-2">
    <nav class="flex px-5 py-3 text-gray-700 border border-gray-200 rounded-md bg-white dark:bg-gray-800 dark:border-gray-700" aria-label="Breadcrumb">
      <ol class="inline-flex items-center space-x-1 md:space-x-3">
        <li class="hidden md:inline-flex items-center">
          <nuxt-link :to="{ name: 'index' }" class="inline-flex items-center text-xs text-center font-medium text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100">
            <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>
            Главная
          </nuxt-link>
        </li>
        <li class="">
          <div class="flex items-center">
            <svg class=" hidden md:block w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
            <nuxt-link :to="{ name: 'cts' }" class="ml-1  text-xs text-center font-medium text-gray-700 hover:text-gray-900 md:ml-2 dark:text-gray-300 dark:hover:text-gray-100">Каталог</nuxt-link>
          </div>
        </li>
        
        <li v-for="path in props.breadcrumbs" :key="path.id">
          <div class="flex items-center">
            <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
              <nuxt-link :to="{ name: 'prods', query: { ct: path.id, page: 1 }}" class="ml-1 text-xs text-center font-medium text-gray-700 hover:text-gray-900 md:ml-2 dark:text-gray-300 dark:hover:text-gray-100">{{ path.name }}</nuxt-link>
          </div>
        </li>
      </ol>
    </nav>
  </div>
</template>