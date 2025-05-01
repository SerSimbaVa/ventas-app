<template>
  <div class="bg-white shadow rounded-2xl p-6">
    <h3 class="text-lg font-semibold text-gray-700 mb-4">📦 Ventas por Producto</h3>
    <Bar v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else class="text-gray-500">No hay datos disponibles</p>
  </div>
</template>

<script setup>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { computed } from 'vue'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
)

// Consulta: Cantidad total vendida por producto
const GET_SALES_BY_PRODUCT = gql`
  query {
    salesByProduct {
      producto
      totalCantidad
    }
  }
`

const { result } = useQuery(GET_SALES_BY_PRODUCT)

const chartData = computed(() => {
  if (!result.value?.salesByProduct) return null
  const labels = result.value.salesByProduct.map((item) => item.producto)
  const data = result.value.salesByProduct.map((item) => item.totalCantidad)
  return {
    labels,
    datasets: [
      {
        label: 'Unidades Vendidas',
        data,
        backgroundColor: '#6366F1',
      },
    ],
  }
})

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      display: true,
      position: 'top',
    },
  },
  scales: {
    y: {
      beginAtZero: true,
    },
  },
}
</script>

  