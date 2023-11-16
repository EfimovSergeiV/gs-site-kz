<script setup>
  const config = useRuntimeConfig()
  const { data: brands } = await useFetch(`${ config.public.baseURL }c/brands/`)

</script>


<template>
  <div class="container mx-auto px-4 max-w-6xl lg:px-8 pt-2">
    <div class="bg-gray-100 dark:bg-gray-800 rounded-t-md border-t border-x border-gray-200 dark:border-gray-700 px-4 py-2 relative">

      <div class="md:flex md:justify-between items-center py-2">

        <div class="md:order-2">
          <div class="flex gap-2 items-end justify-end px-4">
            <p class="mdi mdi-36px mdi-map-marker-outline"></p>
            <div class="flex flex-col">
              <p class="text-sm text-end">Рудный, ул. Топоркова 35, 111500</p>
              <a href="tel:+77084238070" class="text-2xl text-end">+7 (708) 423-80-70</a>
            </div>
          </div>


          <p class="mt-2 text-sm">Наш график работы:</p>
          <div class="flex items-end justify-between gap-12">
            <div class="grid grid-cols-1 gap-1">
              <div class=" border-b border-gray-200 dark:border-gray-700">
                <div class="grid grid-cols-2 gap-10 md:gap-12">
                  <p class="text-xs">понедельник</p>
                  <p class="text-xs">08:30 – 17:30</p>
                </div>                      
              </div>
              <div class=" border-b border-gray-200 dark:border-gray-700">
                <div class="grid grid-cols-2 gap-10 md:gap-12">
                  <p class="text-xs">вторник</p>
                  <p class="text-xs">08:30 – 17:30</p>
                </div>                      
              </div>
              <div class=" border-b border-gray-200 dark:border-gray-700">
                <div class="grid grid-cols-2 gap-10 md:gap-12">
                  <p class="text-xs">среда</p>
                  <p class="text-xs">08:30 – 17:30</p>
                </div>                          
              </div>
            </div>
            <div class="grid grid-cols-1 gap-1">
              <div class=" border-b border-gray-200 dark:border-gray-700">
                <div class="grid grid-cols-2 gap-10 md:gap-12">
                  <p class="text-xs">четверг</p>
                  <p class="text-xs">08:30 – 17:30</p>
                </div>                      
              </div>
              <div class=" border-b border-gray-200 dark:border-gray-700">
                <div class="grid grid-cols-2 gap-10 md:gap-12">
                  <p class="text-xs">пятница</p>
                  <p class="text-xs">08:30 – 17:30</p>
                </div>                      
              </div>
              <div class=" border-b border-gray-200 dark:border-gray-700">
                <div class="grid grid-cols-2 gap-10 md:gap-12">
                  <p class="text-xs">суббота</p>
                  <p class="text-xs">09:00 – 15:00</p>
                </div>                      
              </div>
              <div class=" border-b border-gray-200 dark:border-gray-700">
                <div class="grid grid-cols-2 gap-10 md:gap-12">
                  <p class="text-xs">воскресенье</p>
                  <p class="text-xs">Закрыто</p>
                </div>                          
              </div>
            </div>
          </div>
        </div>

        <div class="w-full h-full md:w-1/2 md:order-1">
          
          <p class="text-[10px] md:text-xs my-3 select-none text-gray-700 dark:text-gray-300">
            Все цены и материаллы, указанные на сайте www.glsvar.kz, приведены как справочная информация и не являются публичной офертой и могут быть изменены в любое время без предупреждения. 
            Для получения подробной информации о стоимости, сроках и условиях поставки просьба обращаться по указанным на сайте телефонам.
          </p>  
          <div class="">
            <ul class="flex justify-start gap-8 text-xs md:text-sm mt-3 sm:mt-0 md:order-last py-2 ">
              <li>
                <button @click="showAllert()" class="text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100">Доставка</button>
              </li>
              
              <li>
                <button @click="showAllert()" class=" text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100">Способы оплаты</button>
              </li>

              <li>
                <nuxt-link :to="{ name: 'policy'}" class=" text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100 text-xs md:text-sm">Политика обработки данных</nuxt-link>
              </li>
            </ul>
          </div>
        
        </div>
      </div>


      <div class="">
        <div class="flex items-center justify-start">

          <span class="text-xs text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-gray-100 flex items-end justify-center md:justify-start">© 2023 <p class="mx-1">Главный сварщик</p></span>

        </div>
      </div>

    </div>
  </div>
</template>