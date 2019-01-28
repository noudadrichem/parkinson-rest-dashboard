<template>
  <div id="app" class="container">
    <div class="row">
      <div class="zeventig col trillingen">
        <Trillingen :labols="trillingen.labels" :datavalues="trillingen.data"/>
      </div>
      <div class="dertig col activities">
        <Activities :labols="activities.labels" :datavalues="activities.data"/>
      </div>
    </div>

    <div class="row">
      <div class="dertig col">
        <Patient :patient="patient" />
      </div>

      <div class="zeventig col">
        <Dampening :labols="dampening.labels" :datavalues="dampening.data"/>
      </div>
    </div>
  </div>
</template>

<script>
const URL = 'http://nontwikkel.nl:9094'
import axios from 'axios'

import Trillingen from './components/Trillingen.vue'
import Activities from './components/Activities.vue'
import Dampening from './components/Dampening.vue'
import Patient from './components/Patient.vue'

export default {
  name: 'root',
  data: () => ({
    trillingen: {
      data: null,
      labels: null
    },
    activities: {
      labels: ['liggen', 'staan'],
      data: []
    },
    dampening: {
      labels: [],
      data: []
    },
    patient: {}
  }),
  components: {
    Trillingen,
    Activities,
    Dampening,
    Patient
  },
  methods: {
    fetchData() {
      axios.all([
        axios.get(`${URL}/measurements`),
        axios.get(`${URL}/activities`),
        axios.get(`${URL}/dampening`),
        axios.get(`${URL}/patient`),
      ])
      .then(axios.spread(
        (measurements, activities, dampening, patient) => {
          const activis = activities.data.activities
          this.updateActivityChart(activities.data.activities)
          this.updateTrillingenChart(measurements.data.measurements)
          this.updateDampeningChart(dampening.data.dampening)
          this.$set(this, 'patient', patient.data.patients[0])
        }
      ))
    },

    updateTrillingenChart(messes) {
      console.log('updateTrillingenChart', messes)
      const SHOW = 10

      const mesChartData = messes
        .slice(Math.max(messes.length - SHOW, 1))
        .map(mes => mes.aantaltrillingen)

      const newLabels = messes
        .slice(Math.max(messes.length - SHOW, 1 ))
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

      const procent = (wat,waarvan) => (wat / activities.length) * 100
      console.log({
        stajewelCount,
        stajenietCount,
        stajewelPercent: procent(stajenietCount, stajewelCount),
        stajenietPercent: procent(stajewelCount, stajenietCount)
      })

      if(stajewelCount > stajenietCount) {
        const stajewelPercent = procent(stajenietCount, stajewelCount)
        console.log({ stajewelPercent })
        this.$set(this.activities.data, 0, (stajewelPercent))
        this.$set(this.activities.data, 1, (100 - stajewelPercent))
      } else {
        const stajenietPercent = procent(stajewelCount, stajenietCount)
        console.log({ stajenietPercent})
        this.$set(this.activities.data, 1, stajenietPercent)
        this.$set(this.activities.data, 0, (100 - stajenietPercent))
      }
    },

    updateDampeningChart(dampenings) {
      const damps = dampenings.map(d => d.luchtvochtigheid)
      const newLabels = dampenings
        .slice(Math.max(dampenings.length - 10, 1 ))
        .map(mes => new Date(parseInt(mes.created)).toString())
        .map(dateString => dateString.split(' ')[4])

      this.$set(this.dampening, 'data', damps)
      this.$set(this.dampening, 'labels', newLabels)
    }
  },
  mounted() {
    this.fetchData()
    const SEC = 5
    window.setInterval(this.fetchData, (SEC * 1000))
  }
}
</script>
