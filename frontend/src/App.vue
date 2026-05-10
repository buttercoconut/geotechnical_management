<template>
  <div id="app">
    <nav>
      <router-link to="/data">지반 데이터</router-link>
      <router-link to="/modeling">모델링</router-link>
      <router-link to="/simulation">시뮬레이션</router-link>
      <router-link to="/safety">안전성 평가</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
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
</script>

<style>
nav {
  display: flex;
  gap: 1rem;
  background: #f0f0f0;
  padding: 0.5rem;
}
nav a {
  text-decoration: none;
  color: #333;
}
nav a.router-link-exact-active {
  font-weight: bold;
}
#app {
  font-family: Arial, sans-serif;
}
</style>
