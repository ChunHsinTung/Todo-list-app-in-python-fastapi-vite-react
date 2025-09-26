<script setup>
import { ref, onMounted } from "vue";
import TodoForm from "./components/TodoForm.vue";
import TodoList from "./components/TodoList.vue";
import { fetchTodos, createTodo, updateTodo, deleteTodo } from "./api/todoApi";

const todos = ref([]);
const loading = ref(true);
const error = ref("");

async function load() {
  try {
    loading.value = true;
    todos.value = await fetchTodos();
  } catch (e) {
    error.value = "Failed to load todos.";
  } finally {
    loading.value = false;
  }
}

async function addTodo(newTodo) {
  const created = await createTodo(newTodo);
  todos.value.unshift(created);
}

async function toggleCompleted(todo) {
  const updated = await updateTodo(todo.id, { completed: !todo.completed });
  Object.assign(todo, updated); // keep reactivity
}

async function saveEdits(todo, patch) {
  const updated = await updateTodo(todo.id, patch);
  Object.assign(todo, updated);
}

async function removeTodo(todo) {
  await deleteTodo(todo.id);
  todos.value = todos.value.filter(t => t.id !== todo.id);
}

onMounted(load);
</script>

<template>
  <main class="max-w-xl mx-auto p-6">
    <h1 class="text-2xl font-bold mb-4">My To-Dos</h1>

    <TodoForm @create="addTodo" />

    <p v-if="loading">Loading…</p>
    <p v-else-if="error">{{ error }}</p>
    <TodoList
      v-else
      :items="todos"
      @toggle="toggleCompleted"
      @edit="saveEdits"
      @remove="removeTodo"
    />
  </main>
</template>

<style>
/* add your styles or Tailwind */
</style>
