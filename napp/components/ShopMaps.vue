<script setup>
  const config = useRuntimeConfig()
  const shopStore = useShopStore()
  const { data: shops } = await useFetch(`${ config.public.baseURL }c/shops/`)

  /// Перенести карты в модели бэка
  const mapURLs = {
    "Псков" : "https://yandex.ru/map-widget/v1/?um=constructor%3A47f57d246b40670e64b17cb3f82dde8a81f3b3a825fa0ec9dc5e2a360214ec38&amp;source=constructor",
    "Москва" : "https://yandex.ru/map-widget/v1/?um=constructor%3Ae113235413b59c4ae31cb4d894caa9612e5c88e95cb5fc873f8508770800a19f&amp;source=constructor",
    "Санкт-Петербург" : "https://yandex.ru/map-widget/v1/?um=constructor%3A4892b9a6ff89034d14a4833ed892e30ddac4cde58559e85c6ae75d9d5cb766b2&amp;source=constructor",
    "Великие луки" : "https://yandex.ru/map-widget/v1/?um=constructor%3A8cbd01689857fcf3e2c9604637d5e0e3ac33b5e71467a701ed470d12b63e1dea&amp;source=constructor",
    "Смоленск" : "https://yandex.ru/map-widget/v1/?um=constructor%3A22e3d619383ca4fb59e78352a52f5e3808418009918e23d73549578277b6a013&amp;source=constructor",
    "Петрозаводск" : "https://yandex.ru/map-widget/v1/?um=constructor%3A7a6886838355b4c4aab4597dd2ee3dcd40eb7c6cd2bab5638666af5f1606c267&amp;source=constructor",
  }

</script>


<template>
  <div class="mx-auto px-4 max-w-6xl lg:px-8 py-2">

    <div class="mt-2 bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md">
      <div class="relative">
        <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d9607.746256144887!2d63.1143089!3d52.9855424!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x43cd03eb0088f70d%3A0xfaaebd2d312ed8f7!2z0JPQu9Cw0LLQvdGL0Lkg0KHQstCw0YDRidC40Lo!5e0!3m2!1sru!2sru!4v1695649108350!5m2!1sru!2sru" width="100%" height="350" frameborder="0" loading="lazy" class="rounded-md"></iframe>
      </div>
    </div>

  </div>
</template>