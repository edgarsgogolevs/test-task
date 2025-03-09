<template>
  <div>
    <select v-model="model">
      <option v-for="m in models" :key="m">{{ m }}</option>
    </select>
  </div>
</template>

<script setup lang="ts">
import { defineModel, ref } from 'vue';

import { getAvailableModels } from '@/lib/gemini';

const models = ref<string[]>([]);
const model = defineModel<string>();

readModels();

async function readModels() {
  models.value = await getAvailableModels();
  model.value = models.value[0];
}
</script>
