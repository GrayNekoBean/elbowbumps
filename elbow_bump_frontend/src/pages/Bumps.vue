<template>
  <Card>
    <template #header>
      <h2 style="text-align: center; margin-top:4rem;">
        Welcome to your bumps!
      </h2>
      <p style="text-align: center;">
        Here you can see all the users with whom you've previously bumped
        elbows!
      </p>
    </template>
    <template #content>
      <div v-if="noMatches">
        <p>
          Well, it looks like you don't have any right now. Put yourself out
          there by <router-link to="/matches">matching with users</router-link>!
        </p>
      </div>
      <Accordion>
        <AccordionTab
          v-for="user in users"
          :key="user.id"
          :header="user.forename"
        >
          <h2>{{ user.forename }}</h2>
          <p>Twitter: @{{ user.twitter }}</p>
        </AccordionTab>
      </Accordion>
      <div style="display:flex; justify-content:center;">
      <Button @click="getBumps">Refresh!</Button>
      <Button @click="logout">Logout</Button>
      <router-link to="/matches"
        ><Button>Back to my matches!</Button></router-link
      >
      </div>
    </template>
  </Card>
</template>

<script>
import Accordion from "primevue/accordion";
import AccordionTab from "primevue/accordiontab";
import axios from "axios";

export default {
  components: { Accordion, AccordionTab },
  data() {
    return {
      matches: [],
      users: [],
    };
  },
  mounted() {
    this.getBumps();
  },
  computed: {
    noMatches: function() {
      return this.matches.length == 0;
    },
  },
  methods: {
    getBumps() {
      const URL = `${this.$store.getters.URL}get_bumps`;
      const userId = this.$store.getters.userId;
      axios
        .get(URL, {
          params: {
            user_id: userId,
          },
        })
        .then((res) => (this.matches = res.data.matches))
        .catch((err) => {
          console.log(err);
        });
      this.getMatchInfo();
    },
    getMatchInfo() {
      const jsonmatches = [];
      for (const match in this.matches) {
        jsonmatches.push({ uid_ud_id: this.matches[match] });
      }
      const URL = `${this.$store.getters.URL}match_info`;

      const form = new FormData();
      form.append("matches", JSON.stringify(jsonmatches));
      axios
        .post(URL, form)
        .then((res) => (this.users = res.data.match_info))
        .catch((err) => {
          console.log(err);
        });
    },
    logout() {
      this.$store.dispatch("logOut");
      this.$router.push("/");
    },
  },
};
</script>

<style></style>
