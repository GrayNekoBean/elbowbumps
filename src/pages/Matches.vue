<template>
  <SplitedPage ratio="0.6">
    <template #left>
      <h2 style="text-align: center; margin-top: 5rem; padding-top: 3rem">
        Welcome to your matches!
      </h2>
      <div v-if="selectedMatchType != 'Matches'" style="text-align: center">
        Opposites attract, or maybe you just want to find someone you can elbow
        bump in the face. We get it!
      </div>
      <div v-if="noMatches" style="text-align: center">
        You have no new matches :( Click
        <router-link to="/questionnaire">here</router-link> to do the
        questionnaire, or <router-link to="/profile">here</router-link> to
        update your Twitter info.
      </div>
      <div
        style="margin-left: 10%; margin-top: 5%; width: 75%; overflow: hidden"
        v-else
      >
        <!-- <h2>{{ user.forename }} {{ user.surname }}</h2>
          <Button @click="bump(user.id)">Bump {{ user.forename }}!</Button> -->
        <div class="matches-list" ref="matches">
          <BumperPanel
            class="bump-card"
            v-for="user in users"
            :key="user"
            :userID="user.id"
            :distance="user.distance"
            @onRemove="removeUser"
          />
        </div>
      </div>
      <!-- <div style="">
        <Button @click="moveLeft">《-</Button>
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
      <Button @click="moveRight"> -》</Button>
      </div> -->
      <div
        style="
          display: flex;
          width: 100%;
          height: 2rem;
          margin-top: 4rem;
          justify-content: center;
        "
      >
        <IconButton icon="pi-refresh" hint="Refresh Matches" @onClick="refresh" />
        <select class="form-control" @change="changeInterestCat($event)">
          <option value="All interests">All interests</option>
          <option
            v-for="interestCat in interestCats"
            :value="interestCat.id"
            :key="interestCat.id"
          >
            {{ interestCat.name }}
          </option>
        </select>
        <select class="form-control" @change="changeLimit($event)">
          <option value="8" selected disabled>Default Matches 8</option>
          <option v-for="limit in limits" :value="limit.id" :key="limit.id">
            {{ limit.name }}
          </option>
        </select>
        <select class="form-control" @change="changeMatchOrder($event)">
          <option value="True">Matches</option>
          <option value="False">Anti-matches</option>
          <!-- <option v-for="interestCat in interestCats" :value="interestCat.id" :key="interestCat.id">{{ interestCat.name }}</option> -->
        </select>
        <!-- <Button><router-link to="/antimatches"  style="text-decoration: none; color: inherit;">AntiMatches</router-link></Button> -->
      </div>
    </template>
    <template #right>
      <ScrollPanel class="detailed-info">
        <div class="detail-top">
          <Avatar
            shape="circle"
            :image="selectedUser.avatar"
            size="xlarge"
            style="margin-right: 2rem"
          />
          <div style="width: 60%">
            <h3>
              {{ selectedUser.name }}
            </h3>
            <p>
              {{ selectedUser.intro }}
            </p>
          </div>
        </div>
        <br />
        Interests in:
        <Tag
          v-for="tag in selectedUser.tags"
          severity="success"
          :key="tag"
          class="p-mr-2"
          :value="tag"
        />
        <br />
        <TabView>
          <TabPanel>
            <template #header>
              <i class="pi pi-align-center"></i>
              <span style="margin-left: 0.5rem;">Bio</span>
            </template>
            <div class="bio-area" ref="bio">(No Bio)</div>
          </TabPanel>
          <TabPanel>
            <template #header>
              <i class="pi pi-chart-bar"></i>
              <span style="margin-left: 0.5rem;">Data</span>
            </template>
            <br />
            <Graphs :userId="selectedUser.userId" :showTable="false" ref="graph" />
          </TabPanel>
        </TabView>
      </ScrollPanel>
    </template>
  </SplitedPage>
</template>

<script>
import axios from "axios";
import Flickity from "flickity";
import "flickity/dist/flickity.min.css";
import Markdown from "markdown-it";
import emoji from "markdown-it-emoji";
import BumperPanel from "../components/BumperPanel";
import SplitedPage from "../components/SplitedPage";
import IconButton from "../components/IconButton";
import Graphs from "../components/Graphs";

export default {
  components: { BumperPanel, SplitedPage, IconButton, Graphs },
  data() {
    return {
      matches: [],
      users: [],
      selectedUser: {
        userId: 0,
        avatar: "",
        name: "",
        intro: "",
        bio: "",
        twitter: "",
        tags: [],
        interestData: null,
      },
      leftMoving: false,
      rightMoving: false,
      focused: 0,
      originalMarginLeft: 0,
      flickity: null,
      interestCats: [],
      selectedInterestCat: "All interests",
      limits: [],
      selectedLimit: "8",
      selectedMatchType: "Matches",
    };
  },
  mounted() {
    this.markdown = new Markdown({
      html: true, // Enable HTML tags in source
      xhtmlOut: true, // Use '/' to close single tags (<br />).
      // This is only for full CommonMark compatibility.
      breaks: false, // Convert '\n' in paragraphs into <br>
      langPrefix: "language-", // CSS language prefix for fenced blocks. Can be
      // useful for external highlighters.
      linkify: true, // Autoconvert URL-like text to links
      // Enable some language-neutral replacement + quotes beautification
      // For the full list of replacements, see https://github.com/markdown-it/markdown-it/blob/master/lib/rules_core/replacements.js
      typographer: true,
      // Double + single quotes replacement pairs, when typographer enabled,
      // and smartquotes on. Could be either a String or an Array.
      //
      // For example, you can use '«»„“' for Russian, '„“‚‘' for German,
      // and ['«\xA0', '\xA0»', '‹\xA0', '\xA0›'] for French (including nbsp).
      quotes: "“”‘’",
      // Highlighter function. Should return escaped HTML,
      // or '' if the source string is not changed and should be escaped externally.
      // If result starts with <pre... internal wrapper is skipped.
      highlight: function (/*str, lang*/) {
        return "";
      },
    });
    this.markdown.use(emoji);
    this.FetchCurrentUserInterests();
    this.setLimits();
    if (!this.$store.getters.matchesRetrieved) {
      this.getMatches();
    }
    setInterval(this.onUpdate, 1000 / 40);
  },
  computed: {
    noMatches: function () {
      return this.matches.length == 0;
    },
  },
  methods: {
    setLimits() {
      for (let i = 1; i < 17; i++) {
        this.limits.push({ name: String(i), id: i });
      }
    },
    FetchCurrentUserInterests() {
      const userId = this.$store.getters.userId;
      let args = {
        user_id: userId,
      };
      axios
        .get(this.$store.getters.URL + "get_interests", { params: args })
        .then((response) => {
          if (response.data.STATUS_CODE == 200) {
            let interests = response.data.Data;
            for (let i = 0; i < interests.length; i++) {
              this.interestCats.push({ name: interests[i], id: 1 + i });
            }
          }
          //this.$root.displayLog(this.interestCats);
        });
    },
    changeMatchOrder(event) {
      this.selectedMatchType =
        event.target.options[event.target.options.selectedIndex].text;
      this.$root.displayLog("Changed matching type: " + this.selectedMatchType);
      this.refresh();
    },
    changeInterestCat(event) {
      this.selectedInterestCat =
        event.target.options[event.target.options.selectedIndex].text;
      this.$root.displayLog(
        "Weighted matching based on: " + this.selectedInterestCat
      );
      this.getMatches();
      // TO-DO Needs a forced flickity update or something with flickity
    },
    changeLimit(event) {
      this.selectedLimit =
        event.target.options[event.target.options.selectedIndex].text;
      this.$root.displayLog(
        "Limited number of matches to: " + this.selectedLimit
      );
      this.getMatches();
      // TO-DO Needs a forced flickity update or something with flickity
    },
    getMatchesNum(event) {
      this.getmatch =
        event.target.options[event.target.options.selectedIndex].text;
      this.getMatches();
      // TO-DO Needs a forced flickity update or something with flickity
    },
    refresh() {
      if (this.selectedMatchType == "Matches") {
        this.getMatches();
      } else {
        this.getAntiMatches();
      }
    },
    getMatches() {
      const URL = `${this.$store.getters.URL}find_matches`;
      const userId = this.$store.getters.userId;
      axios
        .get(URL, {
          params: {
            user_id: userId,
            limit: this.selectedLimit,
            interestCat: this.selectedInterestCat,
          },
        })
        .then((res) => {
          this.matches = res.data.result;
          if (this.matches == null) {
            this.matches = [];
          }
          this.getMatchInfo();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getAntiMatches() {
      const URL = `${this.$store.getters.URL}find_furthest_matches`;
      const userId = this.$store.getters.userId;
      axios
        .get(URL, {
          params: {
            user_id: userId,
            limit: this.selectedLimit,
            interestCat: this.selectedInterestCat,
          },
        })
        .then((res) => {
          this.matches = res.data.result;
          if (this.matches == null) {
            this.matches = [];
          }
          this.getMatchInfo();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getMatchInfo() {
      const URL = `${this.$store.getters.URL}match_info`;
      const form = new FormData();
      form.append("matches", JSON.stringify(this.matches));
      axios
        .post(URL, form)
        .then((res) => {
          this.users = res.data.match_info;
          this.users.forEach((user) => {
            const distance = this.matches.filter(
              (match) => match.uid_ud_id == user.id
            )[0].distance;
            user["distance"] = distance;
          });
          this.$nextTick(() => {
            if (this.flickity) {
              this.flickity.destroy();
              this.$forceUpdate();
            }
            this.flickity = new Flickity(this.$refs.matches, {
              accessbility: true,
              cellAlign: "center",
              draggable: ">1",
              dragThreshold: 3,
              percentPosition: false,
              prevNextButtons: true,
              pageDots: true,
              cellSelector: ".p-card.p-component.bump-card",
              lazyLoad: false,
              resize: true,
              setGallerySize: false,
              watchCSS: false,
              wrapAround: false,
            });
            this.flickity.on("change", this.onSelectBumper);
          });
          if (this.users.length > 0) {
            this.onSelectBumper(0);
          }
        })
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
          this.getMatches();
        }
      });
    },
    removeUser(element) {
      if (this.flickity) {
        this.flickity.remove(element);
      }
    },
    logout() {
      this.$store.dispatch("logOut");
      this.$router.push("/");
    },
    moveLeft() {
      this.leftMoving = true;
      this.rightMoving = false;
    },
    moveRight() {
      this.rightMoving = true;
      this.leftMoving = false;
    },
    onUpdate() {
      if (this.leftMoving || this.rightMoving) {
        let dom = this.$refs["matches"];
        let margin_left = Number(
          dom.style.marginLeft.substring(0, dom.style.marginLeft.length - 2)
        );
        let direction = this.leftMoving ? -1 : 1;
        dom.style.marginLeft = margin_left + direction * 8 + "px";
        if (Math.abs(margin_left - this.originalMarginLeft) >= 288) {
          dom.style.marginLeft =
            this.originalMarginLeft + direction * 288 + "px";
          this.leftMoving = false;
          this.rightMoving = false;
          this.originalMarginLeft = margin_left;
        }
      }
    },
    onSelectBumper(index) {
      axios
        .get(this.$store.getters.URL + "user_data", {
          params: {
            user_id: this.users[index].id,
          },
        })
        .then((response) => {
          if (response.data.STATUS_CODE == 200) {
            let dat = response.data.data;
            this.selectedUser.userId = this.users[index].id;
            this.selectedUser.avatar = dat.avatar;
            this.selectedUser.name = dat.fName + " " + dat.sName;
            this.selectedUser.intro = dat.intro;
            this.selectedUser.bio = dat.bio;
            this.selectedUser.twitter = dat.twitter;
            this.$refs.bio.innerHTML = this.markdown.render(dat.bio);
            this.$refs.graph.initGraph(this.selectedUser.userId);
            this.$forceUpdate();
          } else {
            this.$root.displayWarn(
              "Request Failed: " + response.data.STATUS_CODE,
              response.data.message
            );
            return;
          }
        })
        .catch((err) => {
          this.$root.displayError("Request Error", err);
        });
      let args = {
        user_id: this.users[index].id,
      };
      axios
        .get(this.$store.getters.URL + "get_interests", { params: args })
        .then((response) => {
          if (response.data.STATUS_CODE == 200) {
            this.selectedUser.tags = response.data.Data;
          }
        });
      console.log("flickity index: " + index);
    },
  },
};
</script>

<style lang="scss" scoped>
.matches-frame {
  margin-top: 10rem;
  padding-bottom: 3rem;
  display: flex;
  justify-content: center;
}
.matches-list {
  display: flex;
  flex-flow: row;
  flex-wrap: nowrap;
  height: 416px;
  z-index: 2;
}
.bump-card {
  width: 16rem;
  height: 24rem;
  margin: 1rem;
}
.detailed-info {
  display: block;
  margin-top: 10%;
  margin-left: 5%;
  height: 48rem;
}
.detail-top {
  display: flex;
  flex-flow: row;
  justify-content: left;
}
::v-deep {
  .flickity-viewport {
    width: 100%;
  }
  .flickity-page-dots {
    bottom: inherit;
  }
  .p-tag {
    margin-right: 0.25rem;
    margin-bottom: 0.25rem;
  }
}
// .bump-card {
//   animation-name: move-right;
//   animation-duration: 800ms;
//   animation-delay: 0ms;
//   animation-fill-mode: forwards;
//   animation-timing-function: linear;
//   animation-iteration-count: infinite;
//   transform-origin: 0 0;
// }
// @keyframes move-right {
//   0% {transform:translate(0px, 0px) scale(1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) translate(-50%, -50%);animation-timing-function: cubic-bezier(.25,.25,.75,.75);}
//   12.50% {transform:translate(100px, 0px) scale(1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) translate(-50%, -50%);animation-timing-function: cubic-bezier(.25,.25,.75,.75);}
//   87.50% {transform:translate(200px, 0px) scale(1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) translate(-50%, -50%);animation-timing-function: cubic-bezier(.25,.25,.75,.75);}
//   100% {transform:translate(250px, 0px) scale(1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) translate(-50%, -50%);}
// }html::after { content: url(https://ga-beacon.appspot.com/UA-42910121-1/stylie?pixel); position: absolute; left: -999em; }
</style>