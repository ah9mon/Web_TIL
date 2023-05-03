<template>
  <div>
    <h2>결정세액 : {{ incomeDeduction - taxReduction }}</h2>
  </div>
</template>

<script>
export default {
  name:'Finaltax',
  props: {
    taxReduction : Number,
    incomeDeduction : Number,
  }

}
</script>

<style>

</style>