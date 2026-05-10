<template>
  <div class="safety">
    <h2>지반 안전성 평가</h2>
    <div>
      <label>지반 깊이 (m): <input v-model.number="depth" type="number" min="0" /></label>
      <label>지반 수직응력 (kPa): <input v-model.number="sigma_v" type="number" min="0" /></label>
      <label>지반 수평응력 (kPa): <input v-model.number="sigma_h" type="number" min="0" /></label>
      <button @click="evaluateSafety">평가 실행</button>
    </div>
    <div v-if="result">
      <p>안전성 지수 (Factor of Safety): {{ result.fos.toFixed(2) }}</p>
      <p>결과: {{ result.isSafe ? '안전' : '위험' }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const depth = ref(10);
const sigma_v = ref(200);
const sigma_h = ref(150);
const result = ref(null);

const evaluateSafety = () => {
  // 간단한 Mohr-Coulomb 기반 평가
  const c = 25; // cohesion kPa
  const phi = 30; // friction angle degrees
  const gamma = 18; // unit weight kN/m3

  const sigma_v_total = sigma_v.value;
  const sigma_h_total = sigma_h.value;

  const sigma_n = (sigma_v_total + sigma_h_total) / 2;
  const tau = (sigma_v_total - sigma_h_total) / 2;

  const sigma_c = c + sigma_n * Math.tan(phi * Math.PI / 180);
  const fos = sigma_c / tau;

  result.value = {
    fos,
    isSafe: fos >= 1.5
  };
};
</script>

<style scoped>
.safety {
  padding: 1rem;
}
</style>
