<template>
  <div>
    <div>
      <h1>AppParent</h1>
      <input type="text" v-model="parentInputData" @input="parentInputShooting">
    </div>
    <!--other's input-->
    <div>
      <p>appData: {{ appToParent }}</p>
      <p>childData: {{ childInput }}</p>
    </div>
    <AppChild 
    :parent-to-child = 'this.parentInputData'
    :app-to-child = 'appToParent'
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import AppChild from './AppChild.vue';

export default {
  name:'AppParent',
  components : {
    AppChild
  },
  data: function () {
    return {
      parentInputData : null,
      childInput: null,
    }
  },
  props: {
    appToParent : String,
  },
  methods: {
    parentInputShooting : function () {
      this.$emit('parent-input', this.parentInputData)
    },
    childInputShooting : function () {
      this.$emit('child-input', this.childInput)
    },
    getDynamicData : function (input) {
      console.log(input)
      this.childInput = input
      this.childInputShooting()
    },

  }

}
</script>

<style>

</style>