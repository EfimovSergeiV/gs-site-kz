import { type } from 'os'
import { defineStore } from 'pinia'


interface Product {
  id: number
  vcode: string
  name: string
  rating: any
  price: number | null,
  status: string
  preview_image: string
  description: string,
  propstrmodel: any
  quantity: number
}

interface Client {
  shop_id: number | null
  region_code: string | null
  person:string | null
  phone: string | null
  email: string | null
  comment: any | null
  delivery: boolean
  adress: string | null
  
  city: string | null
  contact: string | null

  entity: boolean
  company: string | null
  legaladress: string | null
  inn: string | null
  kpp: string | null
  okpo: string | null
  bankname: string | null
  currentacc: string | null
  corresponding: string | null
  bic: string | null
}

interface ProductImages {
  id: number,
  image: string,
}

export const useShopStore = defineStore('ShopStore', {
  /// Определение локации и магазина пользователя
  state: () => ({
    shop: null,
    shops: [],
    city: 'Псков',
    writeUsModal: false
  }),
  actions: {
    selectShop(shop: any) {
      this.shop = shop
    },
    selectCityMaps(city: any) {
      this.city = city
    },
    writeShops(shops: any) {
      this.shops = shops
      this.shop = shops.value[0]
    },
    showWriteUsModal() {
      this.writeUsModal = !this.writeUsModal
    },
    async sendCoordinates(coordinates: any) {
      const config = useRuntimeConfig()
      const { data }: any = await useFetch(`${ config.public.baseURL }coordinates/`, {
        method: 'POST',
        body: coordinates
      });
      if (data.value) {
        this.city = data.value.at(-1)
        this.shops.forEach((el: any) => {
          if (el.city.toLowerCase() === this.city.toLowerCase()) {
            this.shop = el
          }
        })
      }
    }
  },
})

export const useProductsStore = defineStore('ProductsStore', {
  /// Манипуляции с товарами. Сравнение, корзина, избранное Notifications
  state: () => ({
    cart: [] as Product[],  /// Товары в корзине
    comp: [] as Product[],  /// Товары в сравнении
    like: [] as Product[],  /// Товары в избраннном
    requestPrice: null as Product | null, /// Модальное на запрос стоимости товара
    cartAlert: false, /// Уведомление о добавленном товаре (модальное окно)
    cartAlertBlock: false,  /// Уведомление о добавленном товаре (модальное окно)
    productImages: null as ProductImages[] | null, /// Отображение изображений товаров
  }),
  getters: {
    productInCart: (state) => (id: number) => {
      return state.cart.find((item) => item.id === id);
    },
    productInComp: (state) => (id: number) => {
      return state.comp.find((item) => item.id === id);
    },
    productInLike: (state) => (id: number) => {
      return state.like.find((item) => item.id === id);
    },
    cartTotalPrice: (state) => {
      let result = 0
      state.cart.forEach((el) => (result += el.price * el.quantity)) /// Проверка на null
      return result
    },
  },
  actions: {
    /// Добавление или удаление товаров
    addProduct(target: string, payload: Product) {
      console.log('addProd')
      const product: Product = { ...payload}
      
      /// Добавление или удаление товара в корзину
      if (target === 'cart') {
        product.quantity = 1
        const index = this.cart.findIndex((item) => item.id === product.id)
        if (index === -1){

          this.cart.push(product)

          if (!this.cartAlertBlock) {
            setTimeout(() => {
              this.cartAlert = !this.cartAlert
            }, 800);
          }

        } else {
          this.cart.splice(index, 1)
        }
      }
      /// Добавление или удаление товара в сравнение
      if (target === 'comp') {
        const index = this.comp.findIndex((item) => item.id === product.id)
        if (index === -1){
          this.comp.push(product)
        } else {
          this.comp.splice(index, 1)
        }
      }
      /// Добавление или удаление товара в избранные
      if (target === 'like') {
        const index = this.like.findIndex((item) => item.id === product.id)
        if (index === -1){
          this.like.push(product)
        } else {
          this.like.splice(index, 1)
        }
      }
    },
    /// Изменение кол-ва товаров в корзине
    changeQuantity( product: any, action: string ) {
      const cartProduct = this.cart.find((item) => item.id === product.id)
      if ( cartProduct &&  cartProduct.quantity > 1 && action === 'del' ) {
        cartProduct.quantity--
      } else if ( cartProduct && action === 'add') {
        cartProduct.quantity++
      }
    },
    clearCartProducts() {
      this.cart = []
    },
    showCartModal() {
      this.cartAlert = !this.cartAlert
    },
    addRequestPrice(product: any) {
      this.requestPrice = product
    },
    clearRequestPrice() {
      this.requestPrice = null
    },
    showProductImages(images: any) {
      this.productImages = images
      
    },
    clearProductImages() {
      this.productImages = null
    }
  },
})


export const useClientStore = defineStore('ClientStore', {
  /// Данные клиента 
  state: () => ({
    client: {
      shop_id: null,
      region_code: null,
      person: null,
      phone: null,
      email: null,
      comment: null,
      delivery: false,
      adress: null,

      city: 'Москва', /// Custom city
      contact: null,  /// Custom contact
    
      entity: false,
      company: null,
      legaladress: null,
      inn: null,
      kpp: null,
      okpo: null,
      bankname: null,
      currentacc: null,
      corresponding: null,
      bic: null,
    } as Client,

    locationModal: false,
    registerModal: false,
    loginModal: false,
    order: null,        /// Последний сделаный заказ, если заказан в этой сессии (завязан на модальку заказа)
    orderHistory: null, /// История заказов клиентов, получать из API
  }),
  actions: {
    saveClientData(data: any) {
      this.client = data
      this.client.comment = null
    },
    
  },
})



interface Toasts {
  id: number
  type: string
  text: string
}

export const useNotificationsStore = defineStore('NotificationsStore', {
  /// Уведомления и всплывающие окна 
  state: () => ({
    filterComponent: false,
    toasts: [] as Toasts[],
  }),
  actions: {
    statusFilterComponent() {
      this.filterComponent = !this.filterComponent
    },
    pushToast(toast: any) {
      this.toasts.push(toast)
      setTimeout(() => {
        this.toasts.shift()
      }, 5000 )
    },
    removeToast(id: number) {
      const toast = this.toasts.findIndex((item) => item.id === id)
      this.toasts.splice(toast, 1)
    }
  },
})