<template>
  <SplitedPage ratio="0.6">
    <template #left>
      <h2 style="text-align: center; margin-top:5rem; padding-top: 3rem;">
        <span v-if="noMatches"> No bumps for you to see today... but at least there are plenty more fish in the sea. </span>
        <span v-else>You both bumped each other!</span>
      </h2>
      <div v-if="!noMatches" style="text-align: center;"> Go ahead and add them on their Twitter if provided or pop them an email.</div>
      <div v-if="noMatches" style="text-align: center;">
        No-one has bumped you back (yet). Click
        <router-link to="/questionnaire">here</router-link> to do the
        questionnaire, or
        <router-link to="/profile">here</router-link> to update your
        Twitter info!
      </div>
      <div style="margin-left:10%; margin-top: 5%; width: 75%; overflow: hidden;" v-else>
          <div class="matches-list" ref="matches">
            <AfterAfterBumperPanel
              class="bump-card"
              v-for="user in users"
              :key="user"
              :userID="user.id"
              :selected="selectedUser.userId == user.id"
              @onRemove="removeUser"
            />
          </div>
      </div>
      <div style="display: flex;width: 100%;height: 2rem;margin-top: 4rem;justify-content: center;">
         <IconButton icon="pi-refresh" hint="Refresh Matches" @onClick="refresh" />
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
//import BumperPanel from "../components/BumperPanel";
import AfterAfterBumperPanel from "../components/AfterAfterBumperPanel";
import SplitedPage from "../components/SplitedPage";
import IconButton from "../components/IconButton";
import Graphs from "../components/Graphs";

export default {
  components: { AfterAfterBumperPanel, SplitedPage, IconButton, Graphs},
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
    if (!this.$store.getters.matchesRetrieved) {
      this.getMatches();
    }
    setInterval(this.onUpdate, 1000 / 40);
  },
  computed: {
    noMatches: function() {
      return this.matches.length == 0;
    },
  },
  methods: {
    getMatches() {
      const URL = `${this.$store.getters.URL}get_bumps`;
      const userId = this.$store.getters.userId;
      axios
        .get(URL, {
          params: {
            user_id: userId,
          },
        })
        .then((res) => {
          this.matches = res.data.matches;
          this.getMatchInfo();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    refresh() {
        this.getMatches();
    },
    getMatchInfo() {
      const URL = `${this.$store.getters.URL}match_info`;
      const jsonmatches = [];
      for (const match in this.matches) {
        jsonmatches.push({ uid_ud_id: this.matches[match] });
      }
      
      const form = new FormData();
      form.append("matches", JSON.stringify(jsonmatches));
      axios
        .post(URL, form)
        .then((res) => {
          this.users = res.data.match_info;
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
    removeUser(element) {
      if (this.flickity) {
        this.flickity.remove(element);
      }
    },
    logout() {
      this.$store.dispatch("logOut");
      this.$router.push("/");
    },
    moveLeft(){
      this.leftMoving = true;
      this.rightMoving = false
    },
    moveRight(){
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
