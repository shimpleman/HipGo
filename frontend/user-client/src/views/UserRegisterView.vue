<template>
  <div class="register-container">
    <h2>注册</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <input type="text" v-model="username" placeholder="请输入用户名" required />
      </div>
      <div class="form-group">
        <input type="email" v-model="email" placeholder="请输入邮箱" required />
      </div>
      <div class="form-group">
        <input type="password" v-model="password" placeholder="请输入密码" required />
      </div>
      <div class="form-group">
        <input type="password" v-model="confirmPassword" placeholder="确认密码" required />
      </div>
      <button type="submit">注册</button>
      <a href="#" @click.prevent="switchToLogin">登录</a>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    handleRegister() {
      if (!this.username) {
        this.$toast('请输入用户名');
        return;
      }
      if (!this.email) {
        this.$toast('请输入邮箱');
        return;
      }
      if (!this.password) {
        this.$toast('请输入密码');
        return;
      }
      if (this.password !== this.confirmPassword) {
        this.$toast('两次密码输入不一致');
        return;
      }
      // API 注册请求
      console.log('注册信息：', {
        username: this.username,
        email: this.email,
        password: this.password
      });
    },
    switchToLogin() {
      this.$router.push({ name: 'Login' });
    }
  }
};
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
}
.form-group {
  margin-bottom: 15px;
}
.form-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>