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
  width: 1920px; /* 设置导航栏宽度为1920px */
  height: 125px; /* 设置导航栏高度为125px */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: linear-gradient(to right, #6a1b9a, #4a148c); /* 深紫渐变色 */
  color: #fff; /* 文字颜色为白色，方便显示 */
}
.logo {
  width: 40px;
}
</style>