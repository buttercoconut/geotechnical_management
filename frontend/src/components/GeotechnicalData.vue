# frontend/src/components/GeotechnicalData.vue
<template>
  <div>
    <h2>Geotechnical Data</h2>
    <form @submit.prevent="submit">
      <label>Site ID: <input v-model="form.site_id" type="number" required /></label>
      <label>Depth: <input v-model="form.depth" type="number" step="0.01" required /></label>
      <label>N Value: <input v-model="form.n_value" type="number" step="0.01" required /></label>
      <label>Location: <input v-model="form.location" required /></label>
      <label>Description: <input v-model="form.description" /></label>
      <button type="submit">Save</button>
    </form>
    <ul>
      <li v-for="item in dataList" :key="item.id">
        {{ item.id }} - Site {{ item.site_id }}: Depth {{ item.depth }}, N {{ item.n_value }} }
      </li>
    </ul>
  </div>
</template>
<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const form = ref({ site_id: 0, depth: 0, n_value: 0, location: "", description: "" })
const dataList = ref([])

const submit = async () => {
  await axios.post("http://localhost:8000/geotechnical/data", form.value)
  await fetchData()
}

const fetchData = async () => {
  const res = await axios.get("http://localhost:8000/geotechnical/data")
  dataList.value = res.data
}

onMounted(fetchData)
</script>
