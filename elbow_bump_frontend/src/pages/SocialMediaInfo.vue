
<template>
<div class="heading">
  <h1>Please share your Twitter username with us</h1>
</div>
<form @submit.prevent="submitUsername">
  <label for="twitterUsername">Twitter   @</label>
  <input type="text" id="twitterUsername" name="twitterUsername" v-model="twitterUsername"> <br><br>
  <input type="submit" value="Submit"> <br><br>
</form>
</template>

<script>
export default {
  data() {
    return {
      twitterUsername: ""
    };
  },
  methods: {
    submitUsername() {
      console.log(this.twitterUsername);
      this.twitterUsername = "";
    },
  },
};
</script>
