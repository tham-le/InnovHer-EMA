// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import Landing from '../page/Landing.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Landing',
      component: Landing
    },
    {
      path: '/me',
      name: 'Profile',
      component: () => import('../page/Profile.vue')
    },
    {
      path: '/aliments',
      name: 'Alimentation',
      component: () => import('../page/Aliment.vue')
    },
    {
      path: '/activities',
      name: 'Activities',
      component: () => import('../page/Acti.vue')
    },
    {
      path: '/patho',
      name: 'Pathologie',
      component: () => import('../page/Patho.vue')
    },
    {
      path: '/microbiote',
      name: 'Microbiote',
      component: () => import('../page/Microbiote.vue')
    }
  ]
})

export default router