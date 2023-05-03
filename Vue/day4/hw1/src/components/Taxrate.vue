<template>
  <div>
    <div>
      <h2>산출세액 : {{ IncomeDeduction }}</h2>
      <h2>세액감면 : (-) {{ taxReduction }} </h2>
      <hr>
    </div>

    <Finaltax 
    :tax-reduction = 'this.taxReduction'
    :income-deduction = 'IncomeDeduction'
    />
  </div>
</template>

<script>
import Finaltax from '@/components/Finaltax.vue'

export default {
  name:"Taxrate",
  components: {
    Finaltax,
  },
  props: {
    taxBase: Number,
    taxReduction: Number,
  },
  computed: {
    IncomeDeduction: function (){
      if (this.taxBase <= 1200) {
        return Math.round(this.taxBase * 0.06)
      } else if (1200 < this.taxBase <= 4600) {
        return Math.round(this.taxBase * 0.15 - 108)
      } else if (4600 < this.taxBase <= 8800) {
        return Math.round(this.taxBase * 0.24 - 522)
      } else if (8800 < this.taxBase <= 15000 ) {
        return Math.round(this.taxBase * 0.35 - 1490)
      } else if (15000 < this.taxBase <= 30000) {
        return Math.round(this.taxBase * 0.38 - 1940)
      } else if (30000 < this.taxBase <= 50000) {
        return Math.round(this.taxBase * 0.40 - 2540)
      } else if (50000 < this.taxBase <= 100000) {
        return Math.round(this.taxBase * 0.42 - 3540)
      } else {
        return Math.round(this.taxBase * 0.45 - 6540)
      }
    }, 
  }
}
</script>

<style>

</style>