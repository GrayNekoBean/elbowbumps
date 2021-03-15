<template>
  <div>
    <Card class="register-card">
      <template #header>
        <div class="heading" style="margin-top: 15rem;">
          <h2>Create an account</h2>
        </div>
      </template>

      <template #content>
        <div id="creds">
          <form @submit.prevent="registerUser">
            <label>First Name:</label><br />
            <InputText
              type="text"
              id="fName"
              v-model="enteredfName"
              required
            /><br /><br />
            <label>Last Name:</label><br />
            <InputText
              type="text"
              id="sName"
              v-model="enteredsName"
              required
            /><br /><br />
            <label>Phone Number:</label><br />
            <InputText
              type="tel"
              id="phoneNum"
              v-model="enteredphoneNum"
              required
            /><br /><br />
            <label>Email:</label><br />
            <InputText
              type="email"
              id="email"
              v-model="enteredemailAdd"
              required
            /><br /><br />
            <label>Password:</label><br />
            <Password id="pw" v-model="enteredpw" required /><br /><br /><br />
            <Checkbox v-model="agree_terms" :binary="true" required />
            <router-link to="/terms"> Terms and Conditions</router-link
            ><br /><br />
            <Button type="submit">Create Account</Button><br />
          </form>
        </div>
            <p v-if="hasErrors">
              <ul v-for="error in errors" :key="error">
                <li>{{error}}</li>
              </ul>
            </p>

        <p>
          Already have an account? Click
          <router-link to="/login">here</router-link> to log in!
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
      enteredfName: "",
      enteredsName: "",
      enteredphoneNum: "",
      enteredemailAdd: "",
      enteredpw: "",
      agree_terms: false,
      errors: [],
    };
  },
  computed: {
    hasErrors: function() { return this.errors.length > 0; }
  },
  methods: {
    registerUser() {
      let remote_url =
        "http://ec2-54-198-73-79.compute-1.amazonaws.com/register";
      let local_url = "http://localhost:5000/register";

      let hashedPw = crypto
        .createHash("sha1")
        .update(this.enteredpw)
        .digest("hex");
      const formData = new FormData()
      formData.append("fName", this.enteredfName)
      formData.append("sName", this.enteredsName)
      formData.append("phoneNum", this.enteredphoneNum)
      formData.append("emailAdd", this.enteredemailAdd)
      formData.append("pw", hashedPw)
      axios
        .post(local_url, formData) 
        .then((response) => {
          if (response.data.STATUS_CODE != 200) {
            this.errors.push(response.data.Message)
          } else {
            this.errors = []
            this.$store.dispatch('logIn', response.data.id)
            console.log(response.data)
            console.log(this.$store.getters.userId)
            this.enteredfName = "";
            this.enteredsName = "";
            this.enteredphoneNum = "";
            this.enteredemailAdd = "";
            this.enteredpw = "";
            this.$router.push('/questionnaire')
          }
        });
    },
  },
};
</script>

<style lang="scss">
.register-card {
  display: block;
  padding-left: 2rem;
  margin-top: 5.5rem;
  margin-left: 5rem;
  top: 20%;
  bottom: 10%;
  width: 40rem;
  height: 41rem;
  z-index: 2;
}
</style>
