export default defineNuxtPlugin(nuxtApp => {
  if (process.client) {
    window.addEventListener('scroll', () => {
      const scrollTop = (window.pageYOffset || document.documentElement.scrollTop)/100;
      const background = document.querySelector('#background-page');

      if (background) {
        background.style.backgroundPositionY = `${100 + scrollTop}px`;
      }
    })    
  }
})
