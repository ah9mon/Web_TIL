<template>
  <div id="app">
    <!--app꺼-->
    <div>
      <h1>App</h1>
      <input type="text" v-model="InputData">
      <br>
    </div>
    <!--children's-->
    <p>parentData : {{ parentInput }}</p>
    <p>childData : {{ childInput }}</p>
    <div>

      <br>
    </div>
    <!--child-->
    <AppParent 
    :app-to-parent = 'this.InputData'
    @parent-input = 'getParentDynamicData'
    @child-input = 'getChildDynamicData'
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent.vue';

export default {
  name: 'App',
  data: function () {
    return {
      InputData:null,
      parentInput:null,
      childInput:null,
    }
  },
  components: {
    AppParent,
  },
  methods: {
    getParentDynamicData : function (input) {
      console.log(input)
      this.parentInput = input
    },
    getChildDynamicData : function (input) {
      console.log(input)
      this.childInput = input
    },
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
