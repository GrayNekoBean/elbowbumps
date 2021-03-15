<template>
  <div>
    <Card>
      <template #header>
        <h2>Welcome to your matches!</h2>
      </template>
      <template #content>
        <Accordion>
          <AccordionTab
            v-for="match in matches"
            :key="match.uid_ud_id"
            :header="match.uid_ud_id"
          >
            <p>{{ match.uid_ud_id }}: {{ match.distance }}</p>
          </AccordionTab>
        </Accordion>
        <Button @click="logout" style="margin: 50px;">
          Logout
        </Button>
        <Button @click="getMatches" style="margin: 50px;">
          Refresh Matches
        </Button>
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
    };
  },
  mounted() {
    if (!this.$store.getters.matchesRetrieved) {
      this.getMatches();
    }
  },
  methods: {
    getMatches() {
      const localURL = `${this.$store.getters.localURL}find_matches`;
      const userId = this.$store.getters.userId;
      console.log(userId);
      axios
        .get(localURL, {
          params: {
            user_id: userId,
            limit: 5,
          },
        })
        .then((res) => (this.matches = res.data.result))
        .catch((err) => {
          console.log(err);
        });
    },
    logout() {
      this.$store.dispatch("logOut");
      this.$router.push('/')
    },
  },
};
</script>

<style></style>
