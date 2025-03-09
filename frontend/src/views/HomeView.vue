<template>
  <div class="w-full mt-4 p-6">
    <h1 class="text-2xl font-semibold text-gray-800 mb-4">Ask the Gemini</h1>
    <div class="space-y-5">
      <ChooseModel v-model="model" />
      <InputTextarea v-model="query" class="mt-4"
        placeholder="Enter your query and hit enter or press the submit button..." />
      <BaseButton @click="onSubmit">Submit</BaseButton>
      <AiResponse v-if="result" :value="result" />
    </div>
  </div>
</template>

<script setup lang="ts">
import InputTextarea from '@/components/ai-app/InputTextarea.vue';
import BaseButton from '@/components/BaseButton.vue';
import AiResponse from '@/components/ai-app/AiResponse.vue';
import ChooseModel from '@/components/ai-app/ChooseModel.vue';

import { queryGemini } from '@/lib/gemini';

import { ref } from 'vue';

const query = ref('');
const result = ref('');
const model = ref('');

async function onSubmit() {
  result.value = '';

  try {
    const response = await queryGemini(query.value, model.value);

    if (!response.body) throw new Error('No response body');

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      result.value += decoder.decode(value, { stream: true });
    }
  } catch (error) {
    console.error('Error fetching streamed data:', error);
  }
}
</script>
