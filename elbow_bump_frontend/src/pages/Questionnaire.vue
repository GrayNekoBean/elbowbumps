<template>
      <p1>Strongly disagree 1-2-3-4-5 Strongly agree</p1>
      <form @submit.prevent="submitScore">
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
      </form>
      <br><br>


  <aside class="left">
    <h1>Here's a Few Questions to Get You Started...</h1>


  </aside>
</template>

<script>
export default {
  data() {
    return {
      basketballScore: ""
    };
  },
  methods: {
    submitScore() {
      console.log(this.basketballScore);
      this.basketballScore = "";
    },
  },
};
</script>
