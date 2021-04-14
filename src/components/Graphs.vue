<template>
  <div>
    <Chart class='chart' type="radar" :data="chartData" />
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      chartData: {},
    };
  },
  mounted() {
    let that = this;
    axios
      .get(this.$store.getters.URL + "get_all_interests", {
        params: { user_id: that.$store.getters.userId },
      })
      .then((res) => {
        var data = res.data.Data;
        var labels = data.map((i) => i["cat"]);
        that.chartData["labels"] = labels;
        var weights = data.map((i) => i["weight"]);
        that.chartData["datasets"] = [{
          label: "Interest Weights",
          backgroundColor: "rgba(179,181,198,0.2)",
          borderColor: "rgba(179,181,198,1)",
          pointBackgroundColor: "rgba(179,181,198,1)",
          pointBorderColor: "#fff",
          pointHoverBackgroundColor: "#fff",
          pointHoverBorderColor: "rgba(179,181,198,1)",
          data: weights,
        }];
      });
    this.$forceUpdate();
  },
};
</script>

<style scoped>
.chart {
    margin-top: 50px
}
</style>
