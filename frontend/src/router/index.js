import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: () => import('../page/landing.vue')
  },
  {
    path: '/patho',
    name: 'Patho',
    component: () => import('../page/patho.vue')
  },
  {
    path: '/activities',
    name: 'Activities',
    component: () => import('../page/acti.vue')
  },
  {
    path: '/aliments',
    name: 'Aliments',
    component: () => import('../page/aliment.vue')
  },
  {
    path: '/meal-plan',
    name: 'MealPlan',
    component: () => import('../page/mealplan.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router