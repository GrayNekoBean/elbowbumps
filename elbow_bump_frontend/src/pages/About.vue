<template>
  <div>
      <h1>About Us</h1>

  </div>
  <div id="frame">
    <div id="top">
      <img src="../assets/pic2.png" id="pic2"/>
    </div>
    <div id="bottom">
      <h3>Having trouble making friends during covid?</h3>

      <p style =" color: #444444"> Elbow bumps is here to help!<br> Elbow Bumps is an interest-based friend recommendation platform, 
          which will allow you to find other people whose interests closely match yours. 
          You can either provide us with your twitter account or answer a few short questions so we can get to know your
          interests. Then, you can get a list of matches, 'bump' with them, and get chatting!<br><br>

          Register <router-link to="/register">here</router-link> to get started and beat lockdown loneliness.<br><br>

          <i>For more on the terms of use of our website, and how we use your data, please read our <router-link to="/terms">Terms and Conditions</router-link> and <router-link to="/privacy">Privacy Policy</router-link></i>
          
        </p>
    </div>

  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss">
$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #fffaba;

#frame {
  position: absolute;
  height: 100%;
  width: 100%;
  background: #ffffff;
}

#top {
  position: absolute;
  height: 50%;
  left: 0px;
  width: 100%;
  margin-right: 4%;
  background: $primitive-color;
}

#bottom {
  position: absolute;
  margin-top: 22%;
  height: 50%;
  left: 0px;
  width: 100%;
  margin-right: 4%;
  font-size: 30px;
  text-color: #444444;
  text-align: center;
  font-family: IBM Plex Sans;
  line-height: 35px;
  background: #ffffff;
}

#pic2 {
  display: flex;
  object-fit: contain;
  height: 100%;
  width: 100%;
  z-index: 1;
  background: $primitive-color;
}

</style>