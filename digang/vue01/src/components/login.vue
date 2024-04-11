 <!--
打包     npm run build
启动前端  npm run dev
<template>
    <div id="login">
    <div style="text-align: center; font-size: larger;">
        <div>欢迎光临</div>
        <div>请输入您的账户</div>
    </div>
    <div>
      <form action="/index/" method="post">
        <input v-model="loginfo.username" type="text" placeholder="请输入用户名">
        <input v-model="loginfo.password" type="password" placeholder="请输入密码">
    </form>
        <input v-on:click="login()" value="登录" />
        <div style="height: 5px;"></div>
        <div>
          <div style="height: 9px;"></div>
          <a href="/#/signup" style="color:black ;text-decoration:none">注册</a>
        </div>
    </div>
</div>
</template>

 -->
<template>
  <div>
    <el-card class="box-card">
      <h2>登录</h2>
      <el-form
        :model="loginfo"
        status-icon
        :rules="rules"
        ref="loginfo"
        label-position="left"
        label-width="70px"
        class="login-from">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="loginfo.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            type="password"
            v-model="loginfo.password"
            autocomplete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div class="btnGroup">
        <el-button type="primary" @click="login()">登录</el-button>
        <el-button @click="resetForm('loginfo')">重置</el-button>
        <router-link to="/signup">
          <el-button style="margin-left:10px">注册</el-button>
        </router-link>
      </div>
    </el-card>
  </div>
</template>

<script>

export default {
  name: 'login',
  data () {
    return {
      loginfo: {
        'username': '',
        'password': ''
      }}
  },
  methods: {
    login () {
      if (this.loginfo.username === '') {
        this.$message({
          message: '警告哦，用户名不能为空',
          type: 'warning'
        })
        return
      }
      if (this.loginfo.password === '') {
        this.$message({
          message: '警告哦，密码不能为空',
          type: 'warning'
        })
        return
      }
      this.$axios.get('/getcsrf/').then(res => {
        var csrftoken = res.data.csrftoken
        this.$axios.post(
          '/login/', // 向loginn发送请求，验证密码是否正确
          {'name': this.loginfo.username,
            'password': this.loginfo.password
          }, {
            headers: {
              'X-CSRFToken': csrftoken
            }
          }
        ).then(res => {
          if (res.data.loginstatus === 1) // loginstatus为后端返回的数据，
          // eslint-disable-next-line brace-style
          {
            this.$router.push({ // 页面跳转到登录成功界面
              path: '/',
              query: {message: true, username: this.loginfo.username}
            })
          } else if (res.data.loginstatus === 2) {
            alert('账号未注册')
          } else {
            alert('密码错误')
          }
        })
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }

}
</script>

<style scoped>
.box-card {
  margin: auto auto;
  width: 400px;
}
.login-from {
  margin: auto auto;
}
</style>
