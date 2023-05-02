<template>
  <div class="shadow-lg m-auto w-75 h-75">
    <br>
    <h2>예약 페이지</h2>
    <br>
    <h3>시간 선택</h3>
    <!--시간선택-->
    <div class="time-list">
      <div class="time-item" v-for="(time, index) in times" :key="index" @click="toggleSelected(time)">
        <p :class="{ 'selected': selectedTimes.includes(time) }">{{ time }}</p>
      </div>
    </div>
    <!--선택한 시간-->
    <hr>
    <div class="flexbox row">
      <div class="selected-times">
          <h3> 선택 시간 :&nbsp;
          <span v-for="(selectedTime, index) in selectedTimes" :key="index">{{selectedTime}}&nbsp;&nbsp;</span>
          </h3>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TimePicker',
  data: function() {
    return {
      times: [
        "00:00","00:30","01:00","01:30","02:00","02:30","03:00","03:30","04:00","04:30",
        "05:00","05:30","06:00","06:30","07:00","07:30","08:00","08:30",
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectedTimes: []
    }
  },
  methods: {
    toggleSelected(time) {
      if (this.selectedTimes.includes(time)) {
        this.selectedTimes.splice(this.selectedTimes.indexOf(time), 1)
      } else {
        if (this.selectedTimes.length < 5) {
          this.selectedTimes.push(time)
        } else {
          alert('5타임까지만 신청할 수 있습니다')
        }
      }
    }
  }
}
</script>

<style scoped>
.time-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  overflow-x: hidden;
}
.time-item {

  text-align: center;
  flex: 0 0 calc(12.5% - 1rem);
}
.selected {
  background-color: skyblue;
  color: white;
}

</style>
