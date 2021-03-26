<template>
  <div>
    <Card>
      <template #header>
        <h2 style="text-align: center; margin-top:4rem;">
          Welcome to your matches!
        </h2>
      </template>
      <template #content>
        <div v-if="noMatches" style="text-align: center;">
          You have no matches! Click
          <router-link to="/questionnaire">here</router-link> to do the
          questionnaire, or
          <router-link to="/socialmediainfo">here</router-link> to update your
          Twitter info!
        </div>
        <accordion v-else>
          <accordion-tab
            v-for="user in users"
            :key="user.id"
            :header="user.forename"
          >
            <h2>{{ user.forename }} {{ user.surname }}</h2>
            <Button @click="bump(user.id)">Bump {{ user.forename }}!</Button>
          </accordion-tab>
        </accordion>
        <div style="padding-bottom:3rem; display:flex; justify-content:center;">
          <Button @click="logout" style="display:inline-block;">
            Logout
          </Button>
          <Button @click="getMatches" style="display:inline-block;">
            Refresh Matches
          </Button>
          <router-link to="/bumps"
            ><Button style="display:inline-block"
              >See bumps</Button
            ></router-link
          >
        </div>
      </template>
    </Card>
  </div>
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
    if (!this.$store.getters.matchesRetrieved) {
      this.getMatches();
    }
  },
  computed: {
    noMatches: function() {
      return this.matches.length == 0;
    },
  },
  methods: {
    getMatches() {
      const URL = `${this.$store.getters.URL}find_matches`;
      const userId = this.$store.getters.userId;
      axios
        .get(URL, {
          params: {
            user_id: userId,
            limit: 8,
          },
        })
        .then((res) => (this.matches = res.data.result))
        .catch((err) => {
          console.log(err);
        });

      this.getMatchInfo();
    },
    getMatchInfo() {
      const URL = `${this.$store.getters.URL}match_info`;

      const form = new FormData();
      console.log(JSON.stringify(this.matches))
      form.append("matches", JSON.stringify(this.matches));
      axios
        .post(URL, form)
        .then((res) => (this.users = res.data.match_info))
        .catch((err) => {
          console.log(err);
        });
    },
    bump(id) {
      const URL = `${this.$store.getters.URL}bump`;
      console.log(`${this.$store.getters.userId} ${id}`);
      const form = new FormData();
      form.append("userId", this.$store.getters.userId);
      form.append("matchId", id);
      axios.post(URL, form).then((res) => {
        if (res.data.STATUS_CODE == "200") {
          console.log("success!");
        }
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
