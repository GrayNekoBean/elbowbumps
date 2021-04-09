// This will go under account when you match with them but I'll put it here for now 
// There are three outputs of the report form, 'report' (a radio option)', 'how' (a radio option) and 'details' (text)

<template>
  <form @submit.prevent="submitForm">
    <h1>Report this account</h1>
    <div
      @change="
        how = null;
        details = '';
      "
    >
      <h2>What is your problem with this account?</h2>
      <div>
        <input
          id="report-student"
          name="report"
          type="radio"
          value="not-student"
          v-model="report"
        />
        <label for="report-student">They are not a student</label>
      </div>
      <div>
        <input
          id="report-blogs"
          name="report"
          type="radio"
          value="abusive"
          v-model="report"
        />
        <label for="report-blogs"
          >Abusive or hateful behaviour on the messaging service</label
        >
      </div>
      <div>
        <input
          id="report-fake"
          name="report"
          type="radio"
          value="fake"
          v-model="report"
        />
        <label for="report-fake"
          >They are impersonating me or someone else</label
        >
      </div>
      <div>
        <input
          id="report-abusive"
          name="report"
          type="radio"
          value="abusive-content"
          v-model="report"
        />
        <label for="report-abusive"
          >Their profile picture or name includes abusive or hateful
          content</label
        >
      </div>
      <div>
        <input
          id="report-help"
          name="report"
          type="radio"
          value="needs-help"
          v-model="report"
        />
        <label for="report-help"
          >They're expressing intentions of self-harm or suicide on the
          messaging service</label
        >
      </div>
      <div>
        <input
          id="report-other"
          name="report"
          type="radio"
          value="other"
          v-model="report"
        />
        <label for="report-other">Other</label>
      </div>
    </div>

    <div v-if="report === 'abusive'">
      <h2>How is this account being abusive?</h2>
      <div>
        <input
          id="abusive-protected"
          name="how"
          type="radio"
          value="abusive-protected-cat"
          v-model="how"
        />
        <label for="abusive-protected"
          >Targeted hate towards a protected category (race, religion, gender,
          orientation, disability)</label
        >
      </div>
      <div>
        <input
          id="abusive-violence"
          name="how"
          type="radio"
          value="abusive-violence"
          v-model="how"
        />
        <label for="abusive-violence"
          >Encouraging violence or physical harm</label
        >
      </div>
      <div>
        <input
          id="abusive-harassment"
          name="how"
          type="radio"
          value="abusive-harassment"
          v-model="how"
        />
        <label for="abusive-harassment"
          >They are targetting harassment towards me</label
        >
      </div>
    </div>

    <div v-else-if="report === 'fake'">
      <h2>Who is being impersonated?</h2>
      <div>
        <input
          id="fake-me"
          name="how"
          type="radio"
          value="fake-me"
          v-model="how"
        />
        <label for="fake-me">Me</label>
      </div>
      <div>
        <input
          id="fake-else"
          name="how"
          type="radio"
          value="fake-else"
          v-model="how"
        />
        <label for="fake-else">Someone else</label>
      </div>
      <div>
        <input
          v-if="how === 'fake-else'"
          placeholder="Type in their name"
          type="text"
          v-model="details"
        />
      </div>
    </div>

    <div v-else-if="report === 'content'">
      <h2>
        What kind of content does their profile picture or account name contain?
      </h2>
      <div>
        <input
          id="content-hateful"
          name="how"
          type="radio"
          value="content-hateful"
          v-model="how"
        />
        <label for="content-hateful">Hateful</label>
      </div>
      <div>
        <input
          id="content-graphic"
          name="how"
          type="radio"
          value="content-graphic"
          v-model="how"
        />
        <label for="content-graphic">Graphic</label>
      </div>
    </div>

    <div v-if="report === 'other' || report === 'help' || report === 'abusive'">
      <br />
      <h2>Please describe the situation in more detail:</h2>
      <textarea
        v-model="details"
        placeholder="add multiple lines"
        rows="4"
        cols="76"
      ></textarea>
    </div>

    <div>
      <br />
      <button>Next</button>
    </div>
  </form>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      report: null,
      how: null,
      details: "",
    };
  },
  methods: {
    submitForm() {
      let form = new FormData();
      if (this.how == null){
        this.how = this.report;
      }
      if (this.$store.getters.userId){
        form.append("id_1", this.$store.getters.userId);
      }
      else {
        console.error('Not logined.');
        return;
      }
      if (this.$route.params.user_id){
        form.append("id_2", this.$route.params.user_id);
      }
      else {
        console.error('Cannot find who you are reporting.');
        return;
      }
      form.append("report", this.how);
      form.append("details", this.details);

      axios.post(this.$store.getters.URL + "/report", form).then(
        (response) => {
          let jsonData = response.data;
          if (jsonData['STATUS_CODE'] == 200){
            this.$router.push('/bumps');
          }
        }
      );
    },
  },
};
</script>

<style lang="scss" scoped>
  form {
    margin: 2rem auto;
    max-width: 40rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    padding: 2rem;
    background-color: #ffffff;
  }

  .form-control {
    margin: 0.5rem 0;
  }

  label {
    font-weight: bold;
  }

  h2 {
    font-size: 1rem;
    margin: 0.5rem 0;
  }

  input,
  select {
    display: block;
    width: 100%;
    font: inherit;
    margin-top: 0.5rem;
  }

  select {
    width: auto;
  }

  input[type='checkbox'],
  input[type='radio'] {
    display: inline-block;
    width: auto;
    margin-right: 1rem;
  }

  input[type='checkbox'] + label,
  input[type='radio'] + label {
    font-weight: normal;
  }

  button {
    font: inherit;
    border: 1px solid #0076bb;
    background-color: #0076bb;
    color: white;
    cursor: pointer;
    padding: 0.75rem 2rem;
    border-radius: 30px;
  }

  button:hover,
  button:active {
    border-color: #002350;
    background-color: #002350;
  }

</style>
