<template>
  <div id="myChart" :style="{width: '100%', height: '700px'}" />
</template>
<script>

export default {
  name: 'house',
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
          data: ['金额(万元/㎡)', '数量']
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
            ['东城', 871, 9.74],
            ['丰台', 1743, 5.74],
            ['大兴', 1093, 4.64],
            ['房山', 674, 3.51],
            ['昌平', 1422, 4.13],
            ['朝阳', 1777, 7.17],
            ['海淀', 1796, 8.67],
            ['西城', 1152, 10.61],
            ['通州', 957, 4.55],
            ['顺义', 488, 4.15],
            ['门头沟', 304, 4.04],
            ['石景山', 451, 5.73],
            ['亦庄开发区', 255, 5.03]
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
            name: '金额(万元/㎡)',
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
            name: '金额(万元/㎡)',
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
