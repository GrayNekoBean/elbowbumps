<template>
  <Card style="width: 16rem; height: 24rem;">
    <template #content>
      <div class="bumper-panel">
        <div
          style="display: flex; flex-flow: column; justify-content: space-between; align-items: center;"
        >
          <Avatar size="xlarge" :image="avatar" shape="circle" />
          <h3>{{ userName }}</h3>
        </div>
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
          :model="buttonItem"
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
            label: "View their Twitter",
            icon: "pi pi-twitter",
            command: this.openTwitterPage,
        },
        {
          label: "Email them",
          icon: "pi pi-envelope",
          command: this.openEmail,
        },
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
      class: "", 
      email: ""
    };
  },
  computed: {

  },
  props: ["userID", "distance"],
  emits: ["onRemove"],
  methods: {
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
             this.email = data["email"];
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
        if (this.twitter != ''){
             this.buttonItem.push({
                label: "View their Twitter",
                icon: "pi-twitter",
                command: this.openTwitterPage,
             }) 
        }
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
    getValidTags(limit) {},
    reportUser() {
      console.log(this.userID);
      this.$router.push({ name: "report", params: { user_id: this.userID } });
    },
    openTwitterPage(){
        if (this.twitter == ''){
             this.$root.displayLog(
                "They don't seem to have provided a Twitter account. Email them and complain."
            );
        }
        else {
            window.open("https://twitter.com/" + this.twitter, "_blank");
        }
    },
    openEmail(){
        if (this.email == ''){
          this.$root.displayError(
            "There was an error getting their email."
        );
        }
        else {
            window.open("mailto:" + this.email, "_blank");
        }
    }
  },
  mounted: function() {
    this.FetchUserInfo();
    this.FetchUserInterests();
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
