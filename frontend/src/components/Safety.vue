<template>
  <div class="safety">
    <h2>안전 관리</h2>
    <ul>
      <li v-for="worker in workers" :key="worker.id">
        {{ worker.name }} - {{ worker.status }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const workers = ref([]);

onMounted(async () => {
  try {
    const res = await axios.get('/api/safety/workers');
    workers.value = res.data;
  } catch (e) {
    console.error(e);
  }
});
</script>
