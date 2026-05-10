import { createRouter, createWebHistory } from 'vue-router';
import GeotechnicalData from './components/GeotechnicalData.vue';
import Modeling from './components/Modeling.vue';
import Simulation from './components/Simulation.vue';
import Safety from './components/Safety.vue';

const routes = [
  { path: '/data', component: GeotechnicalData },
  { path: '/modeling', component: Modeling },
  { path: '/simulation', component: Simulation },
  { path: '/safety', component: Safety },
  { path: '/', redirect: '/data' }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
