<template>
  <h3 class="text-xl font-bold">Answer</h3>
  <div class="mt-4 p-4 bg-gray-50 border rounded-lg text-gray-700">
    {{ props.value }}
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
  value: string;
}>();
console.log(props.value);
</script>
