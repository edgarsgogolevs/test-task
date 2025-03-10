import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(router);

import Vue3Toastify, { type ToastContainerOptions } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

app.use(Vue3Toastify, {
  autoClose: 3000,
} as ToastContainerOptions);

app.mount('#app');
