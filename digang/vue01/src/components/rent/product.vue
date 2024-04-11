<!--

-->
<template>
    <div class="filter-more">
      <transition name="selectbox">
        <div class="box" v-show="boxshow">
          <Row v-for="(item,index) in filterBox" :key="index" >
            <i-col span="2">{{item.name}}</i-col>
            <i-col span="22">
              <a href="#"
                v-for="(v,i) in item.items"
                :key="i"
                @click="clickrange(index,v,i)"
                class="text-filter"  >
                <span :class="{ isActive:v.active}">{{v.text}}</span>
              </a>
            </i-col>
          </Row>
        </div>
      </transition>
      <div>
        <a href="#" v-for="(item,index) in selectBox" class="text-select" :key="index">
          {{item.text}}
          <i @click="removeCurrentSelect(index)">&times;</i>
        </a>
      </div>
      <p class="text-toggle" @click="togglebox" >{{btnTxt ?'收起选项':'更多选项'}}</p>

      <rent :list="selectrents"></rent>
    </div>
</template>
<script>
import {getRent} from '../../api/api'
import Rent from './rent'

export default {
  name: 'product',
  data () {
    return {
      rents: [
        {garden: '', price: '', id: '', region: '', layout: '', size: '', site: '', img: ''}
      ],
      selectrents: [],
      boxshow: false,
      btnTxt: false,
      selectBox: [],
      selectBox2: [],
      filterBox: [
        {
          name: '城区:',
          items: [
            { value: 1, text: '全部', active: false },
            { value: 2, text: '东城', active: false },
            { value: 3, text: '海淀', active: false },
            { value: 4, text: '朝阳', active: false },
            { value: 5, text: '丰台', active: false },
            { value: 6, text: '大兴', active: false },
            { value: 7, text: '房山', active: false },
            { value: 8, text: '昌平', active: false },
            { value: 9, text: '西城', active: false },
            { value: 10, text: '顺义', active: false },
            { value: 11, text: '通州', active: false },
            { value: 12, text: '门头沟', active: false },
            { value: 13, text: '石景山', active: false },
            { value: 14, text: '亦庄开发区', active: false }
          ]
        },
        {
          name: '面积(㎡):',
          items: [
            { value: 15, text: '全部', active: false },
            { value: 16, text: '1~50', active: false },
            { value: 17, text: '50~70', active: false },
            { value: 18, text: '70~90', active: false },
            { value: 19, text: '90~120', active: false },
            { value: 20, text: '120~160', active: false },
            { value: 21, text: '160~1200', active: false }
          ]
        },
        {
          name: '价格(元/月):',
          items: [
            { value: 22, text: '全部', active: false },
            { value: 23, text: '500-1000', active: false },
            { value: 24, text: '1000-2000', active: false },
            { value: 25, text: '2000-3000', active: false },
            { value: 26, text: '3000-5000', active: false },
            { value: 27, text: '5000-8000', active: false },
            { value: 28, text: '8000-160000', active: false }
          ]
        },
        {
          name: '户型:',
          items: [
            { value: 29, text: '全部', active: false },
            { value: 30, text: '1室', active: false },
            { value: 31, text: '2室', active: false },
            { value: 32, text: '3室', active: false },
            { value: 33, text: '4室', active: false },
            { value: 34, text: '', active: false },
            { value: 35, text: '', active: false }
          ]
        }
      ]
    }
  },
  components: {Rent},
  computed: {
    // 目前没用，但可以看看
    ChooseList () {
      return this.rents.filter((item) => {
        if (this.selectrents.includes(item.id)) {
          return item
        }
      })
    },
    // 过滤四个选项
    listregion () {
      this.pusharr()
      if (this.selectBox2.includes(1)) {
        return this.rents
      } else if (this.selectBox2.includes(2)) {
        return this.rents.filter(function (data) {
          return data.region === '东城'
        })
      } else if (this.selectBox2.includes(3)) {
        return this.rents.filter(function (data) {
          return data.region === '海淀'
        })
      } else if (this.selectBox2.includes(4)) {
        return this.rents.filter(function (data) {
          return data.region === '朝阳'
        })
      } else if (this.selectBox2.includes(5)) {
        return this.rents.filter(function (data) {
          return data.region === '丰台'
        })
      } else if (this.selectBox2.includes(6)) {
        return this.rents.filter(function (data) {
          return data.region === '大兴'
        })
      } else if (this.selectBox2.includes(7)) {
        return this.rents.filter(function (data) {
          return data.region === '房山'
        })
      } else if (this.selectBox2.includes(8)) {
        return this.rents.filter(function (data) {
          return data.region === '昌平'
        })
      } else if (this.selectBox2.includes(9)) {
        return this.rents.filter(function (data) {
          return data.region === '西城'
        })
      } else if (this.selectBox2.includes(10)) {
        return this.rents.filter(function (data) {
          return data.region === '顺义'
        })
      } else if (this.selectBox2.includes(11)) {
        return this.rents.filter(function (data) {
          return data.region === '通州'
        })
      } else if (this.selectBox2.includes(12)) {
        return this.rents.filter(function (data) {
          return data.region === '门头沟'
        })
      } else if (this.selectBox2.includes(13)) {
        return this.rents.filter(function (data) {
          return data.region === '石景山'
        })
      } else if (this.selectBox2.includes(14)) {
        return this.rents.filter(function (data) {
          return data.region === '亦庄开发区'
        })
      } else {
        return this.rents
      }
    },
    listsize () {
      this.pusharr()
      if (this.selectBox2.includes(15)) {
        return this.selectrents
      } else if (this.selectBox2.includes(16)) {
        return this.selectrents.filter(function (data) {
          return data.size < 50
        })
      } else if (this.selectBox2.includes(17)) {
        return this.selectrents.filter(function (data) {
          return data.size < 70 && data.size >= 50
        })
      } else if (this.selectBox2.includes(18)) {
        return this.selectrents.filter(function (data) {
          return data.size < 90 && data.size >= 70
        })
      } else if (this.selectBox2.includes(19)) {
        return this.selectrents.filter(function (data) {
          return data.size < 120 && data.size >= 90
        })
      } else if (this.selectBox2.includes(20)) {
        return this.selectrents.filter(function (data) {
          return data.size < 160 && data.size >= 120
        })
      } else if (this.selectBox2.includes(21)) {
        return this.selectrents.filter(function (data) {
          return data.size < 1200 && data.size >= 160
        })
      } else {
        return this.selectrents
      }
    },
    listprice () {
      this.pusharr()
      if (this.selectBox2.includes(22)) {
        return this.selectrents
      } else if (this.selectBox2.includes(23)) {
        return this.selectrents.filter(function (data) {
          return data.price < 1000
        })
      } else if (this.selectBox2.includes(24)) {
        return this.selectrents.filter(function (data) {
          return data.price < 2000 && data.price >= 1000
        })
      } else if (this.selectBox2.includes(25)) {
        return this.selectrents.filter(function (data) {
          return data.price < 3000 && data.price >= 2000
        })
      } else if (this.selectBox2.includes(26)) {
        return this.selectrents.filter(function (data) {
          return data.price < 5000 && data.price >= 3000
        })
      } else if (this.selectBox2.includes(27)) {
        return this.selectrents.filter(function (data) {
          return data.price < 8000 && data.price >= 5000
        })
      } else if (this.selectBox2.includes(28)) {
        return this.selectrents.filter(function (data) {
          return data.price < 16000 && data.price >= 8000
        })
      } else {
        return this.selectrents
      }
    },
    listlay () {
      this.pusharr()
      if (this.selectBox2.includes(29)) {
        return this.selectrents
      } else if (this.selectBox2.includes(30)) {
        return this.selectrents.filter(function (data) {
          return data.layout === '1室0厅' || data.layout === '1室1厅' || data.layout === '1室1卫'
        })
      } else if (this.selectBox2.includes(31)) {
        return this.selectrents.filter(function (data) {
          return data.layout === '2室1厅' || data.layout === '2室2厅' || data.layout === '2室1卫'
        })
      } else if (this.selectBox2.includes(32)) {
        return this.selectrents.filter(function (data) {
          return data.layout === '3室2厅' || data.layout === '3室1厅' || data.layout === '3室1卫'
        })
      } else if (this.selectBox2.includes(33)) {
        return this.selectrents.filter(function (data) {
          return data.layout === '4室1厅' || data.layout === '4室2厅'
        })
      } else if (this.selectBox2.includes(34)) {
        return this.selectrents
      } else if (this.selectBox2.includes(35)) {
        return this.selectrents
      } else {
        return this.selectrents
      }
    }
  },

  methods: {
    togglebox: function () {
      this.boxshow = !this.boxshow
      this.btnTxt = !this.btnTxt
    },
    clickrange (parentIndex, el, childIndex) {
      const item = this.filterBox[parentIndex].items
      item.filter((v, i) => {
        if (i === childIndex) {
          v.active = !v.active // 选中和反选
          this.selectBox.unshift(v) // 选中的数组
        } else {
          v.active = false // 取消选中
          this.selectBox.filter((childEl, childI) => {
            if (childEl.active === false) {
              this.selectBox.splice(childI, 1) // 反选删除数组中的当前个
            }
          })
        }
      })
      this.loadRent()
    },
    removeCurrentSelect (index) {
      this.filterBox.filter((el, i) => {
        el.items.filter((data, childIndex) => {
          if (data.text === this.selectBox[index].text) {
            data.active = false
          }
        })
      })
      this.selectBox.splice(index, 1)
      this.loadRent()
    },
    loadRent () {
      getRent().then(response => {
        this.rents = response.data
        this.selectrents = this.listregion
        this.selectrents = this.listsize
        this.selectrents = this.listprice
        this.selectrents = this.listlay
      })
    },
    pusharr () {
      this.selectBox2 = []
      this.selectBox.forEach(e => {
        this.selectBox2.push(e.value)
      })
    }
  },
  created () {
    this.loadRent()
    console.log('mounted事件执行！')
  }

}
</script>

<style scoped>
.filter-more {
  width: 90%;
  margin: 0 auto;
  border: 1px solid #e8f4fd;
  padding: 25px 15px;
  font-size: 16px;
}
.box {
  height: 150px;
  overflow: hidden;
}
.text-toggle {
  text-align: center;
  cursor: pointer;
  font-size: 18px;
}
.selectbox-leave-active,
.selectbox-enter-active {
  transition: all 1s ease;
}
.selectbox-leave-active,
.selectbox-enter {
  height: 0px !important;
}
.selectbox-leave,
.selectbox-enter-active {
  height: 150px;
}
.text-filter {
  display: inline-block;
  color: #404040;
  width: 160px;
  span {
    display: inline-block;
    text-align: center;
    width: 100px;
    &:hover {
      border-radius: 50px;
      color: #ffffff;
      animation: myfirst 1s;
      -moz-animation: myfirst 1s; /* Firefox */
      -webkit-animation: myfirst 1s; /* Safari and Chrome */
      -o-animation: myfirst 1s; /* Opera */
      animation-fill-mode: forwards;
    }
  }
}
.text-select {
  display: inline-block;
  padding: 0px 5px;
  border: 1px solid #268edb;
  border-radius: 40px;
  color: #268edb;
  font-size: 18px;
  margin-right: 20px;
  i {
    display: inline-block;
    height: 100%;
    font-size: 15px;
    padding: 0px 5px;
  }
}
.isActive {
  background-color: #2989dd;
  border-radius: 40px;
  color: #ffffff;
}
@keyframes myfirst {
  from {
    background: #ffffff;
  }
  to {
    background: #2989dd;
  }
}
</style>
