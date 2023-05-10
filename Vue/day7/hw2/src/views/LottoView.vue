<template>
  <div>
    <h1>로또</h1>
    <button @click="getLuckyNumber">Get Lucky Numbers</button>
    <p>{{ arr }}</p>
  </div>
</template>

<script>
export default {
  name : 'LottoView',
  data () {
    return {
      arr: null
    }
  },
  methods : {
    getLuckyNumber () {
      let rlt = []
      while (rlt.length !== 6) {
        let newNum = Math.floor((Math.random() * 46)+1)
        while (newNum in rlt) {
          newNum = Math.floor((Math.random() * 46)+1)
        }
        rlt.push(newNum)
      }
      this.arr = rlt
    }
  }

}
</script>

<style>

</style>