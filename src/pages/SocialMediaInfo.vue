<template>
  <Card>
    <template #header>
      <div class="heading">
        <h1>Please share your Twitter username with us</h1>
      </div>
    </template>
    <template #content>
      <form @submit.prevent="submitUsername">
        <label for="twitterUsername">Twitter @</label>
        <input
          type="text"
          id="twitterUsername"
          name="twitterUsername"
          v-model="twitterUsername"
        />
        <br /><br />
        <Button type="submit">Submit</Button> <br /><br />
        <Dialog v-model:visible="hasErrors" header="Oh no!" class="error">
          {{ error }} <br/><br/>
          <Button label="Got it!" autofocus @click="removeErrors"></Button>
        </Dialog>
      </form>
    </template>
  </Card>
</template>

<script>
import Dialog from "primevue/dialog";
import axios from "axios";

export default {
  components: { Dialog },
  data() {
    return {
      twitterUsername: "",
      error: "",
    };
  },
  computed: {
    hasErrors: function() {
      return this.error !== "";
    },
  },
  methods: {
    submitUsername() {
      let localURL = `${this.$store.getters.localURL}/social_media_info`;
      axios
        .post(localURL, {
          params: {
            id: this.$store.getters.userId,
            twitter: this.twitterUsername,
          },
        })
        .then((res) => {
          if (res.data.STATUS_CODE == 200) {
            this.$router.push("/matches");
          } else {
            this.error = res.data.Message;
          }
        })
        .catch((err) => {
          console.log(err);
        });
      this.twitterUsername = "";
      this.$router.push('/matches')
    },
    removeErrors() {
      this.error = ""
    }
  },
};
</script>

<style scoped>
.heading {
  margin-top: 9rem;
  text-align: center;
  padding-top: 1px;
}
</style>
