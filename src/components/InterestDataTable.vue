<template>
    <div>
        <Chart class="chart" type="radar" :data="data()" />
        <br><br><br><br><br>
        <p>Data: {{dat}}</p>

        <ul id="example-1">
            <li v-for="item in dat" :key="item.uid_interest_type">
                {{ dat.uid_interest_type }}
                {{ dat.uid_interest_weight }}
            </li>
        </ul>

    </div>
</template>


<script>
import axios from "axios";
// import datatale from ""
export default {
    data(){
        return {dat:[]}
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
      });
    }
}
</script>
