<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild
    static-props="component에서 child로" 
    :mamaProps="dynamicProps"
    />
    <MyChild
    static-props="1" 
    :mamaProps="1"
    />
    <MyChild
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />

  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  data: function () {
    return {
      dynamicProps : "it's in data"
    }
  },
  methods: {
    parentGetEvent:function () {
      console.log("자식에서 발생한 이벤트")
    },
    getDynamicData: function (input) {
      console.log(`child에서 입력한 ${input}을 출력`)
    }
  }

}

</script>

<style>
  .border {
    border: solid;
  }
</style>
