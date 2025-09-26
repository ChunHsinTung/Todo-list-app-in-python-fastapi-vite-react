<script setup>
import { ref } from "vue";

const title = ref("");
const notes = ref("");

const emit = defineEmits(["create"]);

function submit() {
  if (!title.value.trim()) return;
  emit("create", { title: title.value.trim(), notes: notes.value || null });
  title.value = "";
  notes.value = "";
}
</script>

<template>
  <form @submit.prevent="submit" class="mb-4 flex gap-2">
    <input v-model="title" placeholder="Add a task…" class="flex-1 border p-2" />
    <input v-model="notes" placeholder="Notes (optional)" class="flex-1 border p-2" />
    <button class="border px-4">Add</button>
  </form>
</template>
