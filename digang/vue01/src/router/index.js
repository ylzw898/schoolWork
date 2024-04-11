/*
import rent from '../components/rent/rent'
import pay from '../components/pay/pay'
 ,
    {
      path: '/rent',
      name: 'rent',
      component: rent
    },
    {
      path: '/pay',
      name: 'pay',
      component: pay
    }
*/
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import login from '../components/login'
import signup from '../components/signup'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/signup',
      name: 'signup',
      component: signup
    }
  ]
})
