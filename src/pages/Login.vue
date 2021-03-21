<template>
  <section>
    <div id="frame">
      <div id="login-left">
        <div id="poster-div">
          <img src="../assets/elbows-w-lines.png" id="elb-poster" />
        </div>
      </div>
      <div id="login-right">
        <LoginPanel></LoginPanel>
      </div>
    </div>
  </section>
</template>

<script>

import LoginPanel from "../components/LoginPanel";

export default {
  components: { LoginPanel },
  data() {
    return {};
  },
  methods: {}
}
</script>

<style lang="scss" scoped>
$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #fffaba;

#background {
  position: absolute;
  object-fit: contain;
  object-position: 0px, 0px;
  filter: blur(10px);
}

#frame {
  position: absolute;
  height: 100%;
  width: 100%;
}

#login-right {
  position: absolute;
  right: 0px;
  width: 50%;
}

#login-left {
  position: absolute;
  height: 100%;
  left: 0px;
  width: 50%;
  background: $primitive-color;
}

#poster-div {
  position: absolute;
  //display: block;
  width: 100%;
  z-index: 0;
  background: #a9edfe;
}

#elb-poster {
  display: flex;
  object-fit: contain;
  height: 10rem;
  width: 10rem;
  margin-left: 36%;
  margin-top: 20%;
  z-index: 1;
  border-radius: 50%;
  background: $background-color;
}
</style>
