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
          value="student"
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
          value="content"
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
          value="help"
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
          value="abusive-protected"
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
      console.log(this.report);
      console.log(this.how);
      console.log(this.details);
      this.report = null;
      this.how = null;
      this.details = "";
    },
  },
};
</script>
