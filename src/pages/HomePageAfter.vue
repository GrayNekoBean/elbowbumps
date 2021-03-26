<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <div id = "welcome">
    <h1>Welcome</h1>
  </div>
  <div id="frame">
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
      <button id="button" @click="$router.push('Bumps')"><i class="fa fa-bars" style="margin-right:19%;"></i>  VIEW PAST BUMPS</button>
      <button id="button" @click="$router.push('SocialMediaInfo')"><i class="fa fa-twitter" style="margin-right:31%;"></i>  YOUR SOCIALS</button>
      <button id="button" @click="$router.push('Matches')"><i class="fa fa-heart" style="margin-right:23%;"></i>  MATCHING PAGE</button>
      <button id="button" @click="$router.push('Questionnaire')"><i class="fa fa-question-circle" style="margin-right:24%;"></i> QUESTIONNAIRE</button>
    </div>
    <!-- <div id="bottom-right">
      <img src="../assets/pic.png" id="pic"/>
    </div> -->
  </div> 
</template> 

<script>
export default {};
</script>

<style lang="scss" scoped>

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
$primitive-color: #a9edfe;
$secondary-color: #ffaaaab9;
$background-color: 	#80929F;
//$background-color: #E95B46;
//$background-color: 	#DB744E;
//$background-color: #ffffff;
//$background-color: #fffaba;

#icon1 {
  background: url()
}

#frame {
  position: absolute;
  height: 100%;
  width: 100%;
  background: $background-color;
}

#top-right {
  position: absolute;
  //margin-left:2%;
  margin-right:6%;
  height: 100%;
  right: 0px;
  width: 42%;
  top: -10%;
  background: $background-color;
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
  margin-top: 23%;
  margin-left:7.5%;
  height: 50%;
  left: 0px;
  width: 42%;
  font-size: 2vw;
  text-align: right;
  font-family: 'Lato', sans-serif;
  line-height: 3.75vw;
  color: #ffffff;
}

#button {
    //font-weight: bold;
    width:60%;
    height: 15%;
    margin-top: 1%;
    padding: 1% 2% 1% 1%;
    border: 1% 1% 1% 1%;
    margin-bottom: 1%;
    text-align: right;
    color: #ffffff;
    font-family: 'Lato', sans-serif;
    font-size: 1.7vw;
    justify-content: center;
    background: $secondary-color;
    border: none;
}

</style>

