<template>
  <div class="modeling">
    <h2>3D 지반 모델링</h2>
    <div id="three-container" style="width: 100%; height: 500px;"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import * as THREE from 'three';

onMounted(() => {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 500, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer();
  renderer.setSize(window.innerWidth, 500);
  document.getElementById('three-container').appendChild(renderer.domElement);

  const geometry = new THREE.BoxGeometry();
  const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
  const cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  camera.position.z = 5;

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
#three-container {
  background: #f0f0f0;
}
</style>
