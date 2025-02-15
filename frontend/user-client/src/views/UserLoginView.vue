<template>
  <div class="login-container">
    <h2>登录</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <input type="text" v-model="username" placeholder="请输入用户名/邮箱" required />
        <p v-if="usernameError" class="error-message">{{ usernameError }}</p>
      </div>
      <div class="form-group">
        <input type="password" v-model="password" placeholder="请输入密码" required />
        <p v-if="passwordError" class="error-message">{{ passwordError }}</p>
      </div>
      <div class="form-group">
        <input type="text" v-model="captcha" placeholder="请输入验证码" required />
        <span>{{ captchaText }}</span>
      </div>
      <button type="submit">登录</button>
      <a href="#" @click.prevent="switchToRegister">注册</a>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      captcha: '',
      captchaText: 'F F V 1',
      usernameError: '',
      passwordError: '',
      maxAttempts: 5,
      attempts: 0
    };
  },
  computed: {
    isCaptchaCorrect() {
      return this.captcha === 'F F V 1';
    }
  },
  methods: {
    handleLogin() {
     if (!this.username) {
        this.usernameError = '请输入用户名';
        return;
      }
      if (!this.password) {
        this.passwordError = '请输入密码';
        return;
      }
      if (!this.isCaptchaCorrect) {
        alert('验证码错误');
        return;
      }
      // API 登录请求
      this.attempts++;
      if (this.attempts > this.maxAttempts) {
        alert('尝试次数过多，请稍后再试');
        return;
      }
      // 调用 API 登录
      console.log('登录信息：', { username: this.username, password: this.password });
    },
    switchToRegister() {
      this.$router.push({ name: 'Register' });
    }
  }
};
</script>

<style scoped>
.login-container {
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
.error-message {
  color: red;
  font-size: 12px;
}
</style>