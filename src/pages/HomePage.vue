<template>
  <div id = "welcome">
    <h1>Welcome</h1>
  </div>
  <div id="frame">
    <div id="top-right">
      <div id = "poster">
        <img src="../assets/elbows-w-lines.png" id="elb-poster" />
      </div>
    </div>
    <div id="top-left">
      <h1 style = "color: #fffaba">Welcome to</h1>
      <h1 style = "color: #a9edfe">Elbow</h1>
      <h1 style = "color: #ffaaaa">Bumps!</h1>
    </div>
    <div id="bottom-left">
      <p></p>
      <p style =" color: #444444">Elbow Bump is a website that uses data provided by the user to recommend a match with someone with similar interests</p>
      <p style =" color: #444444">We would like you to answer a few quick questions to get started</p>
      <div id="button2"><Button id="button" @click="this.$root.route_to('/login');">Get Started!</Button></div>
    </div>
    <div id="bottom-right">
      <img src="../assets/pic.png" id="pic"/>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #fffaba;

#frame {
  position: absolute;
  height: 100%;
  width: 100%;
  margin-top: 4%;
  background: #ffffff;
}

#top-right {
  position: absolute;
  height: 50%;
  right: 0px;
  width: 50%;
  margin-right: 4%;
  background: $background-color;
}


#poster {
  position: absolute;
  //display: block;
  z-index: 0;
  margin-left: 40%;
  margin-top: 10%;
  border-radius: 50%;
}

#elb-poster {
  display: flex;
  object-fit: contain;
  height: 10rem;
  width: 10rem;
  margin-left: 36%;
  margin-top: 32%;
  z-index: 1;
  border-radius: 50%;
  background: $background-color;
}

#top-left {
  position: absolute;
  height: 50%;
  left: 0px;
  width: 50%;
  font-size: 50px;
  text-align: center;
  font-family: IBM Plex Sans;
  line-height: 35px;
  background: #ffffff;
}

#bottom-left {
  position: absolute;
  margin-top: 25%;
  margin-left:2%;
  height: 50%;
  left: 0px;
  width: 45%;
  font-size: 30px;
  font-family: IBM Plex Sans;
  line-height: 35px;
  background: #ffffff;
}

#button {
    //font-weight: bold;
    width: 30%;
    height: 5%;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    color: #ffffff;
    font-family: IBM Plex Sans;
    font-size: 35px;
    justify-content: center;
    background: $secondary-color;
    border: none;
}

#bottom-right {
  position: absolute;
  margin-top: 22.5%;
  margin-right: 2%;
  height: 50%;
  right: 0px;
  width: 50%;
  background: $primitive-color;
}

#pic {
  display: flex;
  object-fit: contain;
  height: 100%;
  width: 100%;
  z-index: 1;
  background: $primitive-color;
}
</style>

