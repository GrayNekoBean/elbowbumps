<template>
  <Card>
    <slot>
      <p>{{ match.forename }} {{ match.surname }}</p>
      <Button @click="bump" :disabled="!bumped">Match with this user!</Button>
    </slot>
  </Card>
</template>

<script>
import axios from "axios";

export default {
  props: { match: Object },
  data() {
    return {
      bumped: false,
    };
  },
  methods: {
    bump() {
      const URL = `${this.$store.getters.URL}bump`;
      axios
        .post(URL, {
          params: {
            user_id: this.$store.getters.userId,
            match_id: this.match.id,
          },
        })
        .then((res) => {
          if (res.data.STATUS_CODE == "200") {
            console.log("success!");
          }
        });

      this.bumped = true;
    },
  },
};
</script>
