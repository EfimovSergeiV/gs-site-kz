<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()
  const tmp_id = useCookie('tmp_id')

  const { data: product } = await useFetch(`${ config.public.baseURL }c/prod/${route.params.id}`)
  await useFetch(`${ config.public.baseURL }u/uwatch/`, {
    method: 'POST',
    headers: { "Authorization": tmp_id.value, },
    body: { "viewed": product.value.id }
  })


  const price = ref("0")
  const brand = ref('noname')
  if ( product.value.brand ) {
    brand.value = product.value.brand.brand
  }
  if ( product.value.price ) {
    price.value = `${product.value.price}00`
  }


  if ( product.value.id ) {
    useHead({
      script: [{
      type: 'application/ld+json',
      innerHTML: JSON.stringify({
          "type": "application/ld+json",
          "textContent": {
              "@context": "https://schema.org",
              "@type": "Product",
              "id": product.value.vcode,
              "name": product.value.name,
              "image": product.value.preview_image,
              "description": product.value.clean_desc,
              "mpn": product.value.vcode,
              "brand": {
                "@type": 'Brand',
                "name": brand.value,
              },
              "aggregateRating": {
                '@type': 'AggregateRating',
                "ratingValue": product.value.rating,
                "reviewCount": '5',
              },
              "offers": {
                '@type': 'Offer',
                "url": 'https://glsvar.kz/product/' + product.value.id,
                "priceCurrency": 'KZT',
                "price": price.value,
                "itemCondition": 'https://schema.org/UsedCondition',
                "availability": 'https://schema.org/InStock',
              },
            }
        })
      }],
    })    
  }


  const status = ref('заказать')

  if ( product.value.status === 'stock' ) {
    status.value = 'купить'
  }

  useSeoMeta({
    title: `${ product.value.name } - ${status.value} онлайн в Главный Сварщик`,
    description: `${ product.value.clean_desc }`,
    keywords: `${ product.value.name }, Главный Сварщик - сварочное оборудование, оборудование для сварки, купить электроды, купить проволоку, купить источник, купить сварочный инвертор`,
    ogLocale: 'ru_RU',
    ogTitle: `${ product.value.name }`,
    ogDescription: `${ product.value.clean_desc }`,
    ogImage: `${ product.value.preview_image }`,
    twitterCard: `${ product.value.preview_image }`,
  })

  

  let relCT = ''
  for ( let i in product.value.related ) {
    relCT += `ct=${product.value.related[i]}&`
  }

  const { data: analogue } =  await useFetch(`${ config.public.baseURL }c/related/?ct=${product.value.category.id}&ct=${product.value.category.id}`)
  // const { data: recommends } = await useFetch(`${ config.public.baseURL }c/prod/${route.params.id}`) ???
  const { data: related } =  await useFetch(`${ config.public.baseURL }c/related/?${relCT}`)
  const { data: recommends } = await useFetch(`${ config.public.baseURL }c/recommend/`)
  const { data: breadcrumbs } = await useFetch(`${ config.public.baseURL }c/breadcrumb/?ct=${product.value.category.id}`)
  
</script>


<template>
  <div class="">

    <AppHeader />
    <BreadCrumbs :breadcrumbs="breadcrumbs" />
    <ProductDetail :product="product" :related="related" :analogue="analogue.slice(0, 2)" />
    <Recommend :recommends="recommends" />
    <AppFooter />
    
  </div>
</template>