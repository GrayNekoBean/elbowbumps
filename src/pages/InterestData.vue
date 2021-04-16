<template>
    <div class="container">
        <h2 style="text-align: center; margin-top:5rem; padding-top: 3rem;"> Want to know more about your interests? You are in the right place!</h2>
        <br />
        Stuff you like:
        <Tag
          v-for="tag in tags"
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
              <span style="margin-left: 0.5rem;">Table View</span>
            </template>
            <Graphs :userId="$store.getters.userId" :showTable="true"></Graphs>
          </TabPanel>
          <TabPanel>
            <template #header>
                <div style="height: 50%;">
                <i class="pi pi-chart-bar"></i>
                <span style="margin-left: 0.5rem;">Graph View</span>
                </div>
            </template>
            <br />
            <Graphs :userId="$store.getters.userId" :showTable="false" ref="graph" />
          </TabPanel>
        </TabView>
    </div>
</template>


<script>
import Graphs from '../components/Graphs.vue'

import axios from "axios";
export default {
    components: { Graphs },
    data() {
        return{
            name: "",
            avatar: "", 
            tags: []
        };
    },
    mounted(){
        this.FetchInterests();
        this.FetchUserInfo();
        
    },
    methods: {
    FetchInterests() {
      const userId = this.$store.getters.userId;
      let args = {
        user_id: userId,
      };
      axios
        .get(this.$store.getters.URL + "get_interests", { params: args })
        .then((response) => {
          if (response.data.STATUS_CODE == 200) {

            this.tags = response.data.Data;

            // let interests = response.data.Data;
            // for (let i = 0; i < interests.length; i++) {
            //   this.interestCats.push({ name: interests[i], id: 1 + i });
            // }
          }
          //this.$root.displayLog(this.interestCats);
        });
    },
    FetchUserInfo() {
      let address = this.$store.getters.URL + "user_data";
      let args = {
        user_id: this.$store.getters.userId
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
            this.userName = this.firstName + " " + this.lastName;

            if (this.avatar == "") {
              this.avatar = require("../assets/test.jpg");
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
    }
}
</script> 

<style  lang="scss" scoped>
/* * {
    margin-top: 4%;
    margin-bottom: 4%;
} */

#container{
    height:100%;
}
::v-deep {
  .p-tag {
    height: 1.5rem;
    margin-right: 0.25rem;
    margin-bottom: 0.25rem;
  }
}



.detailed-info {
  display: block;
  margin-top: 10%;
  margin-left: 5%;
  height: 48rem;
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