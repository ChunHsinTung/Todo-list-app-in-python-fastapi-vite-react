// src/api/todoApi.js
import axios from "axios";
const api = axios.create({ baseURL: "http://localhost:8000" });

export async function fetchTodos() {
    const { data } = await api.get("/todos/");
    return data;
}
export async function createTodo(payload) {
    const { data } = await api.post("/todos/", payload);
    return data;
}
export async function updateTodo(id, patch) {
    const { data } = await api.patch(`/todos/${id}`, patch);
    return data;
}
export async function deleteTodo(id) {
    await api.delete(`/todos/${id}`);
}
