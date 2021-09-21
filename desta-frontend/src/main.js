// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueRouter from "vue-router";
import * as VueGoogleMaps from "vue2-google-maps"

import './index.css'

Vue.config.productionTip = false
Vue.use(VueRouter)

Vue.use(VueGoogleMaps, {
  load: {
    key: "insert_api_key",
    libraries: "places"
  }
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
