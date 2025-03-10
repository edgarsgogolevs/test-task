<template>
  <textarea
    v-model="model"
    :rows="props.rows || 3"
    :placeholder="props.placeholder"
    class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300 outline-none"
    :class="{'ring-red-500 ring-2': props.invalid}"
  />
</template>

<script setup lang="ts">
const model = defineModel<string>();

const props = defineProps<{
  placeholder?: string;
  rows?: number;
  invalid?: boolean;
}>();
</script>
