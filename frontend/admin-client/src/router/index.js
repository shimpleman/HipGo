// frontend/admin-client/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '../views/Dashboard.vue';

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  // 添加更多路由...
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;