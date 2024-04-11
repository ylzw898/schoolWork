 <!--
  <div>
    <h1>社区</h1>
    <ul>
      <li v-for="(book, index) in books" :key="index" style="display:block">
        {{index}}-{{book.comments}}-{{book.author}}
      </li>
    </ul>

    <form action="">
      输入评论：<input type="text" placeholder="book name" v-model="inputBook.name"><br>
      输入作者：<input type="text" placeholder="book author" v-model="inputBook.author"><br>
    </form>
    <button type="submit" @click="bookSubmit()">submit</button>
  </div>
 -->

<template>
<div id="app" class="container">
      <div class="py-5 text-center">
      <p class="lead text-left">在这个功能模块中，您可以畅所欲言，我们将立即显示您的评论，以表明我们对评论没有任何的干预。</p>
    </div>
        <div class="row g-5 text-left">
            <div class="form-group">
                <label for="">留言人</label>
                <input type="text" name="" id="" class="form-control" v-model="inputBook.author">
            </div>
            <div class="form-group">
                <label for="">留言内容</label>
                <input type="text" name="" id="" class="form-control" v-model="inputBook.name">
            </div>
            <div class="form-group">
                <input type="button" value="发送留言" class="btn btn-primary" @click="bookSubmit()">
            </div>
        </div>
  <div>
    <ol class="list-group list-group-numbered">
    <li class="list-group-item d-flex justify-content-between align-items-start" v-for="item in books" :key="item.id">
      <div class="ms-2 me-auto" style="text-align: left">
        <div class="fw-bold">{{item.author}}:</div>
        {{item.comments}}
      </div>
      <span class="badge bg-primary rounded-pill"></span>
    </li>
  </ol>
  </div>

</div>
</template>

<script>
import {getBooks, postBook} from '../../api/api'

export default {
  name: 'shequ',
  data () {
    return {
      active: 'rent',
      books: [
        {comments: '', author: '', id: new Date()}
      ],
      inputBook: {
        'name': '',
        'author': ''
      }
    }
  },
  methods: {
    loadBooks () {
      getBooks().then(response => {
        this.books = response.data
      })
    }, // load books list when visit the page
    bookSubmit () {
      if (this.inputBook.author === '') {
        this.$message({
          message: '警告哦，用户名不能为空',
          type: 'warning'
        })
      }
      if (this.inputBook.name === '') {
        this.$message({
          message: '警告哦，评论不能为空',
          type: 'warning'
        })
      }
      postBook(this.inputBook.name, this.inputBook.author).then(response => {
        console.log(response)
        this.$message({
          message: '恭喜你，提交评论成功',
          type: 'success'
        })
        this.loadBooks()
      })
    }, // add a book to backend when click the button
    makeActive: function (item) {
      this.active = item
    }
  },
  created: function () {
    this.loadBooks()
  }
}
</script>

<style scoped>
  .container {
    max-width: 100%;
    display: grid;
    place-items: center;
  }
  li {
  width: 700px;
}
</style>
