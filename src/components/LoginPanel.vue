<template>
  <div>
    <Card class="login-card">
      <template #header>
        <div class="heading" style="margin-top: 10%;">
          <h2>Login</h2>
        </div>
      </template>

      <template #content>
        <div style="margin-left: 2rem">
          <Panel header="Login">
            <div id="creds">
              <form method="POST" @submit.prevent="submitLoginInfo()">
                <br />
                <label>Email:</label><br />
                <InputText id="Email" type="text" v-model="email" required />
                <br />
                <br />
                <label>Password:</label><br />
                <Password
                  id="passwd"
                  v-model="pw"
                  :feedback="false"
                  required
                  toggleMask
                /><br /><br />
                <div class="p-field-checkbox">
                  <Checkbox
                    id="remember"
                    name="remember"
                    v-model="rememberMe"
                    :binary="true"
                  />
                  <label for="remember" style="margin-left: 0.5rem;">Remember Me</label>
                </div>
                <br /><br />
                <Button class="p-button-raised" type="submit"
                  ><i class="pi pi-plus-circle" style="margin-top: 0px;" />
                  <div style="margin: 5px;">Login</div></Button
                >
                <br />
              </form>
            </div>
          </Panel>
        </div>
        <div style="margin-left: 2rem">
          <p>
            Forgotten your password? Click
            <router-link to="/forgot_password">here</router-link> to fix that.
          </p>
          <p>Don't already have an account? Register here:</p>
          <Button
            class="p-button-raised"
            @click="this.$root.route_to('/register')"
          >
            Register
          </Button>
          <Dialog v-model:visible="hasErrors" header="Oh no!" class="error">
            {{ error }} <br /><br />
            <Button label="Got it!" autofocus @click="removeErrors"></Button>
          </Dialog>
          <br /><br />
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
      rememberMe: false,
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
      axios.post(url, formData)

        .then((response) => {
          let responseData = response.data;
          console.log(responseData);
          let responseStatus = responseData.STATUS_CODE;

          if (responseStatus == "200") {
            //TODO: Show a notification with info like this: "Login Successful"
            this.$root.login(response.data.id, this.rememberMe);
            this.$root.route_to("/matches");
          } else if (responseStatus == "500") {
            this.errors = responseData.Message;
            this.email = "";
            this.pw = "";
          }
        })
        .catch((e) => {
          this.showNotification("Request Error", "Unexpected Error: " + "Invalid Email or Password");
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
