<template>
  <div id="myChart" :style="{width: '100%', height: '700px'}"/>
</template>
<script>

export default {
  name: 'fenxi',
  mounted () {
    this.drawLine()
  },
  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      const myChart = this.$echarts.init(document.getElementById('myChart'))
      myChart.setOption({
        title: {
          text: '各区的租房数量金额对比',
          subtext: '北京市',
          textStyle: {
            fontSize: 23
          },
          subtextStyle: {
            fontSize: 17
          }
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['平均租金(元/月/㎡)', '数量']
        },
        toolbox: {
          show: true,
          feature: {
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        calculable: true,
        dataset: {
          source: [
            ['东城', 282, 144.24],
            ['丰台', 577, 86.5],
            ['大兴', 362, 63.73],
            ['房山', 180, 47.58],
            ['昌平', 347, 70.09],
            ['朝阳', 1597, 121.50],
            ['海淀', 605, 127.24],
            ['西城', 442, 151.77],
            ['通州', 477, 58.33],
            ['顺义', 297, 65.07],
            ['门头沟', 285, 51.75],
            ['石景山', 175, 82.86],
            ['亦庄开发区', 147, 82.42]
          ]
        },
        xAxis: {
          type: 'category',
          splitLine: {
            show: false
          },
          axisLabel: {
            textStyle: {
              fontSize: 13
            }
          }
        },
        yAxis: [
          {
            type: 'value',
            name: '数量',
            splitLine: {
              show: false
            },
            nameLocation: 'middle',
            nameGap: 70
          },
          {
            type: 'value',
            name: '平均租金(元/月/㎡)',
            splitLine: {
              show: false
            },
            nameLocation: 'middle',
            nameGap: 50
          }
        ],
        series: [
          {
            name: '数量',
            type: 'bar',
            color: '#5470C6'
          },

          {
            name: '平均租金(元/月/㎡)',
            type: 'line',
            yAxisIndex: 1,
            color: '#FC8452',
            label: {
              position: [-35, -20],
              show: true,
              fontSize: 14,
              color: '#FC8452'
            }
          }
        ],
        textStyle: {
          fontSize: 18, // 设置字体大小为 14px
          fontFamily: 'Arial, sans-serif', // 设置字体
          fontWeight: 'normal' // 设置字体粗细
        }
      })
    }
  }
}
</script>
<style scoped>

</style>
