# Nuxt 3 Minimal Starter

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install the dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm run dev

# yarn
yarn dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm run build

# yarn
yarn build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm run preview

# yarn
yarn preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.


```bash
npm install -D @tailwindcss/aspect-ratio
npm install -D @tailwindcss/line-clamp
npm install -D @tailwindcss/typography
npm install -D @tailwindcss/forms
npm install @mdi/font
```

### Examples
```typescript
<script setup>
  const props = defineProps({
    id: Number
  })
  const { data: quote, pending, error } = await useFetch(() => `https://dummyjson.com/quotes/${props.id}`)
</script>

<template>
  <div>
    <p v-if="pending">Fetching...</p>
    <pre v-else-if="error">Could not load quote: {{ error.data }}</pre>
    <figure v-else class="quote">
      <blockquote>{{ quote.quote }}</blockquote>
      <figcaption>&mdash; {{ quote.author }}</figcaption>
    </figure>
  </div>
</template>

<style scoped>
.quote {
  font: 1.25rem serif, system-ui;
  line-height: 150%;
  max-width: 60ch;
  margin: 1.5rem 0;
  padding: 1rem;
  border-radius: .5em;
  background: hsl(260, 60%, 96%);
  border: 1px solid hsl(260, 60%, 92%);
}
.quote figcaption,
.quote blockquote {
  margin: 1rem;
}
</style>
```

```typescript
<div class="">
  <Swiper
    class="rounded-md relative"
    style=""
    :modules="[SwiperAutoplay, SwiperEffectCreative]"
    :slides-per-view="1"
    :loop="true"
    :effect="'creative'"
    :autoplay="{
      delay: 10000,
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
    <SwiperSlide v-for="slide in images" :key="slide.id" class="">
      <img
        :src="slide.url"
        class="rounded-md border dark:border-gray-700 shadow-md "
      />             
    </SwiperSlide>
    <div class="absolute bottom-0 right-0 z-40 p-3">
      <SwiperControls />
    </div>
  </Swiper>
</div>
```