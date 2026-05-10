<template>
  <div class="geotechnical-data">
    <h2>지반 조사 데이터</h2>
    <table>
      <thead>
        <tr>
          <th>시추 ID</th>
          <th>위치 (X, Y)</th>
          <th>깊이 (m)</th>
          <th>N치수</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="sample in samples" :key="sample.id">
          <td>{{ sample.id }}</td>
          <td>{{ sample.x }}, {{ sample.y }}</td>
          <td>{{ sample.depth }}</td>
          <td>{{ sample.nValue }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const samples = ref([]);

const fetchSamples = async () => {
  try {
    const res = await axios.get('/api/geotechnical_data');
    samples.value = res.data;
  } catch (e) {
    console.error('Failed to fetch samples', e);
  }
};

onMounted(fetchSamples);
</script>

<style scoped>
.geotechnical-data {
  padding: 1rem;
}
</style>
