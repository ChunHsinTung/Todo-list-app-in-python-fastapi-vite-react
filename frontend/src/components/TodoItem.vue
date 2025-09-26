<!-- src/components/TodoItem.vue -->
<script setup>
import { ref } from "vue";
const props = defineProps({ todo: Object });
const emit = defineEmits(["toggle", "edit", "remove"]);

const editing = ref(false);
const draftTitle = ref("");
const draftNotes = ref("");

function startEdit() {
  editing.value = true;
  draftTitle.value = props.todo.title;
  draftNotes.value = props.todo.notes || "";
}
function cancel() { editing.value = false; }
function save() {
  emit("edit", { title: draftTitle.value, notes: draftNotes.value });
  editing.value = false;
}
</script>

<template>
  <li class="border p-3 rounded">
    <div v-if="!editing" class="flex items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <input type="checkbox" :checked="todo.completed" @change="emit('toggle')" />
        <div>
          <p :class="{'line-through text-gray-500': todo.completed}">{{ todo.title }}</p>
          <small v-if="todo.notes" class="text-gray-600">{{ todo.notes }}</small>
        </div>
      </div>
      <div class="flex gap-2">
        <button @click="startEdit">Edit</button>
        <button @click="emit('remove')">Delete</button>
      </div>
    </div>

    <div v-else class="flex flex-col gap-2">
      <input v-model="draftTitle" class="border p-2" />
      <input v-model="draftNotes" class="border p-2" />
      <div class="flex gap-2">
        <button @click="save">Save</button>
        <button @click="cancel">Cancel</button>
      </div>
    </div>
  </li>
</template>