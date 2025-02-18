<template>
  <div class="pc-nav">
    <img src="@/assets/doggie.png" alt="Logo" class="logo">
    <video class="logo hipgo-logo" autoplay muted loop playsinline>
      <source src="@/assets/hipgo.mp4" type="video/mp4">
      您的浏览器不支持播放该视频。
    </video>
    <ul>
      <li>Home</li>
      <li>Blog</li>
      <li>Vlog</li>
      <li>Novel</li>
      <li>Shop</li>
      <li>About</li>
    </ul>
    <div class="auth">
      <button class="register-btn" @click="toggleRegisterModal">Register</button>
      <button @click="toggleLoginModal">{{ isAuth ? 'Logout' : 'Login' }}</button>
    </div>
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
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.pc-nav {
  width: 100%;
  max-width: 1920px;
  height: auto;
  display: flex;
  align-items: center;
  padding: 1rem 5%; /* 使用百分比设置左右内边距，保证左右有合适间隔 */
  //background: linear-gradient(to right, #65318e, #4a148c);
  background: #65318e;
  color: #fff;
  white-space: nowrap;
}

.logo {
  max-height: 10rem; /* 设置 logo 最大高度 */
  max-width: 30%; /* 限制 logo 最大宽度占比 */
  height: auto;
  margin-right: 1%; /* 使用百分比设置 logo 与页签的间距 */
  object-fit: contain; /* 保证内容适应容器 */
}

.hipgo-logo {
  max-height: 10rem; /* 设置 logo 最大高度 */
  max-width: 30%; /* 限制 logo 最大宽度占比 */
  height: auto;
  margin-right: 2%; /* 使用百分比设置 logo 与页签的间距 */
}

.pc-nav ul {
  display: flex;
  list-style: none;
  margin: 0 auto; /* 让页签列表居中 */
  padding: 0;
}

@font-face {
  font-family: 'CustomFont';
  src: url('@/assets/Pacifico-Regular.ttf') format('truetype');
}

.pc-nav li {
  margin: 0 1.5rem;
  font-family: 'CustomFont', sans-serif;
  font-size: 1.8rem;
  font-weight: bold;
  font-style: italic;
  color: #fff;
  text-decoration: none;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  transition: all 0.3s ease;
  padding: 0.5rem 0;
  display: flex;
  align-items: center;
}

.auth {
  margin-left: auto; /* 让按钮靠右 */
  display: flex; /* 让按钮水平排列 */
  gap: 10px; /* 设置按钮之间的间距 */
  flex-shrink: 0; /* 防止按钮被压缩 */
}

.auth button {
  padding: 0.6rem 1.2rem; /* 适当增大初始按钮内边距 */
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 5px;
  font-size: 1.1rem; /* 适当增大初始按钮字体大小 */
  transition: all 0.3s ease; /* 添加过渡效果，使变化更平滑 */
}

.auth .register-btn {
  background-color: #fff; /* 白底 */
  color: #000; /* 黑字 */
}

/* 媒体查询，根据不同分辨率调整样式 */
@media (min-width: 769px) {
  .auth {
    margin-left: 25%;
  }
}

@media (max-width: 1280px) {
  .pc-nav {
    padding: 1rem 3%;
  }

  .pc-nav li {
    margin: 0 1rem;
    font-size: 1.2rem;
  }

  .logo,
  .hipgo-logo {
    max-height: 5rem;
    max-width: 25%;
  }

  .auth {
    margin-right: 3%;
  }

  .auth button {
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 1200px) {
  .pc-nav li {
    margin: 0 1rem;
    font-size: 1rem;
    padding: 0.5rem 0;
  }

  .logo {
    max-height: 3rem;
    margin-right: 1.5%;
  }

  .auth button {
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 912px) {
  .pc-nav {
    padding: 1rem 2%;
  }

  .pc-nav li {
    margin: 0 0.8rem;
    font-size: 1rem;
  }

  .logo,
  .hipgo-logo {
    max-height: 4rem;
    max-width: 20%;
  }

  .auth {
    margin-right: 2%;
  }

  .auth button {
    padding: 0.3rem 0.6rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 882px) {
  .pc-nav {
    padding: 1rem 2%;
  }

  .pc-nav li {
    margin: 0 0.75rem;
    font-size: 0.95rem;
  }

  .logo,
  .hipgo-logo {
    max-height: 3.8rem;
    max-width: 22%;
  }

  .auth {
    margin-right: 2%;
  }

  .auth button {
    padding: 0.3rem 0.6rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 853px) {
  .pc-nav {
    padding: 1rem 2%;
  }

  .pc-nav li {
    margin: 0 0.7rem;
    font-size: 0.9rem;
  }

  .logo,
  .hipgo-logo {
    max-height: 3.5rem;
    max-width: 20%;
  }

  .auth {
    margin-right: 2%;
  }

  .auth button {
    padding: 0.3rem 0.6rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 820px) {
  .pc-nav {
    padding: 1rem 2%;
  }

  .pc-nav li {
    margin: 0 0.7rem;
    font-size: 0.9rem;
  }

  .logo,
  .hipgo-logo {
    max-height: 3.5rem;
    max-width: 20%;
  }

  .auth {
    margin-right: 2%;
  }

  .auth button {
    padding: 0.3rem 0.6rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 768px) {
  .pc-nav {
    padding: 1rem 3%;
    white-space: normal;
  }

  .pc-nav li {
    margin: 0 0.6rem;
    font-size: 0.8rem;
    padding: 0.5rem 0;
  }

  .logo {
    max-height: 2.5rem;
    max-width: 25%;
    margin-right: 1%;
  }

  .auth button {
    padding: 0.3rem 0.6rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .pc-nav {
    padding: 1rem 3%;
    white-space: normal;
  }

  .pc-nav li {
    margin: 0 0.3rem;
    font-size: 0.7rem;
    padding: 0.5rem 0;
  }

  .logo {
    max-height: 2rem;
    margin-right: 0.8%;
  }

  .auth button {
    padding: 0.2rem 0.4rem;
    font-size: 0.7rem;
  }
}

@media (max-width: 414px) {
  .pc-nav {
    padding: 1rem 1.5%;
    white-space: normal;
  }

  .pc-nav li {
    margin: 0 0.25rem;
    font-size: 0.65rem;
    padding: 0.5rem 0;
  }

  .logo,
  .hipgo-logo {
    max-height: 2.2rem;
    max-width: 22%;
  }

  .auth {
    margin-right: 1.5%;
  }

  .auth button {
    padding: 0.2rem 0.4rem;
    font-size: 0.65rem;
  }
}

@media (max-width: 390px) {
  .pc-nav {
    padding: 1rem 1%;
    white-space: normal;
  }

  .pc-nav li {
    margin: 0 0.2rem;
    font-size: 0.6rem;
    padding: 0.5rem 0;
  }

  .logo,
  .hipgo-logo {
    max-height: 2.5rem;
    max-width: 25%;
  }

  .auth {
    margin-right: 1%;
  }

  .auth button {
    padding: 0.2rem 0.4rem;
    font-size: 0.6rem;
  }
}

@media (max-width: 375px) {
  .pc-nav {
    padding: 1rem 2%;
    white-space: normal;
  }

  .pc-nav li {
    margin: 0 0.2rem;
    font-size: 0.6rem;
    padding: 0.5rem 0;
  }

  .logo {
    max-height: 1.8rem;
    margin-right: 0.5%;
  }

  .auth button {
    padding: 0.15rem 0.3rem;
    font-size: 0.6rem;
  }
}

@media (max-width: 360px) {
  .pc-nav {
    padding: 1rem 2%;
    white-space: normal;
  }

  .pc-nav li {
    margin: 0 0.2rem;
    font-size: 0.6rem;
    padding: 0.5rem 0;
  }

  .logo {
    max-height: 1.8rem;
    margin-right: 0.4%;
  }

  .auth button {
    padding: 0.15rem 0.3rem;
    font-size: 0.6rem;
  }
}

@media (max-width: 344px) {
  .pc-nav {
    padding: 1rem 2%;
    white-space: normal;
  }

  .pc-nav li {
    margin: 0 0.2rem;
    font-size: 0.6rem;
    padding: 0.5rem 0;
  }

  .logo {
    max-height: 1.8rem;
    margin-right: 0.3%;
  }

  .auth button {
    padding: 0.15rem 0.3rem;
    font-size: 0.6rem;
  }
}
</style>