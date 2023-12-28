<script setup>
  const config = useRuntimeConfig()
  // const colorMode = useColorMode()
  // const route = useRoute()


  const descriptionData = 'С 2009 года Главный сварщик – ваш надежный партнер в мире сварочного оборудования! Наши магазины – это место, где профессионалы и энтузиасты приходят за лучшими решениями для сварочных работ. Сварка - это искусство, и мы знаем, как сделать его доступным и эффективным для каждого.'
  useSeoMeta({
    title: `Интернет магазин Главный Сварщик`,
    description: `${ descriptionData }`,
    keywords: `Главный сварщик, сварочное оборудование, оборудование для сварки, купить электроды, купить проволоку, купить источник, купить сварочный инвертор`,
    ogLocale: 'ru_RU',
    ogTitle: `Интернет магазин Главный Сварщик`,
    ogDescription: `${ descriptionData }`,
    ogImage: `/og-image.png`,
    twitterCard: `/og-image.png`,
  })

</script>

<template>

  <div class="">

    <AppHeader />


    <div class="container mx-auto px-4 max-w-6xl lg:px-8 py-2">
      <div class="bg-gray-100 dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700 px-4 py-2 relative">

        <div class="flex items-center justify-center min-h-[40vh]">

          <div class="flex items-center gap-14">
            
            <p class=" text-9xl">404!</p>            
            
            <div class="">
              <p class="text-xl uppercase">Страницы больше не существует</p>
              <nuxt-link :to="{ name : 'index'}">перейти на главную</nuxt-link>
            </div>

          </div>
        
        </div>



      </div>
    </div>
    
    

    <AppFooter />
  </div>
</template>