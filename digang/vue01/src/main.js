// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// eslint-disable-next-line no-unused-vars
import axios from 'axios'
import VueAxios from 'vue-axios'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import ViewUI from 'view-design'
import 'view-design/dist/styles/iview.css'

// eslint-disable-next-line no-unused-vars
import $ from 'jquery'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import * as echarts from 'echarts'
/* 全局css */
import './assets/css/global.css'
import '@/assets/css/sign-in.css'
import '@/assets/css/bootstrap.min.css'

axios.defaults.withCredentials = true// 请求携带cookie
axios.defaults.headers.post['X-CSRFToken'] = 'csrftoken=Leehiv9BFrbIO7MTSw5qu8WcQjzD1U3F; tabstyle=html-tab'// 设置请求头的跨域密匙
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.transformRequest = [function (data) { // 将发送的post参数封装成FROM-DATA，使后端接收
  let ret = ''
  for (let it in data) {
    ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
  }
  return ret
}]
Vue.prototype.$axios = axios
Vue.prototype.$echarts = echarts

Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(VueAxios, axios) // 使用 axios 插件
Vue.use(ViewUI)
// axios发送http请求的目标地址的基础路径

// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
