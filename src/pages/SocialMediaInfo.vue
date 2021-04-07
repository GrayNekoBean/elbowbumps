<template>
  <div id="frame">
    <img id="twitter-icon" src="../assets/twitter.png">
    <Card class = "social-card">
      <template #header>
        <div class="heading">
          <h1>Please authorise your Twitter account with us</h1>
        </div>
      </template>
      <template #content>
          <p>{{generateURL()}}</p>
          <h2>Enter the PIN you recieved above</h2>
          <div id ="textbox">
            <form @submit.prevent="submitPIN">
              <label for="twitterPIN"></label>
              <input
                type="text"
                id="twitterPIN"
                name="twitterPIN"
                v-model="twitterPIN" 
                value @click="getValue"
              />
              <br /><br />
              <div id="button"><Button type="submit" id="button">Submit</Button></div> <br /><br />
              <Dialog v-model:visible="hasErrors" header="Oh no!" class="error">
                {{ error }} <br/><br/>
                <Button label="Got it!" autofocus @click="removeErrors"></Button>
              </Dialog>
            </form>
          </div>
      </template>
    </Card>
  </div>
</template>

<script>
import Dialog from "primevue/dialog";
import axios from "axios";
import twitter from "../pages/Profile.vue";

export default {
  components: { Dialog },
  data() {
    return {
      twitterPIN: "",
      error: "",
      oauthToken: "",
      oauthTokenSecret: "",
      oauthURL: ""
    };
  },
  computed: {
    hasErrors: function() {
      return this.error !== "";
    },
  },
  methods: {
    submitPIN() {
      let localURL = `${this.$store.getters.URL}/social_media_info`;

      const form = new FormData()

      form.append('id', this.$store.getters.userId)
      form.append('OAUTH_TOKEN', this.oauthToken)
      form.append('OAUTH_TOKEN_SECRET', this.oauthTokenSecret)
      form.append('pin', this.twitterPIN)
      axios
        .post(localURL, form)
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
    },
    generateURL() {
      if (this.oauthURL == ""){
      let localURL = `${this.$store.getters.URL}/twitter_oauth_url`;
      axios
      .post(localURL)
      .then((res) => {
        if (res.data.STATUS_CODE == 200) {
          this.oauthURL = res.data.oauthURL;
          this.oauthToken = res.data.oauthToken;
          this.oauthTokenSecret = res.data.oauthTokenSecret;   
        } else {
          this.error = res.data.Message;
        }
      })
      .catch((err) => {
        console.log(err);
      });}
      return this.oauthURL;
    },
    getValue() {
      //this.twitterUsername= "elbowbumps";
      if (twitter == '[object Object]'){
        this.twitterUsername = '';
      }else{
        this.twitterUsername = twitter;
      }
    }
  },
};
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato&family=Open+Sans&display=swap');


.heading {
  margin-top: 20px;
  text-align: center;
  padding-top: 1px;
}

#frame {
  position: absolute;
  height: 100%;
  width: 100%;
  background: #ffffff; 
}

#textbox {
  position: center;
  height: 10000px;
  width: 700px;
  font-size: 40px;
  left: 500px;
  margin-left:5%;
  margin-top: 200px;
}


#twitterUsername {
  height: 60px;
  width: 500px;
  font-size: 30px;
}

#twitter-icon {
  padding: 1%;
  border: 1%;
  margin-left:20%;
  margin-top: 7.5%;
  margin-bottom:7.5%;
  height: 450px;
  left: 100px;
  width: 450px;
}

.social-card{
    position: absolute;
    display: block;
    top: 50%;
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    padding-left: 1rem;
    margin-left: 5rem;
    right: 300px;
    width: 40rem; 
    height: 45rem; 
    z-index: 2;
    font-size: 1rem;
    font-family: 'Lato', sans-serif;
}

#button {
    font-weight: bold;
    //width: 50%;
    //height: 5%;
    height: 60px;
    width: 500px;
    text-align: center;
    //color: #ffffff;
    font-family: 'Lato', sans-serif;
    font-size: 35px;
    justify-content: center;
    border: none;
    left: 33px;
}

</style>
