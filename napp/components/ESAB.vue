<script setup>
  const title = "Главный Сварщик - официальный партнер-дистрибьютор и авторизованный сервисный центр концерна ESAB"
  const text = "Бренд ESAB - синоним передового опыта в таких областях как: оборудование для ручной сварки и резки, сварочные материалы, автоматизированная сварка, механические системы резки. В каждой из этих сфер ESAB использует постоянно совершенствуемые методы, материалы и ноу-хау, чтобы в полной мере удовлетворить потребности всех секторов промышленности. Компания ESAB разрабатывает высокопроизводительные решения, которые отвечают требованиям заказчиков"

  const esabbanners = [
    {id: 1, image: '/esab-ok.jpg', path: { name: 'prods', query: { ct: 31, w4r4: 'ok48.00' } } },
    {id: 1, image: '/rogue-banner.jpg', path: { name: 'product-id', params: { id: 1705 } } },
    {id: 1, image: '/ws-esab.jpg', path: { name: 'prods', query: { ct: 14, brnd: 3 } } },
    {id: 1, image: '/handy-esab.jpg', path: { name: 'product-id', params: { id: 699 } } },
  ]

</script>

<template>
    <div class="container mx-auto px-4 py-2 max-w-6xl lg:px-8">

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <div class="border dark:border-gray-700 rounded-md shadow-md">

          <div class="relative">
            
            <img 
                class="rounded-md w-full h-full"
                loading=lazy
                width="800px"
                height="400px"
                alt="esab-1"
                src="/esab-banner-one.jpg" 
              />              

            <div class="absolute bottom-0 left-0 top-0">
              <div class="">
                <div class="flex items-center bg-gray-800/80 rounded-t-md">
                  <div class="p-1">
                    <nuxt-link :to="{ name: 'prods', query: { brnd: 3, page: 1 } }">
                      <img src="/esab-logo.jpg" class="w-[140px]" />
                    </nuxt-link>
                  </div>
                  <div class="p-1 text-gray-300">
                    <p class="text-sm xl:text-base">{{ title }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>

        
        <div class="">

          <div class="">
            <Swiper
              class="rounded-md relative"

              :modules="[SwiperAutoplay, SwiperEffectCreative]"
              :slides-per-view="1"
              :loop="true"
              :effect="'creative'"
              :autoplay="{
                delay: 8000,
                disableOnInteraction: true
              }"
              :creative-effect="{
                prev: {
                  shadow: false,
                  translate: ['-20%', 0, -1]
                },
                next: {
                  translate: ['100%', 0, 0]
                }
              }"
            >
              <SwiperSlide v-for="banner in esabbanners" :key="banner.id" class="">
                <nuxt-link :to="banner.path">
                  <img
                    :src="banner.image"
                    class="rounded-md border dark:border-gray-700 shadow-md "
                  />                 
                </nuxt-link>
              </SwiperSlide>
              <div class="absolute bottom-0 right-0 z-40 p-3">
                <SwiperControls  class="bg-gray-100/80 rounded-full border border-gray-200/50 hover:border-gray-300 dark:border-gray-600/50 dark:hover:border-gray-500 dark:bg-gray-700/80 transition-all duration-500 px-1" />
              </div>
            </Swiper>
          </div>



        </div>

      </div>


      <div class="flex items-center mt-2 p-1 bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md">
        <div class="hidden md:block flex-none">
          <img
            src="/esab-logo.jpg"
            class="w-[220px]"
          />
        </div>
        <div class=" md:p-4">
          <div class="">
            <p class="bg-clip-text text-gray-700 dark:text-gray-300 text-xs lg:text-base">
            {{ text }}
            </p>
          </div>
        </div>
      </div>


      </div>
</template>