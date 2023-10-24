<script setup>
  const config = useRuntimeConfig()
  const shopStore = useShopStore()
  const clientStore = useClientStore()
  const { data: shops } = await useFetch(`${ config.public.baseURL }c/shops/`)
  const images = [
    { "id": 1, "url": "/shops/1.webp"},
    { "id": 2, "url": "/shops/2.webp"},
    { "id": 3, "url": "/shops/3.webp"},
    { "id": 4, "url": "/shops/4.webp"},
    { "id": 5, "url": "/shops/5.webp"},
    { "id": 6, "url": "/shops/6.webp"},
  ]

  const mapURLs = {
    "Псков" : "https://yandex.ru/map-widget/v1/?um=constructor%3A47f57d246b40670e64b17cb3f82dde8a81f3b3a825fa0ec9dc5e2a360214ec38&amp;source=constructor",
    "Москва" : "https://yandex.ru/map-widget/v1/?um=constructor%3Ae113235413b59c4ae31cb4d894caa9612e5c88e95cb5fc873f8508770800a19f&amp;source=constructor",
    "Санкт-Петербург" : "https://yandex.ru/map-widget/v1/?um=constructor%3A4892b9a6ff89034d14a4833ed892e30ddac4cde58559e85c6ae75d9d5cb766b2&amp;source=constructor",
    "Великие луки" : "https://yandex.ru/map-widget/v1/?um=constructor%3A8cbd01689857fcf3e2c9604637d5e0e3ac33b5e71467a701ed470d12b63e1dea&amp;source=constructor",
    "Смоленск" : "https://yandex.ru/map-widget/v1/?um=constructor%3A22e3d619383ca4fb59e78352a52f5e3808418009918e23d73549578277b6a013&amp;source=constructor",
    "Петрозаводск" : "https://yandex.ru/map-widget/v1/?um=constructor%3A7a6886838355b4c4aab4597dd2ee3dcd40eb7c6cd2bab5638666af5f1606c267&amp;source=constructor",
  }

  const descriptionData = 'С 2009 года Главный сварщик – ваш надежный партнер в мире сварочного оборудования! '

  useSeoMeta({
    title: `Интернет магазин Главный Сварщик - О нас - Адреса магазинов`,
    description: `${ descriptionData.value }`,
    keywords: `Главный сварщик, сварочное оборудование, оборудование для сварки, купить электроды, купить проволоку, купить источник, купить сварочный инвертор`,
    ogLocale: 'ru_RU',
    ogTitle: `Интернет магазин Главный Сварщик`,
    ogDescription: `${ descriptionData.value }`,
    ogImage: `https://api.glsvar.ru/files/og-image.png`,
    twitterCard: `https://api.glsvar.ru/files/og-image.png`,
  })

</script>

<template>
  <div class="">
    <AppHeader />
    <AppNavbar />

    <div class="container mx-auto px-4 max-w-6xl lg:px-8 min-h-[40rem]">

      <div class="bg-white dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700 mt-2 mb-4">
        <div class="">
          <img src="/bnr/banner_image-1.webp" class=" rounded-t-md" />
        </div>

        <div class="px-4 py-4">
          <div class="">
            <blockquote class="text-2xl font-semibold italic text-center text-gray-700 dark:text-gray-300">
              
              <span class="px-4">ЕСЛИ НУЖНО</span>
              <span class="before:block before:absolute before:-inset-2 before:-skew-y-3 before:bg-blue-600 relative inline-block my-2 lg:my-0">
                <span class="relative text-white"> СВАРОЧНОЕ ОБОРУДОВАНИЕ </span>
              </span>
              <span class="px-4">,ЗАКАЗЫВАЙТЕ ОНЛАЙН </span>
              <p class="mt-1">НА GLSVAR.KZ!</p>
              
            </blockquote>


            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 py-4">
              <div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-700 px-1 py-1 rounded-md border border-white/20 shadow-md shadow-black/50">
                <img src="/bnr/arbeitsschutz-schweissen.webp" class=" rounded-full w-24 border border-white/20"/>
                <nuxt-link :to="{ name: 'prods', query: { ct: 77 }}" class="">
                  <p class="">Средства защиты головы, рук и лица</p>
                </nuxt-link>
              </div>
              <div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-700 px-1 py-1 rounded-md border border-white/20 shadow-md shadow-black/50">
                <img src="/bnr/autogentechnik.webp" class=" rounded-full w-24 border border-white/20"/>
                <nuxt-link :to="{ name: 'prods', query: { ct: 3 }}" class="">
                  <p class="">Принадлежности для газокислородной сварки</p>
                </nuxt-link>
              </div>
              <div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-700 px-1 py-1 rounded-md border border-white/20 shadow-md shadow-black/50">
                <img src="/bnr/Kreise-SH-hell4.webp" class=" rounded-full w-24 border border-white/20"/>
                <nuxt-link :to="{ name: 'prods', query: { ct: 1 }}" class="">
                  <p class="">Современные сварочные аппараты на дуговой сварке</p>
                </nuxt-link>
              </div>
              <div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-700 px-1 py-1 rounded-md border border-white/20 shadow-md shadow-black/50">
                <img src="/bnr/schweissbrenner.webp" class=" rounded-full w-24 border border-white/20"/>
                <nuxt-link :to="{ name: 'prods', query: { ct: 2 }}" class="">
                  <p class="">Сварочные горелки и их изнашиваемые детали</p>
                </nuxt-link>
              </div>
              <div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-700 px-1 py-1 rounded-md border border-white/20 shadow-md shadow-black/50">
                <img src="/bnr/schweisszusatzwerkstoffe.webp" class=" rounded-full w-24 border border-white/20"/>
                <nuxt-link :to="{ name: 'prods', query: { ct: 4 }}" class="">
                  <p class="">Сварочные электроды, проволока и присадочные материалы</p>
                </nuxt-link>
              </div>
              <div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-700 px-1 py-1 rounded-md border border-white/20 shadow-md shadow-black/50">
                <img src="/bnr/oberflaechenbearbeitung.webp" class=" rounded-full w-24 border border-white/20"/>
                <nuxt-link :to="{ name: 'prods', query: { ct: 5 }}" class="">
                  <p class="">Инструменты и химия для очистки поверхности</p>
                </nuxt-link>
              </div>          
              <div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-700 px-1 py-1 rounded-md border border-white/20 shadow-md shadow-black/50">
                <img src="/bnr/schweisszubehoer.webp" class=" rounded-full w-24 border border-white/20"/>
                <nuxt-link :to="{ name: 'cts' }" class="">
                  <p class="">Другие принадлежности для ваших сварочных работ</p>
                </nuxt-link>
              </div>              
            </div>

          </div>

        </div>
      </div>




      <div class="bg-white dark:bg-gray-800 rounded-md border border-gray-200 dark:border-gray-700 py-4 px-4 my-4">
        
        <div class="py-4">

          <div class="">
            <div class="py-4">

              <div class="py-1">
                <p class="text-lg">{{ descriptionData }}</p>  
              </div>
              <div class="py-1 max-w-3xl">
                <p class="text-sm">
                  Наши магазины – это место, где профессионалы и энтузиасты приходят за лучшими решениями для сварочных работ. Сварка - это искусство, и мы знаем, как сделать его доступным и эффективным для каждого.
                </p>
              </div>

            </div>

          </div>
        </div>


        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 hidden">
            <div class="flex items-center py-4">
              <div class="">
                <p class="text-2xl text-center">Сертификаты</p>
                <div class="">
                  <p class="text-sm text-center">
                    Мы являемся официальным дистрибьютором ведущих брендов сварочного оборудования, и всегда готовы предложить вам широкий выбор продуктов, которые обеспечат вашу эффективную и качественную работу. Наши специалисты всегда готовы проконсультировать вас и помочь выбрать именно то, что вам нужно.
                  </p>
                </div>                
              </div>
            </div>

            <div class="flex items-center gap-4">
              <div class="">
                <img alt="cert-1" src="/esab-cert.jpg" class="rounded-md shadow-md shadow-black/50 cursor-zoom-in w-48" fluid/>
              </div>
              <div class="">
                <img alt="cert-2" src="/cert-redius.jpg" class="rounded-md shadow-md shadow-black/50 cursor-zoom-in w-48" fluid />
              </div>
              <div class="">
                <img alt="cert-3" src="/svarog.jpg" class="rounded-md shadow-md shadow-black/50 cursor-zoom-in w-48" fluid />
              </div>                
            </div>            
          </div>




          <!-- <p class="text-xs">{{ clientStore.client.adress }}</p> -->

          
          <!-- <div class="bg-white dark:bg-gray-700 rounded-md shadow-md shadow-black/50 flex items-center justify-center border border-gray-200 dark:border-gray-600 py-2 px-4">
            <p class="text-sm">
              Здесь вы найдете бренды известных производителей, таких как  EWM, ESAB, Fubag, Aurora, Grovers, Cebora и многих других. Поддайтесь очарованию нашего профессионального и широкого ассортимента изделий: от сварочных аппаратов для инверторных, MIG/MAG, TIG или плазменных процессов, до многочисленных дополнительных материалов и до кислородно-топливной технологии. Каждый гарантированно найдет то, что ищет. Главный сварщик предлагает вам сварочную технику как для новичков, так и профессиональное оборудование. Мы также уделяем первостепенное внимание области безопасности труда сварщиков: будь то защита тела, защита ног, защита рук, защита головы, защита глаз и лица, защита рабочего места или защитные шторы для сварки - просто выберите подходящее оборудование для ваших нужд и стань настоящим героем сварки!
            </p>
          </div> -->
      </div>


    </div>

    <AppFooter />
    
  </div>
</template>