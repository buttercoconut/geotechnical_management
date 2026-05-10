<template>
  <div class="simulation">
    <h2>지반 안정성 시뮬레이션</h2>
    <div>
      <label>지반 깊이 (m): <input v-model.number="depth" type="number" min="0" /></label>
      <label>지반 수직응력 (kPa): <input v-model.number="sigma_v" type="number" min="0" /></label>
      <label>지반 수평응력 (kPa): <input v-model.number="sigma_h" type="number" min="0" /></label>
      <button @click="runSimulation">시뮬레이션 실행</button>
    </div>
    <div v-if="result">
      <p>안정성 지수 (Factor of Safety): {{ result.fos.toFixed(2) }}</p>
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

const runSimulation = () => {
  // 간단한 Bishop's method 예시
  const gamma = 18; // unit weight kN/m3
  const c = 25; // cohesion kPa
  const phi = 30; // friction angle degrees
  const n = 10; // number of slices

  const gamma_h = gamma * depth.value;
  const sigma_h_total = sigma_h.value;
  const sigma_v_total = sigma_v.value;

  let sum = 0;
  for (let i = 1; i <= n; i++) {
    const z = (i - 0.5) * depth.value / n;
    const sigma_v_i = sigma_v_total * (z / depth.value);
    const sigma_h_i = sigma_h_total * (z / depth.value);
    const numerator = sigma_v_i + sigma_h_i;
    const denominator = c + (sigma_v_i - sigma_h_i) * Math.tan(phi * Math.PI / 180);
    sum += numerator / denominator;
  }
  const fos = sum / n;
  result.value = {
    fos,
    isSafe: fos >= 1.5
  };
};
</script>

<style scoped>
.simulation {
  padding: 1rem;
}
</style>
