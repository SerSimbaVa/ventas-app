import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '@/views/DashboardView.vue'
import VentasView from '@/views/VentasView.vue'
import EstadisticasView from '@/views/EstadisticasView.vue'

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', name: 'Dashboard', component: DashboardView },
  { path: '/ventas', name: 'Ventas', component: VentasView },
  { path: '/estadisticas', name: 'Estadísticas', component: EstadisticasView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
