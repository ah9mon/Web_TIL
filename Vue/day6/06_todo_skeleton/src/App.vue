<template>
  <div id="app">
    <h1>Todo</h1>
    <h1>총 할일 : {{ allTodosCount }}</h1>
    <h1>완료된 할일 : {{ allTodosCount }}</h1>
    <h1>남은 할일 : {{ allTodosCount }}</h1>
    <TodoForm/>
    <TodoList />
    <button @click="loadTodos">Todo 불러오기</button>
  </div>
</template>

<script>
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'

export default {
  name: 'App',
  methods : {
    loadTodos() {
      this.$store.dispatch('loadTodos')
    }
  },
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    allTodosCount() {
      return this.$store.getters.alltodosCount
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
