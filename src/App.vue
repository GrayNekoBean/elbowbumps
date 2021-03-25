<template>
  <section>
    <Card class="main-frame">
      <template #header>
        <Card class="header-menu">
          <template #header>
            <!--<h1 style="text-align: left">Welcome to Elbow Bump</h1>-->
            <TabView v-model:activeIndex="header_active">
              <TabPanel header="Home"></TabPanel>
              <TabPanel header="About"></TabPanel>
              <TabPanel></TabPanel>
              <TabPanel></TabPanel>
              <TabPanel></TabPanel>
              <TabPanel></TabPanel>
              <TabPanel></TabPanel>
              <TabPanel></TabPanel>
              <TabPanel v-if="!logined()" header="Login"></TabPanel>
              <TabPanel v-else header=""></TabPanel>
              <TabPanel v-if="!logined()" header="Register"></TabPanel>
              <TabPanel v-else header=""></TabPanel>
            </TabView>
            <div v-if="logined()" class="user-info-cover"></div>
            <div v-if="logined()" class="user-info-area">
              <div>
                <Avatar image="https://i.imgur.com/VtIwKXj.jpg" class="p-mr-2" size="large" shape="circle" style="background-color:#2196F3; color: #ffffff" />
              </div>
              <Button class="user-info-text" @click="showMenu">
                <p style="display:block; margin:0;"> Welcom, {{current_user}}! </p>
                <Menu :model="user_menu_items" id="user_menu_overlay" ref="user_menu" :popup="true" />
              </Button>
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

import router from "./router"

export default {
  components: {},
  watch: {
    header_active: function (val){
      router.push(this.id_routers[val]);
    }
  },
  data(){
    return {
      current_user: "",
      avatar: "",
      header_active: 0,
      show_menu: false,
      id_routers: {
        0: "/",
        1: "/about",
        8: "/login",
        9: "/register"
      },
      routers_id: {},
      header_items: [
        { label: "Home", to: "/" },
        { label: "Login", to: "login" },
        { label: "Sign up", to: "register" },
        { label: "About us", to: "about" },
      ],
      footer_items: [
        { label: "Privacy Policy", to: "/privacy" },
        { label: "Terms and Conditions", to: "/terms" },
        { label: "Contact us", to: "/contact" },
      ],
      user_menu_items: [
        {
          label: `Welcome, ${this.current_user}! `,
          items: [
            {
              label: "Profile",
              icon: "pi pi-user",
              to: "/profile"
            },
            {
              label: "Settings",
              icon: "pi pi-sliders-h",
              to: "/settings"
            }
          ]
        }
      ]
    }
  },
  mounted: function(){
    this.routers_id = this.swapKeyValue(this.id_routers);

    if ('current_user' in sessionStorage){
      this.current_user = sessionStorage['current_user'];
    }else if ('current_user' in localStorage){
      this.current_user = localStorage['current_user'];
    }
    if(this.current_user != ""){
      this.setLoginState();
    }

    //this.current_user = this.$store.getters.userId;
    this.avatar = "assets/test.jpg";
  },
  methods: { 
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
    setLoginState: function(userFName, avatar = ''){
      
      // this.login_profile = "Profile";
      // this.register_settings = "Settings";

      // this.id_routers[9] = "/profile";
      // this.id_routers[10] = "/settings";
        this.current_user = userFName;
      this.avatar = avatar;
      this.user_menu_items[0]['label'] = "You're now login as " + this.current_user;
      this.routers_id = this.swapKeyValue(this.id_routers);
      this.$forceUpdate();
      
    },
    setLogoutState: function(){
      // this.login_profile = "Login";
      // this.register_settings = "Register";

      // this.id_routers[9] = "/login";
      // this.id_routers[10] = "/register";


      this.routers_id = this.swapKeyValue(this.id_routers);
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
      this.header_active = Number(this.routers_id[path]);
      this.$router.push(path);
    }
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
        li {
          text-align: center;
          margin-right: 0;
          width: 10%;
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
  //margin-right: 2%;
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
  margin-left: 20%;
  height: 3.3rem;
  text-align: center;
  background: #ffffff; //rgba(255, 255, 255, 0.3); //rgba(169, 237, 254, 1);
  width: 60%;
  z-index: 4;
}

.header-menu {
  position: fixed;
  display: block;
  width: 100%;
  top: 0%;
  z-index: 3;
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

</style>
