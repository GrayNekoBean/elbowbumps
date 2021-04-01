<template>
  <div>
    <Card class="login-card">
      <template #header>
        <div class="heading" style="margin-top: 10%;">
          <h2>Login</h2>
        </div>
      </template>

      <template #content>
        <div id="creds">
          <form method="POST" @submit.prevent="submitLoginInfo()">
            <label>Email:</label><br />
            <InputText
              type="text"
              id="Email"
              v-model="email"
              required
            /><br /><br />
            <label>Password:</label><br />
            <Password
              id="passwd"
              v-model="pw"
              required
              toggleMask
            /><br /><br />
            <Button type="submit">Login</Button><br />
          </form>
        </div>
            <p v-if="hasErrors">
              <ul v-for="error in errors" :key="error">
                <li>{{error}}</li>
              </ul>
            </p>

        <p>
          Don't have an account? Click
          <router-link to="/register">here</router-link> to register
        </p>
        <br /><br /><br />
      </template>
    </Card>
  </div>
</template>

<script>
import axios from "axios";
import crypto from "crypto";


export default {

  data() {
    return {
      email: "",
      pw: "",
      keepLogin: false,
      agree_terms: false,
      error: "",
    };
  },
  computed: {
    hasErrors: function() {
      return this.error !== "";
    },
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    showNotification(info, detail = '') {
      console.log(info);
      this.$toast.add({severity:'warn', summary: info, detail: detail, life: 3000});
    },
    submitLoginInfo() {
      // One hash operation in client side, and another hash operation in server side.
      // Not 100% safe, still easy to be hacked, but enough for demo XD
      let hashedPw = crypto
        .createHash("sha1")
        .update(this.pw)
        .digest("hex");

      let url = `${this.$store.getters.URL}login`;
      const formData = new FormData();
      formData.append("email", this.email);
      formData.append("pw", hashedPw);
      axios
        .post(url, formData)
        .then((response) => {
          let responseData = response.data;
          console.log(responseData);
          let responseStatus = responseData.STATUS_CODE;

          if (responseStatus == "200") {
            //TODO: Show a notification with info like this: "Login Successful"
            this.errors = "";
            axios.get(this.$store.getters.URL + "user_data", {params: {user_id: response.data.id}}).then(
              (resp) => {
                this.$store.dispatch("logIn",{ id: response.data.id, fName: resp.data.data.fName, avatar: resp.data.data.avatar });
                this.$root.setLoginState();
              }
            )
            this.$router.push("/matches");
          } else if (responseStatus == "500") {
            this.errors = responseData.Message;
            this.email = "";
            this.pw = "";
          }
        })
        .catch((e) => {
          this.showNotification("Request Error", "Unexpected Error: " + e.message);
        });
    },
    removeErrors() {
      this.error = "";
    },
  },
};
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

p{
  padding-left: 2rem;
}
.heading{
  font-family: 'Montserrat', sans-serif;
  font-weight: lighter;
  font-size: 1.5rem;
  padding-left: 2rem;
}
.login-card{
    position: absolute;
    display: block;
    top: 50%;
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    padding-left: 1rem;
    margin-left: 5rem;
    width: 40rem;
    height: 45rem;
    z-index: 2;
    font-size: 1rem;
    font-family: 'Lato', sans-serif;
}
#creds{
  margin-left: 2rem;
}
</style>
