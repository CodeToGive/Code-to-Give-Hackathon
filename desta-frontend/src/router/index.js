import Vue from 'vue'
import Router from 'vue-router'
import CloseBy from '@/pages/CloseBy'
import Registration from '../router/Registration'
import Profile from '../router/Profile'
import Login from '../router/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path : '/',
      component : CloseBy
    },
    {
      path: '/registration',
      component : Registration
    },
    {
      path: '/profile',
      component : Profile
    },
    {
      path: '/login',
      component : Login
    }
  ]
})
