<template>
  <div id="frame">
    <br>
    <h1 id="about-us" style = "color: #ffffff">THE BRAINS BEHIND <span style = "color:  #a9edfe">ELBOW</span> <span style = "color: #ffaaaa">BUMPS</span></h1>
    <hr class="solid">
    <br>
    <br>
    <br>
    <div id="bottom">
       <div class="column">
        <div id="rectangle"></div>
        <div class="card">
          <img class="img-circular" src="../assets/zoya.jpg" alt="Zoya">
          <div class="container">
            <div id="name">
            <h2>Zoya Anwar</h2>
            </div>
            <p class="title">CEO</p>
            <!-- <p>Some text that describes me lorem ipsum ipsum lorem.</p> -->
          </div>
        </div>
      </div>

      <div class="column">
        <div class="card">
          <div id="rectangle"></div>
          <img class="img-circular" src="../assets/eve.jpg" alt="Eve" style="width:100%">
          <div class="container">
            <div id="name"> 
            <h2>Eve Ashton</h2>
            </div>
            <p class="title">CEO</p>
            <!-- <p>Some text that describes me lorem ipsum ipsum lorem.</p> -->
          </div>
        </div>
      </div>

        <div class="column">
        <div class="card">
          <div id="rectangle"></div>
          <img class="img-circular" src="../assets/faridz.jpg" alt="Faridz" style="width:100%">
          <div class="container">
            <div id="name">
            <h2>Faridz Ibrahim</h2>
            </div>
            <p class="title">CEO</p>
            <!-- <p>Some text that describes me lorem ipsum ipsum lorem.</p> -->
          </div>
        </div>
      </div>

        <div class="column">
        <div class="card">
          <div id="rectangle"></div>
          <img class="img-circular" src="../assets/lily.jpg" alt="Lily" style="width:100%">
          <div class="container">
            <div id="name">
            <h2>Lily Nicholson</h2>
            </div>
            <p class="title">CEO</p>
            <!-- <p>Some text that describes me lorem ipsum ipsum lorem.</p> -->
          </div>
        </div>
      </div>

        <div class="column">
        <div class="card">
          <div id="rectangle"></div>
          <img class="img-circular" src="../assets/matthew.jpg" alt="Matthew" style="width:100%">
          <div class="container">
            <div id="name">
            <h2>Matthew Oladimeji</h2>
            </div>
            <p class="title">CEO</p>
            <!-- <p>Some text that describes me lorem ipsum ipsum lorem.</p> -->
          </div>
        </div>
      </div>

        <div class="column">
        <div class="card">
          <div id="rectangle"></div>
          <img class="img-circular" src="../assets/naomi.jpg" alt="Naomi" style="width:100%">
          <div class="container">
            <div id="name">
            <h2>Naomi Felix</h2>
            </div>
            <p class="title">CEO</p>
            <!-- <p>Some text that describes me lorem ipsum ipsum lorem.</p> -->
          </div>
        </div>
      </div>

        <div class="column">
        <div class="card">
          <div id="rectangle"></div>
          <img class="img-circular" src="../assets/derek.jpg" alt="Derek" style="width:100%">
          <div class="container">
            <div id="name">
            <h2>Derek Wang</h2>
            </div>
            <p class="title">CEO</p>
            <!-- <p>Some text that describes me lorem ipsum ipsum lorem.</p> -->
          </div>
        </div>
      </div>

        <div class="column">
        <div class="card">
          <div id="rectangle"></div>
          <img class="img-circular" src="../assets/bijan.jpg" alt="Bijan" style="width:100%">
          <div class="container">
            <div id="name">
            <h2>Bijan Parsia</h2>
            </div>
            <p class="title">Intern</p>
            <!-- <p>Some text that describes me lorem ipsum ipsum lorem.</p> -->
          </div>
        </div>
      </div>

      
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
$background-color: 	#80929F;

.solid {
  background: #ffff;
  height: 0.5%;
}

#frame {
  position: relative;
  height: 100%;
  width: 100%;
  padding: 2.5%;
  background: $background-color;
}

#about-us {
  padding-top: 3vw;
  margin-bottom: 0;
  font-size: 60px;
  font-family: 'Montserrat', sans-serif;
  text-align: left;

}

#name {
  height: 4vw;
}

h2 {
  line-height: 110%;
  font-family: 'Montserrat', sans-serif;
}


@media screen and (min-width: 1501px) {
.column {
  float: left;
  width: 12.5%;
  margin-bottom: 16px;
  padding: 0 8px;
}
}

/* Display the columns below each other instead of side by side on small screens */
@media screen and (max-width: 1000px) {
  .column {
    width: 100%;
    display: block;
  }
}

@media screen and (max-width: 1500px) and (min-width: 1000px) {
  .column {
    float: left;
    width: 25%;
    margin-bottom: 8px;
    padding: 0 5px;
  }
}


.card {
  z-index:10;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background: linear-gradient( 180deg, $primitive-color, $primitive-color  30%, white 30%, white 60%, white 60% ); 
}


.container {
  padding: 0 16px;
}



.title {
  color: grey;
  padding: 4px;
}

.img-circular {
  position: relative;
  width: 100%;
  height: 75%;
  overflow: hidden;
  border-radius: 50%;
}

.img-circular img {
  width: 100%;
  height: auto;
}


</style>