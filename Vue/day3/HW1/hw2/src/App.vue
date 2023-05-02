<template>
  <div id="app">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
    <h1>버튼 박스 제작</h1>
    <br>
    <TimePicker/>
  </div>
</template>

<script>
import TimePicker from './components/TimePicker.vue'

export default {
  name: 'App',
  components: {
    TimePicker
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
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  flex-direction: column ;
  justify-content: center;
}

</style>
