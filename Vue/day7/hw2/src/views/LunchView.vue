<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p>{{ this.todayFood }}</p>
    <br>
    <br>
    <h1>로또나 뽑아볼까</h1>
    <button @click="goToLotto">Get Lucky Numbers</button>
  </div>
</template>

<script>
export default {
  name: 'LunchView',
  data () {
    return {
      foods : {
        0 : '라면',
        1 : '치킨',
        2 : '피자',
        3 : '햄버거',
        4 : '국밥',
        5 : '오늘은 굶으세요'
      },
      todayFood : null,
    }
  },
  methods : {
    pickLunch() {
      let keyNum = Math.floor(Math.random() * 6)
      console.log(keyNum)
      console.log(this.foods[keyNum])
      this.todayFood = this.foods[keyNum]
    },
    goToLotto () {
      this.$router.push({name:'lotto'})
    }
  }

}
</script>

<style>

</style>