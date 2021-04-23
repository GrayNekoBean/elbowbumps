<template>
  <Card style="width: 16rem; height: 24rem;">
    <template #content>
      <div :class="selected ? '' : 'overlay'"></div>
      <div class="bumper-panel">
        <div
          style="display: flex; flex-flow: column; justify-content: space-between; align-items: center;"
        >
          <Avatar size="xlarge" :image="avatar" shape="circle" />
          <h3>{{ userName }}</h3>
        </div>
        <Tag :class="{ near : near, middle: middle, far: far }">{{ match_percentage }}% Match</Tag>
        <div class="intro">
          {{ intro }}
        </div>
        <!-- <p style="color:#bb2e2e; font-size:small;">Interests: {{interests}}</p> -->
        <div class="tags-area">
          <Tag
            v-for="ints in interests"
            :key="ints"
            class="p-mr-2"
            severity="success"
            :value="ints"
          ></Tag>
        </div>
        <!-- <Button v-if="!pending" @click="bump">Bump</Button>
                <Button style="background:#bb2e2e;" v-else @click="unbump">Unbump</Button> -->
        <SplitButton
          class="p-mb-2"
          :class="pending ? 'p-button-danger' : ''"
          :label="pending ? 'Unbump' : 'Bump'"
          :icon="pending ? 'pi pi-minus' : 'pi pi-plus'"
          :model="buttonItem"
          @click="onBump"
        />
        <!-- <Button v-if="!pending" @click="bump">Bump</Button>
                <Button style="background:#bb2e2e;" v-else @click="unbump">Unbump</Button>
                <div style="display: flex; justify-content: space-between;">
                    <IconButton hint="Block User" icon="pi-ban" color="black" @click="blockUser()"></IconButton>
                    <IconButton hint="Report User" icon="pi-times" color="red" @click="reportUser()"></IconButton>
                </div> -->
      </div>
    </template>
  </Card>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      buttonItem: [
        {
          label: "Block User",
          icon: "pi pi-ban",
          command: this.blockUser,
        },
        {
          label: "Report User",
          icon: "pi pi-times",
          command: this.reportUser,
        },
      ],
      userName: "",
      bio: "",
      interests: [],
      twitter: "",
      tags: [],
      intro: "",
      firstName: "",
      lastName: "",
      pending: false,
      avatar: "",
      match_percentage: 0,
      class: ""
    };
  },
  computed: {
    far() {
        return this.match_percentage < 40;
    },
    middle() {
        return this.match_percentage >= 40 && this.match_percentage < 60;
    },
    near() {
        return this.match_percentage >= 60;
    }
  },
  props: ["userID", "distance","selected"],
  emits: ["onRemove"],
  methods: {
    PendingUsers() {
      const user_id = this.$store.getters.userId;
      let args = {
        userID_1: user_id,
        userID_2: this.userID,
      };
      axios
        .get(this.$store.getters.URL + "pending_bumps", { params: args })
        .then((response) => {
          if (response.data.STATUS_CODE == 200) {
            this.pending = response.data.result;
            // this.$root.displayLog("Fetching interest data successed", dat);
          }
        });
    },
    FetchMatchScore() {
      this.match_percentage = Number((((8 - Number(this.distance)) / 8) * 100).toFixed(1));
      // let args = {
      //     user_id: this.userID,
      //     limit: 8,
      // }

      // axios.get(this.$store.getters.URL + "find_matches", {params: args}).then(
      // (response) => {
      //     if (response.data.STATUS_CODE == 200){
      //         let match_data = response.data.result;
      //         this.$root.displayLog("Fetching interest data successed", match_data);
      //         var i;
      //         for(i=0; i < match_data.length; i++){
      //             if((match_data[i]['distance'] != null)&&(match_data[i]['uid_ud_id'] == this.$store.getters.userId)){
      //                 this.match_percentage = (((8 - match_data[i]['distance'])/8)*100).toFixed(1);
      //             }
      //         }
      //         console.log(this.match_percentage)

      //     }
      // })
      // .catch((err) => {
      // console.log(err);
      // });
    },

    FetchUserInterests() {
      let args = {
        user_id: this.userID,
      };
      axios
        .get(this.$store.getters.URL + "get_interests", { params: args })
        .then((response) => {
          if (response.data.STATUS_CODE == 200) {
            this.interests = response.data.Data;

            // //only for multiple line testing
            // this.interests.push('test1');
            // this.interests.push('test2');

            // this.$root.displayLog("Fetching interest data successed");
            // dat.forEach( interest =>{
            //     this.interests.append(interest);
            // });
          }
        });
    },
    FetchUserInfo() {
      let address = this.$store.getters.URL + "user_data";
      let args = {
        user_id: this.userID,
      };
      let dataPack = null;
      axios
        .get(address, { params: args })
        .then((response) => {
          if (response.data.STATUS_CODE == "200") {
            let data = response.data["data"];
            this.avatar = data["avatar"];
            this.firstName = data["fName"];
            this.lastName = data["sName"];
            this.twitter = data["twitter"];
            this.bio = data["bio"];
            this.intro = data["intro"];
            this.userName = this.firstName + " " + this.lastName;

            if (this.avatar == "") {
              this.avatar = require("../assets/test.jpg");
            }
            if (this.intro == "") {
              this.intro = "This person doesn't have an intro :( ";
            }
            if (this.bio == "") {
              this.bio = "This person doesn't have an bio :( ";
            }
          } else {
            console.error(response.STATUS);
            console.error(response.Message);
          }
        })
        .catch((e) => {
          console.error(e);
        });
    },
    onBump() {
      if (this.pending) {
        this.unbump();
      } else {
        this.bump();
      }
    },
    bump() {
      const URL = `${this.$store.getters.URL}bump`;
      console.log(`${this.$store.getters.userId} ${this.userID}`);
      const form = new FormData();
      form.append("userId", this.$store.getters.userId);
      form.append("matchId", this.userID);
      axios.post(URL, form).then((res) => {
        if (res.data.STATUS_CODE == "200") {
          console.log("success!");
          this.pending = true;
        }
      });
    },
    unbump() {
      const URL = `${this.$store.getters.URL}unbump`;
      console.log(`${this.$store.getters.userId} ${this.userID}`);
      const form = new FormData();
      form.append("userId", this.$store.getters.userId);
      form.append("matchId", this.userID);
      axios.post(URL, form).then((res) => {
        if (res.data.STATUS_CODE == "200") {
          console.log("success!");
          this.pending = false;
        }
      });
    },
    blockUser() {
      //this.showBumpCard = false;
      const URL = `${this.$store.getters.URL}blockUser`;
      console.log(`${this.$store.getters.userId} ${this.userID}`);
      const form = new FormData();
      form.append("userId", this.$store.getters.userId);
      form.append("matchId", this.userID);
      axios.post(URL, form).then((res) => {
        if (res.data.STATUS_CODE == "200") {
          console.log("success!");
          //this.$el.parentNode.removeChild(this.$el);
          this.$emit("onRemove", this.$el);
          // TODO Flickity update
        }
      });
    },
    fullBump() {
      const user_id = this.$store.getters.userId;
      let args = {
        userID_1: user_id,
        userID_2: this.userID,
      };
      axios
        .get(this.$store.getters.URL + "full_bumps", { params: args })
        .then((response) => {
          if (response.data.STATUS_CODE == 200) {
            if (response.data.result) {
              this.$root.displayLog(this.userName + " bumped you back!");
              this.$el.parentNode.removeChild(this.$el);
            }
          }
        });
    },
    getValidTags(limit) {},
    confirmBump() {
      console.log("Send Bump message: " + this.bumpMsg);
    },
    reportUser() {
      console.log(this.userID);
      this.$router.push({ name: "report", params: { user_id: this.userID } });
    },
    openTwitterPage() {
      window.open("https://twitter.com/" + this.twitter, "_blank");
    },
  },
  mounted: function() {
    this.FetchUserInfo();
    this.FetchUserInterests();
    this.FetchMatchScore();
    this.PendingUsers();
    this.fullBump();
  },
};
</script>

<style lang="scss" scoped>
::v-deep {
  .p-tag {
    height: 1.5rem;
    margin-right: 0.25rem;
    margin-bottom: 0.25rem;
  }
}

.overlay {
  position: absolute;
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #5e686e80; /* Black background with opacity */
  z-index: 6; /* Specify a stack order in case you're using a different order for other elements */
}

.bumper-panel {
  display: flex;
  flex-flow: column;
  justify-content: space-around;
  align-items: center;
  height: 24rem;
  width: 16rem;
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

.tags-area {
  display: flex;
  flex-flow: row;
  flex-wrap: wrap;
  overflow: auto;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 3.5rem;
  overflow: hidden;
}

.intro {
  height: 2.8rem;
  display: -webkit-box;
  overflow: hidden;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
}

.edit-icon {
  height: 2rem;
  width: 2rem;
  padding: 25%;
  cursor: pointer;
}

.edit-button-blue {
  color: rgb(29, 161, 242);
  :hover {
    border-radius: 50%;
    background: rgba(29, 161, 242, 0.3);
  }
}

.edit-button-red {
  color: rgb(128, 16, 16);
  :hover {
    border-radius: 50%;
    background: rgba(128, 16, 16, 0.3);
  }
}

.near {
  font-size: 14px;
  background: #6aab4f;
  color: white;
}

.far {
  font-size: 14px;
  background: #ab4f4f;
  color: white;
}

.middle {
  font-size: 14px;
  background: #abab4f;
  color: white;
}
</style>
