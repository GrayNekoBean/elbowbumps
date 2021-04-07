<template>
  <div>
    <Toast position="top-right" />
    <Card class="login-card">
      <template #header>
        <div class="heading">
          <br />
          <h2 style="margin-left: 2rem">Log in to an existing account:</h2>
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
            Forgottten your password? Click
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
      </template>
    </Card>
  </div>
</template>

<script>
import axios from "axios";
import crypto from "crypto";
import Dialog from "primevue/dialog";

export default {
  components: { Dialog },

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
      axios
        .post(url, formData)
        .then((response) => {
          let responseData = response.data;
          console.log(responseData);
          let responseStatus = responseData.STATUS_CODE;

          if (responseStatus == "200") {
            //TODO: Show a notification with info like this: "Login Successful"
            this.$root.setLoginState(response.data.id, this.rememberMe);
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
$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #fffaba;

.login-card {
  display: block;
  margin-top: 5rem;
  margin-left: 5rem;
  top: 20%;
  bottom: 10%;
  width: 40rem;
  height: 40rem;
  z-index: 2;
}

h2 {
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
  color: $primitive-color;
  font-size: 32px;
}

p {
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
  color: $primitive-color;
}

::v-deep{
  button.p-button {
    font-weight: bold;
    width: 10rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    justify-content: center;
    background: $primitive-color;
    border: none;
  }
}
</style>
