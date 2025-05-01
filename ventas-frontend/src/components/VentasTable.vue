<template>
  <div class="bg-white shadow rounded-2xl p-6 mt-6">
    <h3 class="text-lg font-semibold mb-4 text-gray-700">Ventas por Producto</h3>

    <!-- Tabla agrupada -->
    <div class="overflow-x-auto">
      <table class="min-w-full table-auto border border-gray-200">
        <thead class="bg-gray-100 text-gray-600">
          <tr>
            <th class="px-4 py-2 border">Producto</th>
            <th class="px-4 py-2 border">Cantidad Total</th>
            <th class="px-4 py-2 border">Precio Unitario (€)</th>
            <th class="px-4 py-2 border">Total de Ventas (€)</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(venta, index) in ventasAgrupadas"
            :key="index"
            class="text-center hover:bg-gray-50"
          >
            <td class="px-4 py-2 border">{{ venta.producto }}</td>
            <td class="px-4 py-2 border">{{ venta.cantidad }}</td>
            <td class="px-4 py-2 border">€{{ venta.precioUnitario.toFixed(2) }}</td>
            <td class="px-4 py-2 border">€{{ venta.total.toFixed(2) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
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

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

// GraphQL Query
const GET_SALES = gql`
  query {
    sales {
      id
      producto
      cantidad
      fecha
      precioUnitario
      total
    }
  }
`

const { result } = useQuery(GET_SALES)

const ventasAgrupadas = ref([])

watch(result, () => {
  if (result.value?.sales) {
    agruparVentas(result.value.sales)
  }
})

function agruparVentas(ventas) {
  const agrupadas = {}

  ventas.forEach((venta) => {
    if (!agrupadas[venta.producto]) {
      agrupadas[venta.producto] = {
        producto: venta.producto,
        cantidad: 0,
        precioUnitario: venta.precioUnitario,
        total: 0,
      }
    }

    agrupadas[venta.producto].cantidad += venta.cantidad
    agrupadas[venta.producto].total += venta.total
  })

  ventasAgrupadas.value = Object.values(agrupadas)

  actualizarDatosGrafico()
}

const chartData = ref({
  labels: [],
  datasets: [
    {
      label: 'Cantidad Vendida',
      data: [],
      backgroundColor: '#3B82F6',
    },
  ],
})

function actualizarDatosGrafico() {
  chartData.value.labels = ventasAgrupadas.value.map((v) => v.producto)
  chartData.value.datasets[0].data = ventasAgrupadas.value.map((v) => v.cantidad)
}

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      display: false,
    },
  },
  scales: {
    y: {
      beginAtZero: true,
    },
  },
}
</script>

  