import { createRouter, createWebHistory } from 'vue-router';
import DietRecommendations from './components/DietRecommendations.vue';
import ExerciseRecommendations from './components/ExerciseRecommendations.vue';
import MentalHealthTips from './components/MentalHealthTips.vue';

const routes = [
  { path: '/', redirect: '/diet' },
  { path: '/diet', component: DietRecommendations },
  { path: '/exercise', component: ExerciseRecommendations },
  { path: '/mental-health', component: MentalHealthTips },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
