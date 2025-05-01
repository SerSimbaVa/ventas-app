
<template>
  <div class="flex">
    <aside class="w-64 bg-gray-800 text-white min-h-screen p-4">
      <h1 class="text-2xl font-bold mb-6">VentasApp</h1>
      <nav class="space-y-2">
        <RouterLink to="/dashboard" class="block hover:underline">Dashboard</RouterLink>
        <RouterLink to="/ventas" class="block hover:underline">Ventas</RouterLink>
        <RouterLink to="/estadisticas" class="block hover:underline">Estadísticas</RouterLink>
      </nav>
    </aside>
    <main class="flex-1 bg-gray-100 p-6">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>
