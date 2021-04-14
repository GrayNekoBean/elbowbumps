<template>
    <div class="splited-frame">
        <div class="splited-left" :style="leftRatio()">
            <slot name="left"></slot>
        </div>
          
        <div class="splited-right" :style="rightRatio()">
            <slot name="right"></slot>
        </div>
    </div>
</template>

<script>
export default {
  props: {
    ratio: {
      type: Number,
      default: 0.5
    }
  },
  methods: {
    leftRatio(){
      let r = (this.ratio * 100)
      return `width: ${r}%`;
    },
    rightRatio(){
      let r = ((1 - this.ratio) * 100)
      return `width: ${r}%`;
    }
  },
  mounted(){
    if (this.ratio >= 1){
      console.warn("Splited Page abnormal ratio, please make ratio a number less than 1.");
      this.$emit("update:ratio", 0.5);
    }
  }
}
</script>

<style lang="scss">

$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: 	#80929F;

.splited-frame {
  position: absolute;
  height: 100%;
  width: 100%;
}

.splited-right {
  position: absolute;
  z-index: 1;
  box-shadow: 0px 0px 3px 0px;
  height: 100%;
  right: 0px;
  width: 50%;
}

.splited-left {
  position: absolute;
  z-index: 0;
  height: 100%;
  left: 0px;
  width: 50%;
  background: $primitive-color;
}

</style>