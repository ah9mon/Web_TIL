<template>
  <div>
    <h3>This is child component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ mamaProps }}</p>
    <button @click="ChildToParent">click!</button>
    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data: function () {
    return {
      childInputData: null,
    }
  },
  props : {
    staticProps : String,
    mamaProps : String,
  },
  methods: {
    ChildToParent: function () {
      this.$emit("child-to-parent")
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData)
      this.childInputData = ""
    }
  }
}
</script>

<style>
  
</style>
