<template>
  <div id="app">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap" rel="stylesheet">
    <h1>SSAFY TUBE</h1>
    <iframe v-if="GuadiansOfGalaxy" :src="GuadiansOfGalaxy" frameborder="0" width="640" height="360"></iframe>
    <h2 v-if="GuadiansOfGalaxy">{{ this.GuadiansOfGalaxyTitle }}</h2>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  // key : AIzaSyB-3iWRQvFtsPXBCjx-uridlruzRFFxhng
  name: 'App',
  data () {
    return {
      GuadiansOfGalaxy:null,
      GuadiansOfGalaxyTitle:null
    }
  },
  methods : {
    getYoutube() {
      const youtubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=가디언즈오브갤럭시volume3예고편&key=AIzaSyB-3iWRQvFtsPXBCjx-uridlruzRFFxhng'
      axios({
        method: 'get',
        url: youtubeUrl
      })
      .then((response)=>{
   
        this.GuadiansOfGalaxy = `http://www.youtube.com/embed/${response.data.items[0].id.videoId}`
        this.GuadiansOfGalaxyTitle = response.data.items[0].snippet.title
      })
      .catch((error)=> {
        console.log(error)
        console.log('왜안돼')
      })
    }
  },
  created () {
    this.getYoutube()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
