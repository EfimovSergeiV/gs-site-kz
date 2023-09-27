<script setup>

  const notificationsStore = useNotificationsStore()

</script>


<template>
  <div class="">
    <div class="fixed z-40 top-5 right-0">

      <transition-group tag="div" name="right-emergence">
        <div v-for="toast in notificationsStore.toasts" :key="toast" class="w-96">

          <div v-if="toast.type === 'success'">
            <div :id="toast.id" @click="notificationsStore.removeToast(toast.id)" class="my-2 dark:text-gray-700 px-5 py-4 border-r-8 border-blue-600 bg-white drop-shadow-lg cursor-pointer rounded-l-sm">
              <div class="flex items-center justify-between">
                <div class="">
                  <p class="mdi mdi-36px mdi-information-outline text-blue-600"></p>
                </div>
                <div class="">
                  <p class="text-sm text-center">{{ toast.text }}</p>
                </div>
              </div>
            </div>          
          </div>

          <div v-if="toast.type === 'error'">
            <div :id="toast.id" @click="notificationsStore.removeToast(toast.id)" class="my-2 dark:text-gray-700 px-5 py-4 border-r-8 border-red-600 bg-white drop-shadow-lg cursor-pointer rounded-l-sm">
              <div class="flex items-center justify-between">
                <div class="">
                  <p class="mdi mdi-36px mdi-information-outline text-red-600"></p>
                </div>
                <div class="">
                  <p class="text-sm text-center">{{ toast.text }}</p>
                </div>
              </div>
            </div>          
          </div>
          
        </div>
      </transition-group>


    </div>

  </div>
</template>