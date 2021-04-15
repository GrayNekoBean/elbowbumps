<template>
  <div>
    <Chart class="chart" type="radar" :data="chartData" />
    <Chart
    v-if=hasTwitter
      class="chart"
      type="radar"
      :data="twitterChartData"
    />
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      chartData: {},
      twitterChartData: {},
      hasTwitter: false
    };
  },
  mounted() {
    let that = this;
    axios
      .get(this.$store.getters.URL + "get_all_interests", {
        params: { user_id: this.$store.getters.userId },
      })
      .then((res) => {
        var data = res.data.Data.overall;
        var labels = data.map((i) => i["cat"]);
        that.chartData["labels"] = labels;
        var weights = data.map((i) => i["weight"]);
        that.chartData["datasets"] = [
          {
            label: "Interest Scores",
            backgroundColor: "rgba(179,181,198,0.2)",
            borderColor: "rgba(179,181,198,1)",
            pointBackgroundColor: "rgba(179,181,198,1)",
            pointBorderColor: "#fff",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(179,181,198,1)",
            pointLabelFontColor: '#000',
            data: weights,
          },
        ];
        var twitterData = res.data.Data.twitter;
        if (twitterData.length > 0) { 
            that.chartData['datasets'].push( {
            label: "Twitter Sentiment Analysis",
            backgroundColor: "rgba(255,99,132,0.2)",
            borderColor: "rgba(255,99,132,1)",
            pointBackgroundColor: "rgba(255,99,132,1)",
            pointBorderColor: "#fff",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(255,99,132,1)",
            data: twitterData.map((i) => i['weight']),
          })
        }
        that.$forceUpdate();
      });
  },
};
</script>

<style scoped>
.chart {
}
</style>
