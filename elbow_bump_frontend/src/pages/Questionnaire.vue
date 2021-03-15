<template>
  <Card>
    <template #header>
      <div class="heading">
        <h2>Strongly disagree 1-2-3-4-5 Strongly agree</h2>
      </div>
    </template>
    <template #content>
      <form @submit.prevent="submitScore" class="questionnaire">
        <p>How much do you like basketball?</p>
        <input
          type="radio"
          id="1a"
          name="baskeball"
          v-model="basketballScore"
          value="1"
        />
        <label for="1a">1</label>
        <input
          type="radio"
          id="2a"
          name="basketball"
          v-model="basketballScore"
          value="2"
        />
        <label for="2a">2</label>
        <input
          type="radio"
          id="3a"
          name="basketball"
          v-model="basketballScore"
          value="3"
        />
        <label for="3a">3</label>
        <input
          type="radio"
          id="4a"
          name="basketball"
          v-model="basketballScore"
          value="4"
        />
        <label for="4a">4</label>
        <input
          type="radio"
          id="5a"
          name="basketball"
          v-model="basketballScore"
          value="5"
        />
        <label for="5a">5</label>
        <br />
        <br />
        <Button type="submit">Submit</Button><br />
      </form>
      <br /><br />
    </template>
  </Card>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      basketballScore: 0,
    };
  },
  methods: {
    submitScore() {
      let localURL = `${this.$store.getters.localURL}/questionnaire?user_id=${this.$store.getters.userId}&basketballScore=${this.basketballScore}`;
      axios
        .post(localURL)
        .then((res) => {
          if (res.data.STATUS_CODE == 200) {
            this.$router.push("/socialmediainfo");
          }
        })
        .catch((err) => {
          console.log(err);
        });
      this.basketballScore = "";
    },
  },
};
</script>

<style scoped>
.questionnaire {
  display: block;
  padding-left: 2rem;
  margin-top: 5.5rem;
  margin-left: 5rem;
  top: 20%;
  bottom: 10%;
  width: 40rem;
  height: 15rem;
  z-index: 2;
}
.heading {
  margin-top: 9rem;
  text-align: center;
  padding-top: 1px;
}
</style>
