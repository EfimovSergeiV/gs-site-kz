export default defineNuxtPlugin(nuxtApp => {
    if (process.client) {
      window.addEventListener('scroll', () => {
        const scrollPosition = document.documentElement.scrollTop
        const navMenu = document.getElementById('navbar')
  
        if (scrollPosition > 200) {
          navMenu.classList.remove('hidden',)

          // navMenu.classList.add('bg-white', 'fixed')
        } else {
          // navMenu.classList.remove('bg-white', 'fixed')
          
          navMenu.classList.add( 'hidden',)
        }
  
      })    
    }
  })