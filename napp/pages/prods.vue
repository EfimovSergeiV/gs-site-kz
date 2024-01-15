<script setup>
  const config = useRuntimeConfig()
  const productsStore = useProductsStore()
  const clientStore = useClientStore()
  const notificationsStore = useNotificationsStore()
  const route = useRoute()
  const router = useRouter()

  const { data: brands } = await useFetch(`${ config.public.baseURL }c/ctbrand/`, { params: route.query })
  const { data: props } = await useFetch(`${ config.public.baseURL }c/props/`, { params: route.query })
  const { data: products } = await useFetch(`${ config.public.baseURL }c/prods/`, { params: route.query })
  const { data: breadcrumbs } = await useFetch(`${ config.public.baseURL }c/breadcrumb/`, { params: route.query })

  useSeoMeta({
    title: `${ products.value.meta.title }`,
    description: `${ products.value.meta.title }, большой выбор, купить по низким ценам. Гарантия качества.`,
    keywords: `${ products.value.meta.title }, сварочное оборудование, оборудование для сварки, купить электроды, купить проволоку, купить источник, купить сварочный инвертор`,
    ogLocale: 'ru_RU',
    ogTitle: `${ products.value.meta.title }`,
    ogDescription: `${ products.value.meta.title }, большой выбор, купить по низким ценам. Гарантия качества.`,
    ogImage: `/og-image.png`,
    twitterCard: `/og-image.png`,
  })

  /// Корзина кнопки, лайки, сравнение

  const scrollToTop = () => {
    window.scrollTo({ top: 0 })
  }

  watch(() => route.fullPath, async (fullPath) => {
      const { data: brands_updated }  = await useFetch(`${ config.public.baseURL }c/ctbrand/`, { params: route.query })
      const { data: prods_updated }  = await useFetch(`${ config.public.baseURL }c/prods/`, { params: route.query })
      const { data: props_updated }  = await useFetch(`${ config.public.baseURL }c/props/`, { params: route.query })
      const { data: breadcrumbs_updated } = await useFetch(`${ config.public.baseURL }c/breadcrumb/`, { params: route.query })
      
      brands.value = ( await brands_updated.value )
      products.value = ( await prods_updated.value )
      props.value = ( await props_updated.value)
      breadcrumbs.value = ( await breadcrumbs_updated.value )
      
      scrollToTop()
    }
  )

  // const page_id = ref(1)

  // const { data: products, pending, error } = await useAsyncData(() => {
  //   return $fetch(`${ config.public.baseURL }c/prods/`, { params: { ct: ct_id.value, page: page_id.value } })
  // // return $fetch(`${ config.public.baseURL }c/prods/`, { params: route.query })
  // }, {
  //   watch: [ct_id, page_id ]
  // })

</script>



<template>
  <div>

    <AppHeader />
    <BreadCrumbs id="breadcrumbs" :breadcrumbs="breadcrumbs" />

    <div class="mx-auto px-4 max-w-6xl lg:px-8">

      <div class="flex items-center justify-between">

        <div class="hidden md:block">
          <div class="flex gap-1">
            <button @click="clientStore.viewport = 'grid'" class="mdi mdi-24px mdi-view-grid text-gray-600 dark:text-gray-300"></button>            
            <button @click="clientStore.viewport = 'row'" class="mdi mdi-24px mdi-view-agenda text-gray-600 dark:text-gray-300"></button>
          </div>
        </div>

        <div v-if="products.meta.inserted" class="flex items-center justify-end">
          <div id="" class="">
            <div class="flex flex-wrap gap-2 justify-end">
              <div v-for="inserted in products.meta.inserted" :key="inserted.id" class="">
                <div class="bg-white dark:bg-gray-800 rounded-xl border hover:border-gray-300 dark:border-gray-700 border-gray-200 hover:dark:border-gray-700 transition-all shadow-md">
                  
                  <div class="flex items-center justify-center py-1 px-4">
                    <nuxt-link :to="{ name: 'prods', query: { ct: inserted.id}}" class="text-[10px] md:text-xs">{{ inserted.name }}</nuxt-link>
                  </div>
                
                </div>
              </div>          
            </div>
          </div>
        </div>

      </div>
    </div>


    <div class="mx-auto px-4 my-2 max-w-6xl lg:px-8">
      <div class="grid grid-cols-1 md:flex items-center justify-between">

        <div class="flex items-center gap-1 justify-between md:justify-end my-2">
          <button class="w-full px-4 h-8 text-sm flex items-center justify-center text-gray-500 bg-white rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white" @click="notificationsStore.statusFilterComponent">Фильтр</button>
          <nuxt-link :to="{ name: 'prods', query: { page: 1, ...route.query, by: 'Date' } }" class="w-full px-3 md:px-4 h-8 text-xs md:text-sm flex items-center justify-center text-gray-500 bg-white rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Новые</nuxt-link>
          <nuxt-link :to="{ name: 'prods', query: { page: 1, ...route.query, by: 'Rating' } }" class="w-full px-3 md:px-4 h-8 text-xs md:text-sm flex items-center justify-center text-gray-500 bg-white rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Рейтинг</nuxt-link>
          <nuxt-link :to="{ name: 'prods', query: { page: 1, ...route.query, by: 'LowPrice' } }" class="w-full px-3 md:px-4 h-8 text-xs md:text-sm flex items-center justify-center text-gray-500 bg-white rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Дешевле</nuxt-link>
          <nuxt-link :to="{ name: 'prods', query: { page: 1, ...route.query, by: 'HighPrice' } }" class="w-full px-3 md:px-4 h-8 text-xs md:text-sm flex items-center justify-center text-gray-500 bg-white rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Дороже</nuxt-link>
        </div>

        <Pagination :count="products.count" />

      </div>

    </div>


    <transition name="filter">
      <div v-if="notificationsStore.filterComponent" class="fixed z-40 top-0 left-0">
        <Filters :brands="brands" :props="props" />
      </div>
    </transition>

   
    <div class="">
      <div class="container mx-auto px-4 max-w-6xl lg:px-8">

        <div v-if="products.results.length > 0" id="products" class="">

          <transition name="fade" mode="out-in">
            <div v-if="clientStore.viewport === 'grid'" class="grid grid-cols-1 gap-y-4 gap-x-4 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4">
              <transition-group name="fade">
                  <div class="" v-for="product in products.results" :key="product.id">
                    <ProductCard :product="product" />
                  </div>                
              </transition-group>
            </div>

            <div v-else class="grid grid-cols-1 gap-4">
              <transition-group name="fade">
                  <div class="" v-for="product in products.results" :key="product.id">
                    <ProductCardLS :product="product" />
                  </div>                
              </transition-group>
            </div>            
          </transition>


        </div>
        <div class="" v-else>

          <div class="bg-white dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700">
            <div class="flex items-center justify-center min-h-[50vh]">
              <p class="text-xl"> Ничего не найдено</p>
            </div>
          </div>
          
        </div>

      </div>
    </div>



    <div class="mx-auto px-4 my-2 max-w-6xl lg:px-8">
      <div v-if="products.count > 0" class="flex items-center justify-end">
        <Pagination :count="products.count" />
      </div>
    </div>

    <AppFooter />

  </div>
</template>