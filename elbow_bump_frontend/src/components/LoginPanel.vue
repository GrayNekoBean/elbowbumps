<template>
  <div>
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
              <form method="POST" @submit.prevent="this.submitLoginInfo()">
                <br />
                <label>Email:</label><br />
                <InputText id="Email" type="text" v-model="email" required />
                <br />
                <br />
                <label>Password:</label><br />
                <Password
                  id="passwd"
                  v-model="pw"
                  required
                  toggleMask
                /><br /><br />
                <Checkbox
                  id="agree"
                  v-model="agree_terms"
                  :binary="true"
                  required
                />
                <router-link to="/terms"> Terms & Conditions</router-link>
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
    showNotification(info) {
      console.log(info);
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
            this.$store.dispatch("logIn", response.data.id);

            this.$router.push("/matches");
          } else if (responseStatus == "500") {
            this.errors = responseData.Message;
            this.email = "";
            this.pw = "";
          }
        })
        .catch((e) => {
          this.showNotification("Unexpected Error: " + e);
        });
    },
    removeErrors() {
      this.error = "";
    },
  },
};
</script>

<style lang="scss">
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
  height: 38rem;
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
</style>
