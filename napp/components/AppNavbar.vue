<script setup>
  import debounce from "lodash.debounce";


  const config = useRuntimeConfig()
  const { signIn, signOut, token, data, status, lastRefreshedAt } = useAuth()
  // const { data: products } = await useFetch(`${ config.public.baseURL }c/neues/`) /// for debug styles

  const search = ref('')
  const products = ref([])


  const debouncedHandler = debounce(async query => {

    const { data: prods }  = await useFetch(`${ config.public.baseURL }c/search/`, {
      method: 'POST',
      body: {
        name: search
      }
    })
    
    products.value = ( await prods.value )    

  }, 300);


  watch(search, (searchRequest) => {
    debouncedHandler()
  })


</script>


<template>
  <div class="">
    <div class="container mx-auto py-0.5 px-4 max-w-6xl lg:px-8">





      <!-- <div class="">
        <input 
          v-model="search" 
          type='search'
          id="phone"
          placeholder="Поиск по каталогу"
          class="bg-gray-50 border border-gray-300 text-gray-700 font-semibold dark:text-gray-700 text-sm 
          uppercase rounded-lg focus:ring-gray-300/0 focus:border-gray-300 block 
          w-full pl-12 p-2 dark:bg-white dark:border-gray-700 dark:placeholder-gray-500
          ring-0 dark:focus:ring-gray-600/0 dark:focus:border-gray-700" >
      </div> -->

    </div>
  </div>
</template>