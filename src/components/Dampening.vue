<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  name: 'Dampenings',
  props: ['labols', 'datavalues'],
  methods: {
    renderDan() {
      console.log('renderdan')
      this.renderChart({
        labels: this.labols,
        datasets: [
          {
            label: 'Luchtvochtigheid',
            data: this.datavalues,
            borderColor: '#1a7feb',
            backgroundColor: 'rgba(0,0,0,0)',
          }
        ]
      }, {
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        backgroundColor: null,
        scales: {
          yAxes: [{
            ticks: {
              min: 0,
              max: 100,
              beginAtZero: true,
              stepSize: 5
            }
          }]
        }
      })
    }
  },
  watch: {
    datavalues(neww, old) {
      console.log('trilling props updated ', neww, old)
      this.renderDan()
    }
  },
  mounted() {
    this.renderDan()
  }
}
</script>
