<template>
  <SplitedPage ratio="1">
    <template #left>
      <h2 style="text-align: center; margin-top:5rem; padding-top: 3rem;">
        Welcome to your matches!
      </h2>
      <div v-if="noMatches" style="text-align: center;">
        You have no new matches :( Click
        <router-link to="/questionnaire">here</router-link> to do the
        questionnaire, or
        <router-link to="/profile">here</router-link> to update your
        Twitter info.
      </div>
      <div style="margin-left:10%; margin-top: 5%; width: 75%; overflow: hidden;" v-else>
          <!-- <h2>{{ user.forename }} {{ user.surname }}</h2>
          <Button @click="bump(user.id)">Bump {{ user.forename }}!</Button> -->
          <div class="matches-list" ref="matches">
            <BumperPanel
              class="bump-card"
              v-for="user in users"
              :key="user.id"
              :userID="user.id"
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
      <div style="display: flex;width: 100%;height: 2rem;margin-top: 4rem;justify-content: center;">
        <IconButton icon="pi-undo" hint="Refresh Matches" @onClick="getMatches" />
        <select class="form-control" @change="changeInterestCat($event)">
          <option value="All interests" >All interests</option>
          <option v-for="interestCat in interestCats" :value="interestCat.id" :key="interestCat.id">{{ interestCat.name }}</option>
        </select>
        <select class="form-control" @change="changeLimit($event)">
          <option value="8" selected disabled>Default Matches 8</option>
          <option v-for="limit in limits" :value="limit.id" :key="limit.id">{{ limit.name }}</option>
        </select>
      </div>
    </template>
    <template #right>

    </template>
  </SplitedPage>
</template>

<script>
import axios from "axios";
import Flickity from "flickity";
import "flickity/dist/flickity.min.css";

import BumperPanel from "../components/BumperPanel";
import SplitedPage from "../components/SplitedPage";
import IconButton from "../components/IconButton";

export default {
  components: { BumperPanel, SplitedPage, IconButton },
  data() {
    return {
      matches: [],
      users: [],
      selectedUser: {
        avatar: '',
        name: '',
        bio: '',
        twitter: '',
        tags: [],
        interestData: null
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
    };
  },
  mounted() {
    this.FetchCurrentUserInterests();
    this.setLimits();
    if (!this.$store.getters.matchesRetrieved) {
      this.getMatches();
    }
    setInterval(this.onUpdate, 1000/40);
  },
  computed: {
    noMatches: function() {
      return this.matches.length == 0;
    },
  },
  methods: {
    setLimits(){
      for (let i = 1; i < 50; i++){
        this.limits.push({name: String(i), id: i})
      }
    },
    FetchCurrentUserInterests(){
        const userId = this.$store.getters.userId;
        let args = {
            user_id: userId
        };
        axios.get(this.$store.getters.URL + "get_interests", {params: args}).then(
        (response) => {
            if (response.data.STATUS_CODE == 200){
                let interests = response.data.Data;
                for (let i = 0; i < interests.length; i++){
                  this.interestCats.push({name: interests[i], id: 1+i});
                }
            }
            this.$root.displayLog(this.interestCats);
        });
    }, 
    changeInterestCat (event) {
      this.selectedInterestCat = event.target.options[event.target.options.selectedIndex].text
      this.getMatches();
      // TO-DO Needs a forced flickity update or something with flickity
   },
   changeLimit(event) {
     this.selectedLimit = event.target.options[event.target.options.selectedIndex].text
     this.getMatches();
    // TO-DO Needs a forced flickity update or something with flickity
   },
    getMatches() {
      const URL = `${this.$store.getters.URL}find_matches`;
      const userId = this.$store.getters.userId;
      axios
        .get(URL, {
          params: {
            user_id: userId,
            limit: this.selectedLimit,
            interestCat: this.selectedInterestCat
          },
        })
        .then((res) => {
          this.matches = res.data.result;
          if (this.matches == null){
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
          this.$nextTick(() => {
            if (!this.flickity) {
              this.flickity = new Flickity(this.$refs.matches, {
                accessbility: true,
                cellAlign: 'center',
                draggable: '>1',
                dragThreshold: 3,
                percentPosition: false,
                prevNextButtons: true,
                pageDots: true,
                cellSelector: ".p-card.p-component.bump-card",
                lazyLoad: false,
                resize: true,
                setGallerySize: false,
                watchCSS: false,
                wrapAround: false
              });
              this.flickity.on('change', this.onSelectBumper)
            }
          });
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
    onUpdate(){
      if(this.leftMoving || this.rightMoving){
          let dom = this.$refs['matches'];
          let margin_left = Number(dom.style.marginLeft.substring(0,dom.style.marginLeft.length-2));
          let direction = this.leftMoving ? -1 : 1;
          dom.style.marginLeft = (margin_left + direction*8) + 'px';
          if (Math.abs(margin_left - this.originalMarginLeft) >= 288){
            dom.style.marginLeft = (this.originalMarginLeft + direction * 288) + 'px';
            this.leftMoving = false;
            this.rightMoving = false;
            this.originalMarginLeft = margin_left;
          }
      }
    },
    onSelectBumper(index){
      console.log('flickity index: ' + index);
    }
  }
};
</script>

<style lang="scss" scoped>

.matches-frame{
  margin-top: 10rem;
  padding-bottom:3rem;
  display:flex;
  justify-content:center;
}

.matches-list{
  display: flex;
  flex-flow: row;
  flex-wrap: nowrap;
  height: 416px;
  z-index: 2;
}

.bump-card{
  width: 16rem;
  height: 24rem;
  margin: 1rem;
}

::v-deep {
  .flickity-viewport {
    width: 100%;
  }

  .flickity-page-dots {
    bottom: inherit;
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
