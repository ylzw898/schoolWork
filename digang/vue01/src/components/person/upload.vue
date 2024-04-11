 <!--
 -->
<template>
<div class="container">
  <main>
    <div class="py-5 text-center">
      <h2>上传房产信息</h2>
      <p class="lead text-left">在这一功能模块，你可以自由填写自己的房产信息。我们会将您的房产信息先储存到后台，经过审核后再发表到网站上。在提交信息后，如果未搜索到自己的房产项目，请耐心等待一至三天。若长时间未搜索到自己提交的信息，请联系后台人员。</p>
    </div>
    <hr>
    <div class="row g-5 text-left">
        <form class="needs-validation" novalidate>

          <h4 class="mb-3">必填信息</h4>

          <div class="row g-3">

            <div class="col-md-4">
              <label for="state" class="form-label">上架形式</label>
              <select class="form-select" id="state" required v-model="input.Site">
                <option value="">请选择上架方式</option>
                <option value="rent">出租</option>
                <option value="sales">售卖</option>
              </select>
            </div>

            <div class="col-4">
              <label for="price" class="form-label">价格 <span class="text-muted">(月租或者房间总价)</span></label>
              <input type="text" class="form-control" id="price" placeholder="3000" v-model="input.Price">
            </div>

            <div class="col-4">
              <label for="size" class="form-label">面积</label>
              <input type="text" class="form-control" id="size" placeholder="64" required v-model="input.Size">
            </div>

            <div class="col-2">
              <label for="region" class="form-label">城区</label>
              <input type="text" class="form-control" id="region" placeholder="东城" required v-model="input.Region">
            </div>

            <div class="col-10">
              <label for="place" class="form-label">小区名称 <span class="text-muted">(Optional)</span></label>
              <input type="text" class="form-control" id="place" placeholder="天通苑" v-model="input.Garden">
            </div>

            <div class="col-md-4">
              <label for="name" class="form-label">联系人</label>
              <input type="text" class="form-control" id="name" placeholder="张先生" required v-model="input.Name">
              <small class="text-muted">仅作为联系时使用</small>
            </div>

            <div class="col-md-8">
              <label for="number" class="form-label">电话号码</label>
              <input type="text" class="form-control" id="number" placeholder="186xxxxxxxx" required v-model="input.Phone">
            </div>

          </div>

          <hr class="my-4">

          <h4 class="mb-3">其他信息</h4>

          <div class="col-12">
              <div class="input-group has-validation">
                <el-input type="textarea" :rows="5" placeholder="请输入其他信息" v-model="input.Other"></el-input>
              </div>
          </div>

          <br><br>

          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="same-address">
            <label class="form-check-label" for="same-address">支持看房服务</label>
          </div>

          <hr class="my-4">
          <button class="w-100 btn btn-primary btn-lg" type="submit" @click="open2">提交信息</button>

        </form>
    </div>
  </main>

  <footer class="my-5 pt-5 text-muted text-center text-small">
    <p class="mb-1">&copy; 2017–2024</p>
  </footer>
</div>
</template>

<script>
import {getCheck, postCheck} from '../../api/api'

export default {
  name: 'upload',
  data () {
    return {
      check: [
        {region: '', garden: '', name: '', size: '', price: '', site: '', img: '', other: '', id: '', phone: ''}
      ],
      input: {
        'id': '',
        'Region': '',
        'Garden': '',
        'Name': '',
        'Size': '',
        'Price': '',
        'Site': '',
        'Img': '',
        'Other': '',
        'Phone': ''
      }
    }
  },
  methods: {
    load () {
      getCheck().then(response => {
        this.check = response.data
        console.log(response.data)
      })
    }, // load books list when visit the page
    open2 () {
      if (this.input.Price === '') {
        this.$message({
          message: '警告哦，价格不能为空',
          type: 'warning'
        })
        return
      }
      if (this.input.Size === '') {
        this.$message({
          message: '警告哦，面积不能为空',
          type: 'warning'
        })
        return
      }
      if (this.input.Region === '') {
        this.$message({
          message: '警告哦，城区不能为空',
          type: 'warning'
        })
        return
      }
      if (this.input.Garden === '') {
        this.$message({
          message: '警告哦，小区不能为空',
          type: 'warning'
        })
        return
      }
      if (this.input.Name === '') {
        this.$message({
          message: '警告哦，联系人不能为空',
          type: 'warning'
        })
        return
      }
      if (this.input.Phone === '') {
        this.$message({
          message: '警告哦，电话不能为空',
          type: 'warning'
        })
        return
      }
      this.$confirm('是否确认提交?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        // 在确认按钮被点击时调用 Submit() 方法
        this.Submit()
        this.$message({
          type: 'success',
          message: '已成功提交'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消提交'
        })
      })
    },
    Submit () {
      postCheck(this.input.id, this.input.Region, this.input.Garden, this.input.Name, this.input.Size, this.input.Price, this.input.Site, this.input.Img, this.input.Other, this.input.Phone).then(response => {
        console.log(response)
        this.load()
      })
    } // add a book to backend when click the button
  },
  created: function () {
    this.load()
  }
}
</script>

<style scoped>

  @media (min-width: 768px) {
    .bd-placeholder-img-lg {
      font-size: 3.5rem;
    }
  }

  .nav-scroller .nav {
    display: flex;
    flex-wrap: nowrap;
    padding-bottom: 1rem;
    margin-top: -1px;
    overflow-x: auto;
    text-align: center;
    white-space: nowrap;
    -webkit-overflow-scrolling: touch;
  }

  .container {
    max-width: 960px;
  }

</style>
