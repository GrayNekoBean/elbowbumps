<template>
  <div>
    <Chart class="chart" type="radar" :data="chartData" />
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
        params: { user_id: this.$store.getters.userId },
      })
      .then((res) => {
        var data = res.data.Data.overall;
        var labels = data.map((i) => i["cat"]);
        let zeros = 0;
        if (labels.length < 4) {
          var main_cats = ['films/tv', 'sports', 'music', 'video games']
          for (const label of labels) {
            if (main_cats.includes(label)) {
              main_cats = main_cats.filter((i) => i != label)
            }
          }
          zeros = main_cats.length
          labels = labels.concat(main_cats)
        }
        that.chartData["labels"] = labels;
        var weights = data.map((i) => i["weight"]);
        weights = weights.concat(Array(zeros).fill(0))
        that.chartData["datasets"] = [
          {
            label: "Questionnaire Scores",
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
        that.$forceUpdate();
        var twitterData = res.data.Data.twitter;
        console.log(twitterData)
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
