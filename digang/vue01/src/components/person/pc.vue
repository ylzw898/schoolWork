<template>
  <div>
    <nav class="nav justify-content-center">
      <a class="nav-link active" aria-current="page" v-on:click="makeActive('rent')" style="font-size: 24px">租房</a>
      <a class="nav-link" v-on:click="makeActive('house')" style="font-size: 24px">买房</a>
      <a class="nav-link" v-on:click="makeActive('upload')" style="font-size: 24px">上传</a>
      <a class="nav-link" v-on:click="makeActive('gm')" style="font-size: 24px">政策</a>
    </nav>
    <br><br><br>
    <div v-if="active === 'rent'">
      <fenxi/>
    </div>
    <div v-else-if="active === 'house'">
      <house/>
    </div>
    <div v-else-if="active === 'upload'">
      <upload/>
    </div>
    <div v-else>
      <zhengce/>
    </div>
  </div>
</template>

<script>
import fenxi from './fenxi'
import house from './house'
import upload from './upload'
import zhengce from './zhengce'

export default {
  name: 'pc',
  components: {fenxi, house, upload, zhengce},
  data () {
    return {
      active: 'rent'
    }
  },
  methods: {
    makeActive: function (item) {
      this.active = item
    }
  }
}
</script>

<style scoped>

</style>
