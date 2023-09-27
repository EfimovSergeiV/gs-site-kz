/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./app.vue",

    // `${srcDir}/components/**/*.{vue,js,ts}`,
    // `${srcDir}/layouts/**/*.vue`,
    // `${srcDir}/pages/**/*.vue`,
    // `${srcDir}/composables/**/*.{js,ts}`,
    // `${srcDir}/plugins/**/*.{js,ts}`,
    // `${srcDir}/utils/**/*.{js,ts}`,
    // `${srcDir}/App.{js,ts,vue}`,
    // `${srcDir}/app.{js,ts,vue}`,
    // `${srcDir}/Error.{js,ts,vue}`,
    // `${srcDir}/error.{js,ts,vue}`,
    // `${srcDir}/nuxt.config.{js,ts}`

  ],
  darkMode: 'class',
  theme: {
    fontFamily: {
      // 'sans': ['Play-Regular', 'Helvetica', 'Arial', 'sans-serif' ],
      // 'serif': ['ui-serif', 'Georgia',],
      // 'mono': ['ui-monospace', 'SFMono-Regular',],
      // 'display': ['Oswald',],
      // 'body': ['"Open Sans"',],

      'sans': ['Play-Regular',],
      'serif': ['Play-Regular',],
      'mono': ['Play-Regular',],
      'display': ['Play-Regular',],
      'body': ['Play-Regular',],

    },
    extend: {
      screens: {
        sm: '520px',
        md: '820px',
        lg: '1140px',
        xl: '1440px',
      },
      container: {
        center: true,
      },
      colors: {
        'yellow-450': '#f8dc08',
        'yellow-550': '#baa50a',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
}

