import Vue from 'vue'
import Router from 'vue-router'
import CloseBy from '@/pages/CloseBy'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path : '/',
      component : CloseBy
    }
  ]
})
