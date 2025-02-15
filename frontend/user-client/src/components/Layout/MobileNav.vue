<template>
  <div class="mobile-nav">
    <img src="logo.png" alt="Logo" class="logo" />
    <button @click="toggleLoginModal">{{ isAuth ? '退出登录' : '登录' }}</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isAuth: false
    };
  },
  methods: {
    toggleLoginModal() {
      this.$emit('toggle-login-modal');
    }
  }
};
</script>

<style scoped>
.mobile-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #fff;
}
.logo {
  width: 40px;
}
</style>