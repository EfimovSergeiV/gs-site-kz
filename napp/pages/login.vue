<script lang="ts" setup>
// import { ref } from 'vue'
// import { definePageMeta, useAuth } from '#imports'

const { signIn, token, data, status, lastRefreshedAt } = useAuth()

const username = ref('')
const password = ref('')

definePageMeta({
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/'
  }
})
</script>


<template>
  <div class="mx-auto max-w-xl px-4 lg:px-8 py-8">



    <div class="grid grid-cols-2 gap-4">
      <div class="bg-white border-gray-200 border dark:border-gray-700 dark:bg-gray-800 py-12 px-8 rounded-md">

        <div class="flex items-center justify-start">
          <p>Авторизоваться</p>
        </div>

        <div class="">

          <div class="py-2">

            <div class="relative py-2">
              <input type="text" id="login" v-model="username" class="block px-2.5 py-1 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-700 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " />
              <label for="login" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] bg-white dark:bg-gray-800 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-gray-300 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-4 peer-focus:scale-75 peer-focus:-translate-y-4 left-2 mdi mdi-form-textbox"> Логин</label>
            </div>

            <div class="relative py-2">
              <input type="password" id="password" v-model="password" class="block px-2.5 py-1 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-700 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder=" " />
              <label for="showPassword" class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] bg-white dark:bg-gray-800 px-2 peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-gray-300 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-4 peer-focus:scale-75 peer-focus:-translate-y-4 left-2 mdi mdi-form-textbox-password"> Пароль</label>
            </div>
          </div>


          <div class="flex items-start justify-between py-2">
            <div class="flex items-center">
              <input id="link-checkbox" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-700">
              <label for="link-checkbox" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Отображать пароль</label>
            </div>

            <div class="flex items-center justify-end py-2">
              <button @click="signIn({ username, password })" class="">
                <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                  <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg">
                    <p class="text-white text-base w-52 py-1.5">Авторизоваться</p>
                  </div>
                </div>
              </button>
            </div>

          </div>
        </div>
      </div>
    </div>




    <h1 class="mt-8">Login Page</h1>
    <pre>Status: {{ status }}</pre>
    <pre>Data: {{ data || 'no session data present, are you logged in?' }}</pre>
    <pre>Last refreshed at: {{ lastRefreshedAt || 'no refresh happened' }}</pre>
    <pre>JWT token: {{ token || 'no token present, are you logged in?' }}</pre>

  </div>
</template>