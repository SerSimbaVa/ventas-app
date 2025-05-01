<template>
    <div class="bg-white shadow rounded-xl p-5 flex items-center justify-between">
      <div>
        <p class="text-sm text-gray-500">{{ title }}</p>
        <p class="text-2xl font-bold text-gray-800">{{ value }}</p>
      </div>
      <component :is="iconComponent" class="w-6 h-6" :class="color" />
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  import * as icons from 'lucide-vue-next'
  
  const props = defineProps({
    title: String,
    value: [String, Number],
    icon: String,
    color: String
  })
  
  const iconComponent = computed(() => icons[props.icon] || icons["Circle"])
  </script>
  