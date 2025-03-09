<template>
  <div class="w-full mt-4 p-6">
    <h1 class="text-2xl font-semibold text-gray-800 mb-4">Ask the Gemini</h1>
    <!-- TODO: option to choose the model -->
    <div class="space-y-5">
      <InputTextarea v-model="query" class="mt-4"
        placeholder="Enter your query and hit enter or press the submit button..." />
      <BaseButton @click="submit">Submit</BaseButton>
      <AiResponse v-if="result" :value="result" />
    </div>
  </div>
</template>

<script setup lang="ts">
import InputTextarea from '@/components/ai-app/InputTextarea.vue';
import BaseButton from '@/components/BaseButton.vue';
import AiResponse from '@/components/ai-app/AiResponse.vue';

import { queryGemini } from '@/lib/gemini';

import { ref } from 'vue';

const query = ref('');
const result = ref('');

function addCharWithDelay(char: string): Promise<void> {
  return new Promise((resolve) => {
    setTimeout(() => {
      result.value += char;
      resolve();
    }, 20);
  });
}

async function submit() {
  const testResult = 'Hello World. Hello lorem ipsum dolor gaslighting the world.';
  for (const char of testResult) {
    await addCharWithDelay(char);
  }
}

async function fetchStreamedData() {
  result.value = "";

  try {
    const response = await queryGemini(query.value, 'gemini-2.0-flash');

    if (!response.body) throw new Error("No response body");

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      result.value += decoder.decode(value, { stream: true });
    }
  } catch (error) {
    console.error("Error fetching streamed data:", error);
  }
}
</script>
