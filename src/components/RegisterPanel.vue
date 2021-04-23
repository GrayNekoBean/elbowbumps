
<template>
  <div>
    <Card class="register-card">
      <template #header>
        <div class="heading" style="margin-top: 10%;">
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
              :class="checkName('fName', enteredfName) ? '' : 'p-invalid'"
              required
            />
            <small v-if="!checkName('fName', enteredfName)" id="username2-help" class="p-error">Username is invalid.</small>
            <br /><br />
            <label>Last Name:</label><br />
            <InputText
              type="text"
              id="sName"
              v-model="enteredsName"
              :class="checkName('sName', enteredfName) ? '' : 'p-invalid'"
              required
            />
            <small v-if="!checkName('sName', enteredsName)" id="username2-help" class="p-error">Username is invalid.</small>
            <br /><br />
            <br /><br />
            <label>Email:</label><br />
            <InputText
              type="email"
              id="email"
              v-model="enteredemailAdd"
              :class="checkEmail('email', enteredemailAdd) ? '' : 'p-invalid'"
              required
            />
            <small v-if="!checkEmail('email', enteredemailAdd)" id="username2-help" class="p-error">Email is invalid. (Note that only UoM email is accepted here)</small>
            <br /><br />
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
import validation from "../tools/validation";
export default {
  data() {
    return {
      enteredfName: "",
      enteredsName: "",
      enteredemailAdd: "",
      enteredpw: "",
      agree_terms: false,
      errors: [],
      inputValids: {}
    };
  },
  computed: {
    hasErrors: function() { return this.errors.length > 0; }
  },
  methods: {
    registerUser() {
      if (!(false in Object.values(this.inputValids))){
        let url = `${this.$store.getters.URL}register`;
        console.log(url)
        let hashedPw = crypto
          .createHash("sha1")
          .update(this.enteredpw)
          .digest("hex");
        const formData = new FormData()
        formData.append("fName", this.enteredfName)
        formData.append("sName", this.enteredsName)
        formData.append("emailAdd", this.enteredemailAdd)
        formData.append("pw", hashedPw)
        axios
          .post(url, formData) 
          .then((response) => {
            if (response.data.STATUS_CODE != 200) {
              this.errors.push(response.data.Message)
            } else {
              this.errors = []
              this.$root.login(response.data.id);
              console.log(response.data)
              console.log(this.$store.getters.userId)
              this.$store.dispatch('toggleFirstRegister')
              this.enteredfName = "";
              this.enteredsName = "";
              this.enteredemailAdd = "";
              this.enteredpw = "";
              this.$root.route_to('/questionnaire');
            }
        });
      }else{
        this.$root.displayWarn("Submit Failed", "There are invalid input in your register information.")
      }
    },
    checkName(id, name) {
      if (validation.checkName(name)){
        this.inputValids[id] = true;
        return true;
      }else{
        this.inputValids[id] = false;
        return false;
      }
    },
    checkEmail(id, email) {
      if (validation.checkEmail(email, true)){
        this.inputValids[id] = true;
        return true;
      }else{
        this.inputValids[id] = false;
        return false;
      }
    }
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
.register-card{
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