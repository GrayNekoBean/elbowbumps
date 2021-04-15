<template>

  <div id="frame" v-if="!$root.logined()">
    <div id="top-right">
      <div >
        <img src="../assets/eb_logo.svg" id="elb-poster" />
      </div>
    </div>
    <div id="top-left">
      <h1 style = "color: #ffe38f">WELCOME TO</h1>
      <h1 style = "color: #a9edfe">ELBOW <span style = "color: #ffaaaa">BUMPS</span></h1>
      <!-- <h1 style = "color: #ffaaaa">BUMPS</h1> -->
    </div>
    <div id="bottom-left">
      <p >Is lockdown loneliness bogging you down? Do you want to find other people who are passionate in the same things you are? Elbow Bumps provides a new, innovative way for you to do just that! <br> <br>Simply register, fill in a questionnaire and give us your Twitter, and we'll find you people who love the very same things you love.</p>
      <div id="button2"><Button id="button" @click="$router.push('Register')">GET STARTED</Button></div>
    </div>
    <!-- <div id="bottom-right">
      <img src="../assets/pic.png" id="pic"/>
    </div> -->
  </div>
  <LoginHome v-else />
</template> 

<script>
import LoginHome from "../components/LoginHome";

export default {
  components: {
    LoginHome
  }
};
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato&family=Open+Sans&display=swap');
$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: 	#80929F;
//$background-color: #E95B46;
//$background-color: 	#DB744E;
//$background-color: #ffffff;
//$background-color: #fffaba;
#frame {
  position: absolute;
  height: 100%;
  width: 100%;
  background: $background-color;
}
#top-right {
  position: absolute;
  margin-left:2%;
  margin-right:6%;
  height: 100%;
  right: 0px;
  width: 42%;
  top: -3%;
}
#elb-poster {
  display: block;
  height: auto;
  width: 100%;
  max-height: 100%;
}
#top-left {
  padding: 1%;
  border: 1%;
  position: absolute;
  margin-left:2%;
  margin-top: 5%;
  margin-bottom:7.5%;
  height: 50%;
  left: 0px;
  width: 50%;
  font-size: 3.75vw;
  text-align: right;
  font-family: 'Montserrat', sans-serif;
  line-height: 2.2vw;
}
#bottom-left {
  padding: 1%;
  border: 1%;
  position: absolute;
  margin-top: 20%;
  margin-left:3%;
  height: 50%;
  left: 0px;
  width: 48.5%;
  font-size: 1.5vw;
  text-align: right;
  font-family: 'Lato', sans-serif;
  //line-height: 3.75vw;
  color: #ffffff;
}
#button {
    font-weight: bold;
    width: 30%;
    height: 5%;
    text-align: center;
    color: #ffffff;
    font-family: 'Lato', sans-serif;
    font-size: 35px;
    justify-content: center;
    background: $secondary-color;
    border: none;
}
</style>

