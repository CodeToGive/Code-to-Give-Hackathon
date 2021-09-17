import Vue from 'vue'
import VueRouter from 'vue-router';
import App from './App.vue'
import Profile from './components/Profile.vue'
import Home from './components/Home.vue'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueRouter);

Vue.config.productionTip = false

const routes = [
    { path: '/user', component: Profile},
    { path: '/', component: Home},
];

const router = new VueRouter({
  routes
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
