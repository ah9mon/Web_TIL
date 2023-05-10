<template>
  <div>
    <!-- <p v-if="searching">{{ message }}</p> -->
    <p v-if="!imgSrc">{{ message }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="">
    <br>
    <!-- <h1 v-if="notFound">{{ this.$route.params.breed }}라는 품종은 없습니다</h1> -->


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data () {
    return {
      imgSrc: null,
      notFound: false,
      message : "불러오는중 ",
      searching: true
    }
  },
  methods : {
    getDogImage () {
      
      const breed = this.$route.params.breed
      const dogImageSearchURL = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        method: 'get',
        url: dogImageSearchURL
      })
      .then((response) => {
        // this.searching = false
        console.log('response')
        this.imgSrc = response.data.message
      })
      .catch((error) => {
        // this.searching = false
        // this.message = `${this.$route.params.breed}라는 품종은 없습니다`
        // this.notFound = true
        console.log(error)
        this.$router.push('/404')
      }
      )
    }
  },
  created () {
    this.getDogImage()
  }
}
</script>

<style>

</style>