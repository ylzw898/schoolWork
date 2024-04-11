 <!--

 -->

<template>
  <div class="hello">
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand" href="#" v-on:click="makeActive('shequ')">社区</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-center" id="mynavbar"> <!-- 将这里的class改为justify-content-center -->
      <ul class="navbar-nav">
        <li class="nav-item">
          <a href="#" class="navbar-brand" v-on:click="makeActive('rent')">租房中心</a>
        </li>
        <li class="nav-item">
          <a href="#" class="navbar-brand" v-on:click="makeActive('pay')">买房中心</a>
        </li>
        <li class="nav-item">
          <a href="#" class="navbar-brand" v-on:click="makeActive('log')">个人中心</a>
        </li>
      </ul>
    </div>
    <div class="text-end" v-if="!showname">
      <router-link to="/login">
        <button type="button" class="btn btn-warning">登录</button>
      </router-link>
      <router-link to="/signup">
        <button type="button" class="btn btn-warning">注册</button>
      </router-link>
    </div>
  </div>
</nav>

    <div v-if="active === 'rent'">
      <br><br><product/>
      <br><br><text1/>
    </div>
    <div v-else-if="active === 'pay'">
      <br><br><pay/>
    </div>
    <div v-else-if="active === 'shequ'">
      <br><br><shequ/>
    </div>
    <div v-else>
      <div v-if="!showname">
        <br><br><log/>
      </div>
      <div v-if="showname">
        <br><br><pc/>
      </div>
    </div>

  </div>
</template>

<script>
import Product from './rent/product'
import pay from './pay/pay'
import log from './person/log'
import pc from './person/pc'
import shequ from './shequ/shequ'

export default {
  name: 'HelloWorld',
  components: {Product, pay, log, shequ, pc},
  data () {
    return {
      active: 'rent',
      filterList: [],
      getFilterSelData: [],
      showname: false
    }
  },
  methods: {
    makeActive: function (item) {
      this.active = item
    }
  },
  created: function () {
    this.showname = this.$route.query.message
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

</style>
