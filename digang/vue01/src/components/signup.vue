 <!--
打包     npm run build
启动前端  npm run dev

 -->
<template>
  <div>
    <el-card class="box-card">
      <h2>注册</h2>
      <el-form
        :model="loginForm"
        status-icon
        :rules="rules"
        ref="loginForm"
        label-position="left"
        label-width="80px"
        class="demo-ruleForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="loginForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass">
          <el-input
            type="password"
            v-model="loginForm.pass"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="password">
          <el-input
            type="password"
            v-model="loginForm.password"
            autocomplete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div class="btnGroup">
        <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
        <el-button @click="resetForm('loginForm')">重置</el-button>
        <el-button @click="goBack">返回</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.loginForm.checkPass !== '') {
          this.$refs.loginForm.validateField('checkPass')
        }
        callback()
      }
    }
    const validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.loginForm.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: '',
        pass: '',
        password: ''
      },
      rules: {
        username: [
          { required: true, message: '用户名不能为空！', trigger: 'blur' }
        ],
        pass: [{ required: true, validator: validatePass, trigger: 'blur' }],
        password: [
          { required: true, validator: validatePass2, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm () {
      if (this.loginForm.username === '') {
        this.$message({
          message: '警告哦，用户名不能为空',
          type: 'warning'
        })
        return
      }
      if (this.loginForm.password === '') {
        this.$message({
          message: '警告哦，密码不能为空',
          type: 'warning'
        })
        return
      }
      if (this.loginForm.password !== this.loginForm.pass) {
        this.$message({
          message: '警告哦，两次密码不一致',
          type: 'warning'
        })
        return
      }
      this.$axios
        .post(
          '/regster/', // 后端执行注册的url
          {'name': this.loginForm.username, // 用户名
            'password': this.loginForm.password // 密码
          }
        ).then((res) => {
          if (res.data.codestatus === 1) {
            alert('注册成功')
            this.$router.push({ // 前往登录界面
              path: './'
            })
          } else {
            alert('用户已创建')
          }
        // eslint-disable-next-line handle-callback-err
        }).catch((err) => {
          alert('注册失败，请更换用户名')
        })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    goBack () {
      this.$router.go(-1)
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
