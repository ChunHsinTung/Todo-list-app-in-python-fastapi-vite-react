<!-- src/components/TodoList.vue -->
<script setup>
import TodoItem from "./TodoItem.vue";
defineProps({ items: Array });
const emit = defineEmits(["toggle", "edit", "remove"]);
</script>

<template>
  <ul class="space-y-2">
    <TodoItem
      v-for="t in items"
      :key="t.id"
      :todo="t"
      @toggle="emit('toggle', t)"
      @edit="(patch) => emit('edit', t, patch)"
      @remove="emit('remove', t)"
    />
  </ul>
</template>