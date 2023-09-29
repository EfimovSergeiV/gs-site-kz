<script setup>
  const config = useRuntimeConfig()
  // const colorMode = useColorMode()
  // const route = useRoute()

  const { data: widebanner } = await useFetch(`${ config.public.baseURL }c/widebanners/`)
  const { data: banners } = await useFetch(`${ config.public.baseURL }c/mainbanner/`)
  const { data: brands } = await useFetch(`${ config.public.baseURL }c/brands/`)
  const { data: esab } = await useFetch(`${ config.public.baseURL }c/prods/?brnd=3`)
  const { data: latest } = await useFetch(`${ config.public.baseURL }c/neues/`)
  const { data: mpromobs } = await useFetch(`${ config.public.baseURL }c/mpromob/`)
  const { data: recommends } = await useFetch(`${ config.public.baseURL }c/recommend/`)
  const { data: randomreviews } = await useFetch(`${ config.public.baseURL }c/random-reviews/`)
  const descriptionData = 'С 2009 года Главный сварщик – ваш надежный партнер в мире сварочного оборудования! Наши магазины – это место, где профессионалы и энтузиасты приходят за лучшими решениями для сварочных работ. Сварка - это искусство, и мы знаем, как сделать его доступным и эффективным для каждого.'
  
  useSeoMeta({
    title: `Сеть магазинов Главный Сварщик`,
    description: `${ descriptionData.value }`,
    keywords: `Главный сварщик, сварочное оборудование, оборудование для сварки, купить электроды, купить проволоку, купить источник, купить сварочный инвертор`,
    ogLocale: 'ru_RU',
    ogTitle: `Сеть магазинов Главный Сварщик`,
    ogDescription: `${ descriptionData.value }`,
    ogImage: `https://api.glsvar.ru/files/og-image.png`,
    twitterCard: `https://api.glsvar.ru/files/og-image.png`,
  })

</script>

<template>

  <div class="">
    <AppHeader />
    <AppNavbar />
    <MainSection :latest="latest" :banners="banners" />
    <MainWelder />
    <Reviews :reviews="randomreviews" />
    <ESAB />
    <Recommend :recommends="recommends" />
    <ShopMaps />    
    <CorouselBrands />
    <AppFooter />
  </div>
</template>