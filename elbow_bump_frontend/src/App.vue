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
              <TabPanel :header="login_profile"></TabPanel>
              <TabPanel :header="register_settings"></TabPanel>
            </TabView>
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
      header_active: 0,
      login_profile: "Login",
      register_settings: "Register",
      id_routers: {
        0: "/",
        1: "/about",
        2: "/login",
        3: "/register"
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
  },
  methods: { 
    setLoginState: function(){
      
      this.login_profile = "Profile";
      this.register_settings = "Settings";

      this.id_routers[2] = "/profile";
      this.id_routers[3] = "/settings";
      
      this.routers_id = this.swapKeyValue(this.id_routers);
      
    },
    setLogoutState: function(){
      this.login_profile = "Login";
      this.register_settings = "Register";

      this.id_routers[2] = "/login";
      this.id_routers[3] = "/register";

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
    }
  }
};
</script>

<style lang="scss">

@import './scss/colour-theme';

$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #fffaba;


body{
  margin: 0px;
}

:root{
  --primary-color: #ffaaaa !important;
  --primary-color-text: #fffaba !important;
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
          width: 25%;
        }

        li a.p-tabview-nav-link {
          border-width: 0 2px 2px 0;
          border-top-right-radius: 0;
          border-top-left-radius: 0;
          background: #ffaaaa;
          border-color: #fffaba;
          color: #fffaba;
        }

        li.p-highlight a.p-tabview-nav-link{
          border-width: 0 2px 2px 0;
          border-top-right-radius: 0;
          border-top-left-radius: 0;
          background: #ff8080;
          border-color: #fffaba;
          color: #fffaba;
        }

        li:not(.p-highlight):not(.p-disabled):hover a.p-tabview-nav-link {
          border-width: 0 2px 2px 0;
          border-top-right-radius: 0;
          border-top-left-radius: 0;
          background: #ff9090;
          border-color: #fffaba;
          color: #fffaba;
        }
    }
}

.p-card .p-card-body{
  padding: 0 !important;
  height: 0%;
}


.p-card .p-card-body .p-card-content{
  padding: 0 !important;
  height: 0%;
}

.main-frame {
  width: 100%;
  height: 100%;
  z-index: 0;
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
