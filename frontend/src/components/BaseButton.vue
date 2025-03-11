<template>
  <div class="flex justify-end">
    <button :disabled="!!props.disabled"
      class="w-[100px] bg-blue-600 text-white disabled:opacity-50 disabled:cursor-not-allowed py-2 rounded-lg hoverbg-blue-700 transition">
      <slot></slot>
    </button>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  disabled?: boolean;
}>();
</script>
