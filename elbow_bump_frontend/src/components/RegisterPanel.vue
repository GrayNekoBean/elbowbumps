<template>
    <div>
        <Card class="register-card">
        <template #header>
        <div class="heading" style="margin-top: 10rem;">
            <h2>Create an account</h2>
        </div>
        </template>

        <template #content>
        <div id="creds">
            <form @submit.prevent="registerUser">
            <label>First Name:</label><br>
            <InputText type="text" id="fName" v-model="enteredfName" required /><br /><br>
            <label>Last Name:</label><br>
            <InputText type="text" id="sName" v-model="enteredsName" required /><br /><br>
            <label>Phone Number:</label><br>
            <InputText type="tel" id="phoneNum" v-model="enteredphoneNum" required /><br /><br>
            <label>Email:</label><br>
            <InputText type="email" id="email" v-model="enteredemailAdd" required /><br /><br>
            <label>Password:</label><br>
            <Password id="pw" v-model="enteredpw" required /><br /><br /><br>
            <Checkbox v-model="agree_terms" :binary="true" required />
            <router-link to="/terms"> Terms and Conditions</router-link><br /><br />
            <Button>Create Account</button><br />
            </form>
        </div>

        <p>
            Already have an account? Click
            <router-link to="/login">here</router-link> to log in!
        </p>
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
      agree_terms: false
    };
  },
  methods: {
    registerUser() {

      let remote_url = "postgres://lrrucystcdokqx:8dcdf77fcf5031f6d6bf22e181e8e526fc69393bae3bbaed0065588c2963f6fb@ec2-54-198-73-79.compute-1.amazonaws.com:5432/da8ahn3kepucis";
      let local_url = "http://localhost:5000/register";

      let hashedPw = crypto.createHash('sha1').update(this.enteredpw).digest('hex');

      axios.post(
        local_url,
        {
          fName: this.enteredfName,
          sName: this.enteredsName,
          phoneNum: this.enteredphoneNum,
          emailAdd: this.enteredemailAdd,
          pw: hashedPw
        }
      ).then(() =>
        {
          this.enteredfName = "";
          this.enteredsName = "";
          this.enteredphoneNum = "";
          this.enteredemailAdd = "";
          this.enteredpw = "";
        }
      );
 },
  },
};
</script>

<style lang="scss">
.register-card{
    display: block;
    padding-left: 1rem;
    margin-top: 5.5rem;
    margin-left: 5rem;
    top: 20%;
    bottom: 10%;
    width: 40rem;
    height: 36rem;
    z-index: 2;
}
</style>
