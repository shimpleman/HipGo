// frontend/user-client/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import UserLoginView from '../views/UserLoginView.vue';
import UserRegisterView from '../views/UserRegisterView.vue';
import HomePage from '../views/HomePage.vue';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: UserLoginView
  },
  {
    path: '/register',
    name: 'Register',
    component: UserRegisterView
  },
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  // 添加更多路由...
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;