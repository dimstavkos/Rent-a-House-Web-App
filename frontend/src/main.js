import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
// import * as Vue from 'vue' // in Vue 3
import axios from "axios";
import VueAxios from "vue-axios";

// Nucleo Icons
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";

import materialKit from "./material-kit";

const app = createApp(App);

axios.interceptors.response.use(
  (response) => response,
  (error) => {
    console.log(error);
    alert('Error: ' + error.response.data.detail);
    return error.response;
  }
);

app.use(createPinia());
app.use(router);
app.use(materialKit);
app.use(VueAxios, axios);
app.provide("axios", app.config.globalProperties.axios);
app.mount("#app");

console.clear();
