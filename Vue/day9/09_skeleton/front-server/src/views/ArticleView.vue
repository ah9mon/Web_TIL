<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{name : 'CreateView'}">[Create]</router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue';

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
  },
  created() {
    this.getAticles()
  },
  methods: {
    getAticles(){
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>

</style>
