<template>
<section>
  <SplitedPage>
    <template #right>
      <div style="margin-top: 2rem">
        <div class="question-hint">
          <h3 class="agree" style="margin-left: 35%; margin-right: 12%;"> Strongly disagree </h3>
          <h2 style="font-size: 16px; margin-right: 15%">1-2-3-4-5</h2>
          <h3 class="agree">Strongly agree</h3>
        </div>
        <!-- <form @submit.prevent="submitScore">
        <p>How much do you like basketball? </p>
        <input type="radio" id="1a" name="baskeball" v-model="basketballScore" value="1">
        <label for="1a">1</label>
        <input type="radio" id="2a" name="basketball" v-model="basketballScore" value="2">
        <label for="2a">2</label>
        <input type="radio" id="3a" name="basketball" v-model="basketballScore" value="3">
        <label for="3a">3</label>
        <input type="radio" id="4a" name="basketball" v-model="basketballScore" value="4">
        <label for="4a">4</label>
        <input type="radio" id="5a" name="basketball" v-model="basketballScore" value="5">
        <label for="5a">5</label>

        <br>

        <br>

        <input type="submit" value="Submit"><br>
      </form> -->
      <Panel style="margin-top: 10rem;">
        <div style="display: flex; flex-direction: column;">
          <SingleQuestion v-for="i in questions.length"
          :key="i"
          @selected="(val) => updateScore(i - 1, val)"
          >
            {{ questions[i - 1].q }}
          </SingleQuestion>
          <Button @click = "submitScore">Submit Score</Button>
        </div>
        <br /><br />
      </Panel>
      </div>

    </template>

    <template #left>
      <!-- <aside class="left">
    <h1>Here's a Few Questions to Get You Started...</h1>
  </aside> -->
    </template>
  </SplitedPage>
</section>
</template>

<script>
import SplitedPage from "../components/SplitedPage";
import SingleQuestion from "../components/SingleQuestion";
import fs from "fs";
import axios from "axios";

export default {
  components: { SingleQuestion, SplitedPage },
  watch: {
    results(val) {
      console.log(val);
    }
  },
  data() {
    return {
      questions: [
        {q: "How much do you like Anime?", c: "acg"},
        {q: "How much do you like Basketball?", c: "sports"},
        {q: "How much do you like Hitchcock?", c: "book"},
        



      ],
      results: {},
      scores: []
    };
  },
  methods: {
    submitScore() {
      this.calcResults();
      console.log(this.results);
<<<<<<< HEAD:elbow_bump_frontend/src/pages/Questionnaire.vue
      axios.post(this.$store.getters.URL + "/questionnaire",
      {
        user_id: this.$store.getters.userId,
        scores: this.results
      }).then(
=======
      let form = new FormData();
      
      if (this.$store.getters.userId){
        form.append("user_id", this.$store.getters.userId);
      }else{
        console.error('Not logined.');
        return;
      }

      for (let res in this.results){
        form.append(res, this.results[res]);
      }

      axios.post(this.$store.getters.URL + "/questionnaire", form).then(
>>>>>>> ffe95f22bf7abc221690061cc18587e153d4d801:src/pages/Questionnaire.vue
        (response) => {
          let jsonData = response.data;
          if (jsonData['STATUS_CODE'] == 200){
            this.$router.push('/socialmediainfo');
          }
        }
      );
    },
    updateScore(index, val) {
      this.scores[index] = val;
      console.log(index, val);
    },
    calcResults() {
      let i = 0;
      for (let s in this.scores){
        let cat = this.questions[i].c;
        let score = Number(this.scores[s]);
        if (cat in this.results){
          this.results[cat] += score;
        }else{
          this.results[cat] = score;
          console.warn("There are inconsistent category");
        }
        i++;
      }
      for (let res in this.results){
        this.results[res] /= 5;
      }
    },
    LoadQuestion(url){
      let text = "";
      fs.readFile(url, 'utf8', (err, data) => {
        if(err){
          console.error(err);
        }else{
          text = data;
        }
      });

      let lines = text.split("\n");
      lines.forEach(line => {
          line = line.trim();
          if (':' in line) {
            let parts = line.split(':');
            let qsText = parts[0].trim();
            let cat = parts[1].trim();

            this.question.push({
              q: qsText,
              c: cat
            });

            if (!(cat in this.results)){
              this.results[cat] = Number(0);
            }
          }
      });

    }
  },
};
</script>

<style lang="scss" scoped>

h3.agree{
  font-size: 15px;
}

::v-deep{
  .splited-left{
    width: 30% !important;
  }

  .splited-right{
    width: 70% !important;
  }
}
.question-hint {
  position: absolute;
  display: flex;
  justify-content: space-between;
  margin-bottom: 8rem;
  width: 95%;
}
</style>
