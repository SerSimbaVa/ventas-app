<template>
  <div class="p-6 bg-gray-100 min-h-screen space-y-8">
    <!-- Título -->
    <h2 class="text-2xl font-bold text-gray-800 flex items-center gap-2">
      <span>📊</span> Dashboard de Ventas
    </h2>

    <!-- Estadísticas -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-white shadow-md rounded-2xl p-6 text-center">
        <p class="text-gray-500 text-sm">Total de Ventas</p>
        <p class="text-3xl font-bold text-indigo-600">{{ stats.total }}</p>
      </div>
      <div class="bg-white shadow-md rounded-2xl p-6 text-center">
        <p class="text-gray-500 text-sm">Media</p>
        <p class="text-3xl font-bold text-blue-600">{{ stats.mean }}</p>
      </div>
      <div class="bg-white shadow-md rounded-2xl p-6 text-center">
        <p class="text-gray-500 text-sm">Mediana</p>
        <p class="text-3xl font-bold text-green-600">{{ stats.median }}</p>
      </div>
      <div class="bg-white shadow-md rounded-2xl p-6 text-center">
        <p class="text-gray-500 text-sm">Moda</p>
        <p class="text-3xl font-bold text-purple-600">{{ stats.mode }}</p>
      </div>
    </div>

    <!-- Tabla de ventas -->
    <div class="bg-white shadow-md rounded-2xl p-6">
      <h3 class="text-lg font-semibold text-gray-700 mb-4">Resumen de Ventas</h3>
      <table class="w-full table-auto text-left text-sm">
        <thead class="bg-gray-100 text-gray-600">
          <tr>
            <th class="p-2">Producto</th>
            <th class="p-2">Cantidad</th>
            <th class="p-2">Fecha</th>
            <th class="p-2">Precio Unitario</th>
            <th class="p-2">Total</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="venta in sales" :key="venta.id" class="border-b">
            <td class="p-2">{{ venta.producto }}</td>
            <td class="p-2">{{ venta.cantidad }}</td>
            <td class="p-2">{{ venta.fecha }}</td>
            <td class="p-2">{{ formatCurrency(venta.precioUnitario) }}</td>
            <td class="p-2">{{ formatCurrency(venta.cantidad * venta.precioUnitario) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { computed } from 'vue'

// Query para estadísticas
const GET_STATS = gql`
  query {
    salesStatistics {
      total
      mean
      median
      mode
    }
    sales {
      id
      producto
      cantidad
      fecha
      precioUnitario
    }
  }
`

const { result } = useQuery(GET_STATS)

const stats = computed(() => result.value?.salesStatistics || {
  total: 0,
  mean: 0,
  median: 0,
  mode: 0
})

const sales = computed(() => result.value?.sales || [])

function formatCurrency(value) {
  return new Intl.NumberFormat('es-ES', {
    style: 'currency',
    currency: 'EUR'
  }).format(value)
}
</script>





