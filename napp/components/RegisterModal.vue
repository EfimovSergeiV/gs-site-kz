<script setup>
  const config = useRuntimeConfig()
  // const router = useRouter()

  const productsStore = useProductsStore()
  const clientStore = useClientStore()
  const notificationsStore = useNotificationsStore()
  const { signIn, token, data, status, lastRefreshedAt } = useAuth()

  const errorMsg = ref(null)
  const username = ref(null)
  const email = ref(null)
  const first_name = ref(null)
  const last_name = ref(null)
  const password = ref(null)

  /// Переключение видимости пароля
  const showPassword = ref(false)
  const inputStatus = ref('password')
  watch(showPassword, async () => {
    if (showPassword.value) {
      inputStatus.value = 'text'
    } else {
      inputStatus.value = 'password'
    }
  })

  const sendForm = async () => {
    if ( username.value && email.value && first_name.value && last_name && password.value ) {
      const { data, pending, error } = await useFetch(`${ config.public.baseURL }signup/`, {
        method: 'POST',
        body: {
          username: username.value,
          email: email.value,
          first_name: first_name.value,
          last_name: last_name.value,
          password: password.value,        
        }
      });

      if (error.value == null) {
        signIn({ username: username.value, password: password.value })
        notificationsStore.pushToast({ id: 1, type: 'success', text: 'Вы успешно зарегистрированы' })
        clientStore.registerModal = false       
      } else {
        errorMsg.value = 'Ошибка: Пользователь уже существует или email уже используется'
      }


    } else {
      errorMsg.value = 'Ошибка: неверно введены данные'
    }
  }


</script>



<template>

  <div class="fixed z-40 w-full h-full bg-gray-500/50 backdrop-blur-sm">
    <div class="flex items-center justify-center h-full">
      <div class="h-full w-full flex items-center justify-center">
        

        <div class="container mx-auto px-4 lg:max-w-4xl lg:px-8">
          <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <div class="">

              <div class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-700">
                <h3 class="text-xl font-semibold text-gray-800 dark:text-white">
                  Регистрация
                </h3>
                <button @click="clientStore.registerModal = false" type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="defaultModal">
                  <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                  <span class="sr-only">Закрыть окно</span>
                </button>
              </div>

              <div class="px-4 py-8 min-h-[20rem]">
                <div class="grid grid-cols-2 gap-4 items-end">
                  <div class="">
                    <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-700 dark:text-gray-400">Логин</label>
                    <div>
                      <input v-model="username" type="text" id="login" class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-600 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="">
                    </div> 
                  </div>
                  <div class="">
                    <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-700 dark:text-gray-400">Электронная почта</label>
                    <div>
                      <input v-model="email" type="search" id="email" class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-600 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="">
                    </div> 
                  </div>
                  <div class="">
                    <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-700 dark:text-gray-400">Имя</label>
                    <div>
                      <input v-model="first_name" type="text" id="firstname" class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-600 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="">
                    </div> 
                  </div>
                  <div class="">
                    <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-700 dark:text-gray-400">Фамилия</label>
                    <div>
                      <input v-model="last_name" type="text" id="lastname" class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-600 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="">
                    </div> 
                  </div>
                  <div class="">
                    <label for="message" class="block mt-2 mb-1 text-xs font-medium text-gray-700 dark:text-gray-400">Пароль</label>
                    <div>
                      <input v-model="password" :type="inputStatus" id="password" class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-600 dark:border-gray-700 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="">
                    </div>
                  </div>

                  <button @click="sendForm">
                    <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                      <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                        <p class="px-5 py-2.5">Отправить</p>
                      </div>
                    </div>
                  </button>

                </div>
                <div class="flex items-center justify-between py-1">
                  <div class="">
                    <input 
                      id="show-pwd"
                      type="checkbox"
                      value="text"
                      v-model="showPassword"
                      class="w-4 h-4 
                        rounded text-gray-700 focus:ring-0 
                        focus:ring-gray-300 ring-offset-gray-300 bg-gray-700 border-gray-300
                        dark:focus:ring-gray-700 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-700
                      " >
                    <label for="show-pwd" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Показать пароль</label>
                  </div>
                  <div class="">
                    <p class="text-red-600 dark:text-red-500 text-sm">{{ errorMsg }}</p>
                  </div>
                </div>

              </div>


            </div>


          </div>
        </div>


      </div>        
    </div>
  </div>
</template>