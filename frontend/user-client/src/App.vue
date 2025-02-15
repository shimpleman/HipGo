<!--<template>-->
<!--  <img alt="Vue logo" src="./assets/logo.png">-->
<!--  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--</template>-->

<!--<script>-->
<!--import HelloWorld from './components/HelloWorld.vue'-->

<!--export default {-->
<!--  name: 'App',-->
<!--  components: {-->
<!--    HelloWorld-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--#app {-->
<!--  font-family: Avenir, Helvetica, Arial, sans-serif;-->
<!--  -webkit-font-smoothing: antialiased;-->
<!--  -moz-osx-font-smoothing: grayscale;-->
<!--  text-align: center;-->
<!--  color: #2c3e50;-->
<!--  margin-top: 60px;-->
<!--}-->
<!--</style>-->

<template>
  <div id="app">
    <MobileNav v-if="isMobile" @toggle-login-modal="toggleLoginModal" />
    <PcNav v-else @toggle-login-modal="toggleLoginModal" />
    <LoginModal v-if="isLoginModal" @close="closeLoginModal" />
    <router-view/>
  </div>
</template>

<script>
import MobileNav from './components/Layout/MobileNav.vue';
import PcNav from './components/Layout/PcNav.vue';
import LoginModal from './components/LoginModal.vue';

export default {
  components: {
    MobileNav,
    PcNav,
    LoginModal
  },
  data() {
    return {
      isLoginModal: false,
      isMobile: window.innerWidth < 768 // 简单判断是否为移动端
    };
  },
  methods: {
    toggleLoginModal() {
      this.isLoginModal = !this.isLoginModal;
    },
    closeLoginModal() {
      this.isLoginModal = false;
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  --text-color: #2c3e50;
  --check-color: #42b983;
  color: var(--text-color);
  margin: 0;
}
</style>