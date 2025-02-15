<template>
  <div class="pc-nav">
    <ul>
      <li>首页</li>
      <li>博客</li>
      <li>视频博客</li>
      <li>小说</li>
      <li>商店</li>
      <li>关于</li>
      <li class="auth">
        <button @click="toggleLoginModal">{{ isAuth ? '退出登录' : '登录' }}</button>
      </li>
    </ul>
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
.pc-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #fff;
}
.pc-nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}
.pc-nav li {
  margin: 0 15px;
}
.auth button {
  padding: 5px 10px;
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 5px;
}
</style>