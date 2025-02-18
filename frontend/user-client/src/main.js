// import { createApp } from 'vue'
// import App from './App.vue'
//
// createApp(App).mount('#app')


// frontend/user-client/src/main.js
import { createApp } from 'vue';
import App from './App.vue';
// 引入全局样式文件
import './assets/css/global.css';
import router from './router';
import store from './store';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

const app = createApp(App);

app.use(router);
app.use(store);
app.use(ElementPlus);

app.mount('#app');
