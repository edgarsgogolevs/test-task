<script setup lang="ts">
import { RouterView } from 'vue-router';
import DefaultHeader from './components/DefaultHeader.vue';
</script>

<template>
  <DefaultHeader />
  <main
    class="container min-h-[calc(100vh-60px)] w-full mx-auto flex justify-center bg-white shadow-lg rounded-lg p-6"
  >
    <RouterView />
  </main>
</template>

<style scoped></style>
