<template>
  <div class="modeling">
    <h2>3D 지반 모델링</h2>
    <div ref="canvasContainer" style="width: 100%; height: 500px;"></div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

const canvasContainer = ref(null);

onMounted(() => {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, canvasContainer.value.clientWidth / canvasContainer.value.clientHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(canvasContainer.value.clientWidth, canvasContainer.value.clientHeight);
  canvasContainer.value.appendChild(renderer.domElement);

  const geometry = new THREE.BoxGeometry(1, 1, 1);
  const material = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true });
  const cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  camera.position.z = 5;

  const controls = new OrbitControls(camera, renderer.domElement);

  const animate = function () {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
  };

  animate();
});
</script>

<style scoped>
.modeling {
  padding: 1rem;
}
</style>
