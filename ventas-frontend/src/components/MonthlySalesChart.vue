<template>
  <div class="bg-white shadow rounded-2xl p-6 space-y-8">
    <h2 class="text-2xl font-bold text-gray-800">📈 Estadísticas de Ventas</h2>

    <!-- Ventas por Mes (línea) -->
    <div>
      <h3 class="text-lg font-semibold text-gray-700 mb-2">Ventas Mensuales</h3>
      <Line v-if="monthlyChartData" :data="monthlyChartData" :options="chartOptions" />
    </div>

    <!-- Ingresos por Producto (barras) -->
    <div>
      <h3 class="text-lg font-semibold text-gray-700 mb-2">Ingresos por Producto</h3>
      <Bar v-if="incomeChartData" :data="incomeChartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { Line, Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  BarElement,
  PointElement,
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
  LineElement,
  BarElement,
  PointElement,
  CategoryScale,
  LinearScale
)

// Consulta: Ventas por mes
const GET_MONTHLY_SALES = gql`
  query {
    salesByMonth {
      month
      totalQuantity
    }
  }
`

// Consulta: Ingresos por producto
const GET_SALES_INCOME = gql`
  query {
    sales {
      producto
      total
    }
  }
`

const { result: monthlyResult } = useQuery(GET_MONTHLY_SALES)
const { result: salesResult } = useQuery(GET_SALES_INCOME)

const monthlyChartData = computed(() => {
  console.log("monthlyChartData:", monthlyChartData.value);
  console.log("Datos desde Apollo:", monthlyResult.value);

  if (!monthlyResult.value?.salesByMonth) return null
  const labels = monthlyResult.value.salesByMonth.map((d) => d.month)
  const data = monthlyResult.value.salesByMonth.map((d) => d.totalQuantity)
  return {
    labels,
    datasets: [
      {
        label: 'Unidades Vendidas por Mes',
        data,
        borderColor: '#10b981',
        backgroundColor: '#34d39933',
        fill: true,
        tension: 0.4,
      },
    ],
  }
  

})

const incomeChartData = computed(() => {
  if (!salesResult.value?.sales) return null

  const ingresosPorProducto = {}

  salesResult.value.sales.forEach((venta) => {
    if (!ingresosPorProducto[venta.producto]) {
      ingresosPorProducto[venta.producto] = 0
    }
    ingresosPorProducto[venta.producto] += venta.total
  })

  const labels = Object.keys(ingresosPorProducto)
  const data = Object.values(ingresosPorProducto)

  return {
    labels,
    datasets: [
      {
        label: 'Ingresos por Producto (€)',
        data,
        backgroundColor: '#3B82F6',
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

  