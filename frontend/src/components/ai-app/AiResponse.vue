<template>
  <h3 class="text-xl font-bold">Answer</h3>
  <div class="p-4 bg-gray-50 border rounded-lg text-gray-700">
    <div v-html="renderedMd"></div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, computed} from 'vue';

import markdownit from 'markdown-it';

const props = defineProps<{
  value: string;
}>();

const renderer = markdownit({
  typographer: true
});

const renderedMd = computed<string>(() => {
  return renderer.render(props.value);
});

</script>
