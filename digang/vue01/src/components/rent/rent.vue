 <!--
    <ul v-for="(item,index) in rents" :key="item" v-if="index<5">
     <li class="item">
       <div class="img_box"><img v-bind:src="item.img" alt=""></div>
       <p v-html="item.garden"></p>
       <span :style="{color:'red'}">&yen;{{item.price}}</span>
     </li>
   </ul>
 -->

<template>
 <div id="app">
   <div class="d-grid gap-2 col-6 mx-auto">
      <button class="btn btn-primary btn-lg" type="button" @click="getTabelData">刷新</button>
   </div>
   <br><br>
   <el-table :data="tableData" style="font-size: 18px; width: 100%">
     <el-table-column prop="img" label="图片" min-width="20%" >
       <template   slot-scope="scope">
         <img :src="scope.row.img"  width="186" height="140" />
       </template>
      </el-table-column>
     <el-table-column prop="region" label="城区" min-width="10%"></el-table-column>
     <el-table-column prop="garden" label="小区" min-width="20%"></el-table-column>
     <el-table-column prop="layout" label="布局" min-width="10%"></el-table-column>
     <el-table-column prop="size" label="面积(㎡)" min-width="10%"></el-table-column>
     <el-table-column prop="price" label="价格(元/月)" min-width="15%" ></el-table-column>
     <el-table-column prop="phone" label="联系电话" min-width="15%" ></el-table-column>
   </el-table>

   <el-pagination
     @size-change="sizeChange"
     @current-change="currentChange"
     :current-page="page"
     :page-size="size"
     :page-sizes="pageSizes"
     layout="total, sizes, prev, pager, next, jumper"
     :total="total">
   </el-pagination>
   <p>
     <br><el-button type="primary" size="small" @click="scrollToTop">返回顶部</el-button><br>
   </p>
 </div>
</template>

<script>
export default {
  name: 'rent',
  props: ['list'],
  data () {
    return {
      page: 1, // 第几页
      size: 10, // 一页多少条
      total: 0, // 总条目数
      pageSizes: [10, 20, 50], // 可选择的一页多少条
      tableData: [] // 表格绑定的数据
    }
  },
  created () {
    this.$nextTick(function () {
      this.getTabelData()
    })
  },

  methods: {
    scrollToTop () {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // 平滑滚动
      })
    },
    // 获取表格数据，自行分页（splice）
    getTabelData () {
      console.log('getTableData')
      // allData为全部数据
      this.tableData = this.list.slice(
        (this.page - 1) * this.size,
        this.page * this.size
      )
      this.total = this.list.length
    },
    // page改变时的回调函数，参数为当前页码
    currentChange (val) {
      console.log('翻页，当前为第几页', val)
      this.page = val
      this.getTabelData()
    },
    // size改变时回调的函数，参数为当前的size
    sizeChange (val) {
      this.getTabelData()
      this.size = val
      this.page = 1
      console.log('sizeChange', val)
    }

  }

}
</script>

<style scoped>
 * {
            margin: 0;
            padding: 0;
            list-style: none;
        }
body {
            background: #e3e4e5;
            margin: auto;
        }

#app {
            margin-left: auto;
            margin-right: auto;
            overflow: hidden;
        }

.item {
  float: left;
  width: 190px;
  height: 266px;
  margin: 0 5px 8px;
  text-align: center;
  background: #fff;
}
.item. img_box {
            width: 150px;
            height: 150px;
            margin: 30px auto;
        }
.img_box img {
            width: 100%;
            height: 100%;
        }

.item p {
            font-size: 12px;
            line-height: 20px;
            height: 40px;
            padding: 0 10px;
            /* white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis; */
            display: -webkit-box;
            overflow: hidden;
            text-overflow: ellipsis;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
        }
.more2_info_self {
            background-color: #e1251b;
            border-radius: 2px;
            color: #fff;
            padding: 0 5px;
            margin-right: 4px;
            line-height: 16px;
            height: 16px;
            font-size: 12px;
            font-style: normal;
        }

</style>
