<template>
  <div>
    <!--input-->
    <div>
      <span>연봉 입력 (만원):
        <input v-model.number="Salary" type="number" >
      </span>
      <br>
      <br>
      <span>세액감면액 (만원):
        <input v-model.number="taxReduction" type="number" >
      </span>
      <hr>
    </div>
    <!--종합 소득 관련-->
    <div>
      <h2>종합소득금액 : {{ Salary }} 만원</h2>
      <h2>종합소득공제 : (-) 150 만원</h2>
      <h2>과세표준 : {{ taxBase }}</h2>
      <hr>
    </div>
    <!--세금 관련-->
    <!--과세표준, 세액감면액 prop-->
    <Taxrate 
    :tax-base="taxBase"
    :tax-reduction="taxReduction"
    />

  </div>
</template>

<script>
import Taxrate from '@/components/Taxrate.vue'

export default {
  name:"Income",
  components : {
    Taxrate,
  },
  data: function () {
    return {
      Salary:null,
      taxReduction:null,
    }
  },
  computed: {
    taxBase () {
      if (this.Salary - 150 < 0) {
        return 0
      } else {
        return this.Salary - 150
      }
    }
    ,
  }

}
</script>

<style>

</style>