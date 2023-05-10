<template>
  <div>
    <h1>hello, {{ userName }}</h1> <!--url로 데이터 전달 : param, query-->

  </div>
</template>

<script>
export default {
  name: "HelloView",
  data () {
    return {
      userName: this.$route.params.userName
    }
  }

}
</script>

<style>

</style>