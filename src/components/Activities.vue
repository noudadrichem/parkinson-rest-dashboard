<script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  name: 'Activities',
  props: ['labols', 'datavalues'],
  methods: {
    renderDan() {
      this.renderChart({
        labels: this.labols,
        datasets: [{
            label: 'Activities',
            data: this.datavalues,
            borderColor: '#1a7feb',
            backgroundColor: '#1a7feb',
          }]
      }, {
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        scales: {
          yAxes: [{
            ticks: {
              suggestedMax: 100,
              callback: v => `${v}%`
          },
          scaleLabel: {
              display: true,
              labelString: "Percentage"
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
