<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> | <!--a Tag 같은 기능 -> url 이동시킴-->
      <router-link to="/about">About</router-link> |

      <router-link :to="{name : 'home'}">Home</router-link> | <!--a Tag 같은 기능 -> url 이동시킴-->
      <router-link :to="{name : 'about'}">About</router-link> |
      <router-link :to="{name : 'hello', params: {userName: 'eom'}}">Hello</router-link> <!--직접 params 넘길수도있음-->

    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
