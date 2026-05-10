<template>
  <div class="simulation">
    <h2>지반 안정성 시뮬레이션</h2>
    <button @click="runSimulation">시뮬레이션 실행</button>
    <p v-if="result">결과: {{ result }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const result = ref('');

const runSimulation = async () => {
  try {
    const res = await axios.post('/api/simulation/run');
    result.value = res.data.message;
  } catch (e) {
    console.error(e);
    result.value = '실패';
  }
};
</script>
