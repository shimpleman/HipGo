<!-- frontend/user-client/src/components/LoginModal.vue -->
<template>
  <div class="login-modal" v-if="isVisible">
    <div class="modal-overlay" @click="closeModal"></div>
    <div class="modal-content">
      <button class="close-btn" @click="closeModal">×</button>
      <router-link :to="{ name: 'Login' }">
        <div class="modal-tab login">登录</div>
      </router-link>
      <router-link :to="{ name: 'Register' }">
        <div class="modal-tab register">注册</div>
      </router-link>
      <component :is="currentTab" :key="currentTab"/>
    </div>
  </div>
</template>

<script>
import Login from '../views/UserLoginView.vue';
import Register from '../views/UserRegisterView.vue';

export default {
  components: {
    Login,
    Register
  },
  props: {
    isVisible: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    currentTab() {
      return this.isVisible ? this.isVisible ? 'Login' : 'Register' : null;
    }
  },
  methods: {
    closeModal() {
      this.$emit('close');
    }
  }
};
</script>

<style scoped>
.login-modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0, 0.5);
}
.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}
.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
}
.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
}
.modal-tab {
  cursor: pointer;
  padding: 10px;
}
.modal-tab.login {
  font-weight: bold;
}
</style>