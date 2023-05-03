<template>
  <div>
    <div></div>
    <h1>AppChild</h1>
    <input type="text" v-model="childInputData"  @input="childInputShooting">
    <!--parent's-->
    <div>
      <p>appData : {{ appToChild }}</p>
      <p>parentData : {{ parentToChild }}</p>
      <p>childData : {{ this.childInputData }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name : 'AppChild',
  data : function () {
    return {
      childInputData:null
    }
  },
  props : {
    parentToChild : String,
    appToChild : String
  },
  methods: {
    childInputShooting : function () {
      this.$emit('child-input', this.childInputData)
    }
  }

}
</script>

<style>

</style>