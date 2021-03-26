<template>
<section>
  <SplitedPage>
    <template #right>
      <div style="margin-top: 12rem">
        <div class="question-hint">
          <!-- <h3 class="agree" style="margin-left: 35%; margin-right: 12%;"> Strongly disagree </h3>
          <h2 style="font-size: 16px; margin-right: 15%">1-2-3-4-5</h2>
          <h3 class="agree">Strongly agree</h3> -->
          <h3 class="agree">Pick a category of questions you would like to answer:</h3>
        </div>
      
        <h3 style="font-size:15px; text-align:center;">Strongly Agree 1 - 2 - 3 - 4 - 5 Strongly Disagree</h3>
      
      <Panel style="margin-top: 0rem;">
        <div style="display: flex; flex-direction: column;">
          <!-- Buttons to display questions from the questions.txt bank based on their category -->
          <!-- <div class="topic-buttons">
            <div class = "divider"/>
            <Button @click = "LoadQuestion('music')" style="background-color: #75c9deff;">Music</Button>
            <div class ="divider"/>
            <Button @click = "LoadQuestion('sports')" style="background-color: #75c9deff;">Sport</Button>
            <div class ="divider"/>
            <Button @click = "LoadQuestion('films/tv')" style="background-color: #75c9deff;">Film/TV</Button>
            <div class ="divider"/>
            <Button @click = "LoadQuestion('video games')" style="background-color: #75c9deff;">Video Games</Button>
          </div> -->

          <Accordion>
            <AccordionTab v-for="(qsList, cate) in questions" :key="cate" :header="cate">
              <SingleQuestion v-for="i in qsList.length"
              :key="i"
              @selected="(val) => updateScore(cate, i - 1, val)"
              >
                {{ qsList[i - 1] }}
              </SingleQuestion>
            </AccordionTab>
          </Accordion>
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
import axios from "axios";
import question_bank from "raw-loader!../assets/questions.txt";
//!!!! You may have to run npm i -D raw-loader before this page

export default {
  components: { SingleQuestion, SplitedPage },
  watch: {
    results(val) {
      // console.log(val);
    }
  },
  data() {
    return {
      question_bank: "../assets/questions.txt",
      questions: {},
      results: {},
      scores: []
    };
  },
  methods: {
    submitScore() {
      this.calcResults();
      let form = new FormData();
      // console.log(this.results)
      
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
        (response) => {
          let jsonData = response.data;
          if (jsonData['STATUS_CODE'] == 200){
            this.$router.push('/socialmediainfo');
          }
        }
      );
    },
    updateScore(category, index, val) {
      this.scores[category][index] = val;
    },
    calcResults() {
      for (const cat in this.scores){
        if (this.scores[cat].length == 0) {
          continue;
        }
        let sum = 0;
        let len = this.scores[cat].length;
        this.scores[cat].forEach((score) => sum += score)
        this.results[cat] = sum/(5*len)
      }
    },
    LoadQuestion(){
      let text = "";
      text = question_bank;
      this.questions = {};

      let lines = text.split("\n");
      for (let line in lines) {
          line = lines[line].trim();
          if (line.includes(":")) {
            let parts = line.split(':');
            let qsText = parts[0].trim();
            let cat = parts[1].trim();

            if (!(cat in this.questions)){
              this.questions[cat] = [qsText];
              this.scores[cat] = [];
            }else{
              this.questions[cat].push(qsText);
            }

            // //load all music related questions
            // if(category == "music" && cat == "music"){
            //   this.questions.push({
            //     q: qsText,
            //     c: cat
            //   })
            // }
            // //load all sport questions
            // if(category == "sports" && cat == "sports"){
            //   this.questions.push({
            //     q: qsText,
            //     c: cat
            //   })
            // }
            // //load all film/tv related questions
            // if(category == "films/tv" && cat == "films/tv"){
            //   this.questions.push({
            //     q: qsText,
            //     c: cat
            //   })
            // }
            // //load all video games questions
            // if(category == "video games" && cat == "video games"){
            //   this.questions.push({
            //     q: qsText,
            //     c: cat
            //   })
            // }
          }
      }
    }
  },
  mounted: function(){
    this.LoadQuestion();
  }
};
</script>

<style lang="scss" scoped>

h3.agree{
  font-size: 15px;
  margin-left: 30%;
  position: absolute;
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

.topic-buttons{
  text-align:center;
  font-size: 12px;
  padding: 10px 10px;
}

.divider{
  width:5px;
  height:auto;
  display:inline-block;
}
</style>
