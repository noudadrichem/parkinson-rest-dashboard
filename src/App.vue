<template>
  <div id="app" class="container">
    <div class="row">
      <div class="8 col trillingen">
        <Trillingen :labols="trillingen.labels" :datavalues="trillingen.data"/>
      </div>
      <div class="3 col activities">
        <Activities :labols="activities.labels" :datavalues="activities.data"/>
      </div>
    </div>

  </div>
</template>

<script>
const URL = 'http://localhost:5000'
import Trillingen from './components/Trillingen.vue'
import Activities from './components/Activities.vue'
import axios from 'axios'

export default {
  name: 'root',
  data: () => ({
    trillingen: {
      data: null,
      labels: null
    },
    activities: {
      labels: ['staan', 'liggen'],
      data: []
    }
  }),
  components: {
    Trillingen,
    Activities
  },
  methods: {
    fetchData() {
      axios.all([
        axios.get(`${URL}/measurements`),
        axios.get(`${URL}/activities`)
      ])
      .then(axios.spread(
        (measurements, activities) => {
          const activis = activities.data.activities
          this.updateActivityChart(activities.data.activities)
          this.updateTrillingenChart(measurements.data.measurements)
        }
      ))
    },
    updateTrillingenChart(messes) {
      console.log('updateTrillingenChart', messes)
      // const oldLabels = this.trillingen.labels
      // const oldData = this.trillingen.datasets[0].data
      // oldLabels.shift()

      const mesChartData = messes.map(mes => mes.aantaltrillingen)
      const newLabels = messes
        .map(mes => new Date(parseInt(mes.created)).toString())
        .map(dateString => dateString.split(' ')[4])

      this.$set(this.trillingen, 'labels', newLabels)
      this.$set(this.trillingen, 'data', mesChartData)
    },
    updateActivityChart(activities) {
      console.log('updateActivityChart', activities)
      const stajewel = activities.filter(ac => ac.staje)
      const stajeniet = activities.filter(ac => !ac.staje)
      const stajewelCount = stajewel.length
      const stajenietCount = stajeniet.length



      if(stajewelCount > stajenietCount) {
        const stajewelPercent = (stajenietCount / stajewelCount) * 100
        this.$set(this.activities.data, 0, (stajewelPercent))
        this.$set(this.activities.data, 1, (100 - stajewelPercent))
      } else {
        const stajenietPercent = (stajewelCount / stajenietCount) * 100

        this.$set(this.activities.data, 1, (stajenietPercent))
        this.$set(this.activities.data, 0, (100 - stajenietPercent))
      }
    }
  },
  mounted() {
    // this.fetchData()
    window.setInterval(this.fetchData, 5000)
  }
}
</script>

<style>
#app {
  font-family: 'Open Sans', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.container {
  max-width: 1184px;
  padding: 8px 24px;
  width: 100%;
  margin-left: auto;
  margin: auto;
}
</style>
