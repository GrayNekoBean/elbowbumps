<template id="frame">
  <section>
    <Toast position="top-right" />
    <Sidebar v-model:visible="sidebarOpen">
      <div style="margin: 1rem">
      <h3> <span style = "color: #a9edfe">ELBOW</span> <span style = "color: #ffaaaa">BUMPS</span> </h3>
      </div>
      <Menu style="width: 100%" :model="sidebar_items" />
    </Sidebar>
    <Card class="main-frame">
      <template #header>
        <Card class="header-menu">
          <template #header>  <!--<h1 style="text-align: left">Welcome to Elbow Bump</h1>-->
            <div class="header-right-menu">
              <TabView class="top-tab" v-model:activeIndex="header_active" @tab-click="(event) => route_to(event.index)" v-if="!logined()">
                <TabPanel>
                  <template #header>
                    <i class="pi pi-home tab-icon"></i>
                    <span>Home</span>
                  </template>
                </TabPanel>
                <TabPanel>
                  <template #header>
                    <i class="pi pi-info-circle tab-icon"></i>
                    <span>About</span>
                  </template>
                </TabPanel>
                <TabPanel>
                  <template #header>
                    <i class="pi pi-sign-in tab-icon"></i>
                    <span>Login</span>
                  </template>
                </TabPanel>
                <TabPanel>
                  <template #header>
                    <i class="pi pi-user-plus tab-icon"></i>
                    <span>Register</span>
                  </template>
                </TabPanel>
              </TabView>
              <TabView class="top-tab" v-model:activeIndex="header_active" @tab-click="(event) => route_to(event.index)" v-else>
                <TabPanel>
                  <template #header>
                    <i class="pi pi-home tab-icon"></i>
                    <span>Home</span>
                  </template>
                </TabPanel>
                <TabPanel>
                  <template #header>
                    <i class="pi pi-info-circle tab-icon"></i>
                    <span>About</span>
                  </template>
                </TabPanel>
              </TabView>
              <!-- <div v-if="logined()" class="user-info-cover"></div> -->
              <div v-if="logined()" class="clickable-gray" @click="showMenu">
                <div class="user-info-area">
                  <div>
                    <Avatar image="https://i.imgur.com/VtIwKXj.jpg" class="p-mr-2" size="large" shape="circle" style="background-color:#2196F3; color: #ffffff; margin-right: 1rem;" />
                  </div>
                  <div class="user-info-text">
                    <p style="display:block; margin-right: 1rem;"> Welcome, {{current_user}}! </p>
                    <Menu :model="user_menu_items" id="user_menu_overlay" ref="user_menu" :popup="true" />
                  </div>
                </div>
              </div>
            </div>
            <div style="position: absolute; top: 1rem; left: 1rem; z-index: 6; height: 2rem; width: 2rem;">
            <IconButton v-if="logined()" icon="pi-bars" @click="sidebarOpen = true" color="gray"/>
            </div>
            <div class="header-title" :class="logined() ? 'longer-title' : ''">
              <h3> <span style = "color: #a9edfe">ELBOW</span> <span style = "color: #ffaaaa">BUMPS</span> </h3>
            </div>
          </template>
        </Card>
      </template>
      <br />
      <template #content>
        <div class="context-part">
          <router-view></router-view>
        </div>
      </template>
      <br />
      <template #footer>
        <div class="footer-menu">
          <TabMenu :model="footer_items" />
        </div>
      </template>
    </Card>
  </section>
</template>

<script>
//import AppFrame from "./components/App-Frame.vue";
import axios from "axios";
import IconButton from "./components/IconButton";
import router from "./router";
export default {
  components: { IconButton },
  watch: {
    // header_active: function (val){
    //   if (val >= 0 && val < 4){
    //     router.push(this.id_routers[val]);
    //   }
    // }
  },
  data(){
    return {
      current_user: this.$store.getters.fName,
      avatar: this.$store.getters.avatar,
      header_active: 0,
      show_menu: false,
      sidebarOpen: false,
      id_routers: {
        0: "/",
        1: "/about",
        2: "/login",
        3: "/register"
      },
      routers_id: {},
      footer_items: [
        { label: "Privacy Policy", to: "/privacy" },
        { label: "Terms and Conditions", to: "/terms" },
        { label: "Contact us", to: "/contact" },
      ],
      user_menu_items: [
        {
          label: "",
          items: [
            {
              label: "Profile",
              icon: "pi pi-user",
              command: () => this.route_to('/profile')
            },
            {
              label: "Logout",
              icon: "pi pi-sign-out",
              command: this.logout
            }
          ]
        }
      ],
      sidebar_items: [
        {
          label: "Home",
          icon: "pi pi-home",
          to: "/"
        },
        {
          label: "My Data",
          icon: "pi pi-chart-bar",
          to: "interest-data"
        },
        {
          label: "My Matching",
          icon: "pi pi-users",
          to: "/matches"
        },
        {
          label: "My Bumps",
          icon: "pi pi-user-plus",
          to: "/bumps"
        },
        {
          label: "Bumping Page",
          icon: "pi pi-user-plus",
          to: "/bumping_page"
        },
      ]
    }
  },
  mounted: function(){
    this.routers_id = this.swapKeyValue(this.id_routers);
    if (!this.logined()){
      if ('current_user' in sessionStorage){
        this.current_user = sessionStorage['current_user'];
      }else if ('current_user' in localStorage){
        this.current_user = localStorage['current_user'];
      }
      if(this.current_user != ""){
        this.login(this.current_user, true);
      }
    }else{
      this.current_user = this.$store.getters.fName;
      this.avatar = "assets/test.jpg";
      this.user_menu_items[0].label = "You're now login as " + this.current_user;
    }
  },
  methods: {
    login: function(id, remember=false){
      
      // this.login_profile = "Profile";
      // this.register_settings = "Settings";
      // this.id_routers[9] = "/profile";
      // this.id_routers[10] = "/settings";            this.errors = "";
      axios.get(this.$store.getters.URL + "user_data", {params: {user_id: id}}).then(
        (resp) => {
          this.$store.dispatch("logIn",{ id: id, fName: resp.data.data.fName, avatar: resp.data.data.avatar });
          this.current_user = this.$store.getters.fName;
          sessionStorage.setItem('current_user', id);
          if (remember){
            localStorage.setItem('current_user', id);
          }
          this.user_menu_items[0].label = "You're now login as " + this.current_user;
          this.routers_id = this.swapKeyValue(this.id_routers);
          this.$forceUpdate();
        }).catch((e) => {
          console.error(e);
        });
      
    },
    logout: function(){
      this.$store.dispatch("logOut");
      sessionStorage.removeItem("current_user");
      localStorage.removeItem("current_user");
      this.routers_id = this.swapKeyValue(this.id_routers);
      this.route_to('/');
    },
    displayLog: function(info, detail = '') {
      console.log(info);
      this.$toast.add({severity:'info', summary: info, detail: detail, life: 3000});
    },
    displaySuccessLog: function(info, detail = '') {
      console.log(info);
      this.$toast.add({severity:'success', summary: info, detail: detail, life: 3000});
    },
    displayWarning: function(info, detail = '') {
      console.warn(info);
      this.$toast.add({severity:'warning', summary: info, detail: detail, life: 3000});
    },
    displayError: function(info, detail = '') {
      console.warn(info);
      this.$toast.add({severity:'error', summary: info, detail: detail, life: 3000});
    },
    updateHeader: function(){
      this.current_user = this.$store.getters.fName;
      this.user_menu_items[0].label = `You are now login as ${this.current_user}! `;
      this.$forceUpdate();
    },
    logined: function(){
      if (this.$store.getters.userId){
        return true;
      }else{
        return false;
      }
    },
    showMenu: function(event){
      this.$refs.user_menu.toggle(event);
    },
    swapKeyValue: function(obj){
      let res = {};
      for(let key in obj){
        res[obj[key]] = key;
      }
      return res;
    },
    route_to: function(path){
      console.log('route');
      if (typeof(path) == 'string'){
        if (path in Object.keys(this.routers_id)){
          this.header_active = Number(this.routers_id[path]);
        }else{
          this.header_active = 0;
          //this.header_active = 5;
        }
        this.$router.push(path);
      }else if(typeof(path) == 'number'){
        if (path < Object.keys(this.id_routers).length){
          this.header_active = path;
          this.$router.push(this.id_routers[path]);
        }else{
          this.header_active = 0;
          //this.header_active = 5;
        }
      }else{
        console.error('Invalid routing argument');
      }
    },
  }
};
</script>

<style lang="scss">
@import './scss/colour-theme';
$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #80929F;
:root{
  --primary-color: #ffaaaa !important;
  --primary-color-text: #fffaba !important;
}
div.p-sidebar{
  padding: 0rem;
}
// ul.p-menu-list{
//   margin-top: 1rem !important;
// }
div.top-tab{
  align-self: right;
  width: 100%;
  height: 100%;
}
body{
  margin: 0px;
}
.p-tabview-nav-link {
  display: block !important;
  align-items: center;
}
.p-tabview-title {
  text-align: center;
}
.p-tabview {
    .p-tabview-panels{
        padding: 0 !important;
        height: 0%;
    }
    .p-tabview-nav{
        //margin-left: 60%;
        
        li {
          text-align: center;
          margin-right: 0;
          width: 25%;
          background: #ffffff;
        }
        li a.p-tabview-nav-link {
          border-color: #ffffff;
          // border-width: 0 2px 2px 0;
          // border-top-right-radius: 0;
          // border-top-left-radius: 0;
          // background: #ffaaaa;
          // border-color: #fffaba;
          color: #7da9b4;
          background: #ffffff; //rgba(169, 237, 254, 0.3);
        }
        li.p-highlight a.p-tabview-nav-link{
          border-color: #7da9b4;
          background: #ffffff; //rgba(169, 237, 254, 0.3);
          // border-width: 0 2px 2px 0;
          // border-top-right-radius: 0;
          // border-top-left-radius: 0;
          // background: #ff8080;
          // border-color: #fffaba;
          // color: #fffaba;
        }
        li:not(.p-highlight):not(.p-disabled):hover a.p-tabview-nav-link {
          border-color: #7da9b4;
          background: #ffffff //rgba(169, 237, 254, 0.3);
          // border-width: 0 2px 2px 0;
          // border-top-right-radius: 0;
          // border-top-left-radius: 0;
          // background: #ff9090;
          // border-color: #fffaba;
          // color: #fffaba;
        }
    }
}
div.p-avatar{
  margin-top: 5%;
}
.p-avatar img{
  border-radius: 50%;
}
.p-card .p-card-body{
  padding: 0 !important;
  height: 0%;
}
.p-card .p-card-body .p-card-content{
  padding: 0 !important;
  height: 0%;
}
.user-info-area{
  position: absolute;
  display: flex;
  flex-flow: row;
  top: 0;
  right: 0;
  z-index: 6;
  //width: 70%;
  //margin-right: 2%;
}
.clickable-gray{
  cursor: pointer;
  :hover {
    background: lightgray;
  }
}
button.user-info-text{
  color: black;
  background: transparent;
  border: 0px;
}
div.p-menubar{
  background: transparent;
  border: 0px;
}
.main-frame {
  width: 100%;
  height: 100%;
  z-index: 0;
}
.user-info-cover{
  position: absolute;
  display: block;
  background: white;
  top: 0;
  right: 0;
  height: 96%;
  width: 20%;
  z-index: 5;
}
.header-title{
  position: fixed;
  display: block;
  top: 0;
  margin-left: 0;
  height: 3.3rem;
  margin-left: 4rem;
  text-align: left;
  background: #ffffff; //rgba(255, 255, 255, 0.3); //rgba(169, 237, 254, 1);
  width: 20%;
  z-index: 4;
}
.header-menu {
  position: fixed;
  display: block;
  width: 100%;
  top: 0%;
  z-index: 3;
}
.header-right-menu {
  display: flex;
  flex-flow: row;
  justify-content: right;
  margin-left: 68%;
}
.footer-menu {
  position: fixed;
  width: 100%;
  bottom: 0%;
  z-index: 3;
}
.context-part {
  position: absolute;
  height: 100%;
  top: 0%;
  width: 100%;
  z-index: 0;
}
.tab-icon{
  margin-right: 0.5rem;
}
</style>