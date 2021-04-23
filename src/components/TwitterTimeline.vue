<template>
<div id="tl-container" ref="frame">
  <a
    class="twitter-timeline"
    :href="`https://twitter.com/${twitter}?ref_src=twsrc%5Etfw`"
  ></a>
</div>
</template>

<script>
export default {
  props: ["twitter"],
  mounted() {
    let twitterFeed = document.createElement("script");
    twitterFeed.setAttribute("src", "https://platform.twitter.com/widgets.js");
    document.head.appendChild(twitterFeed);
  },
  methods: {
    load(){
        //this.$refs.frame.innerHTML = `<a class="twitter-timeline" href="https://twitter.com/${this.twitter}?ref_src=twsrc%5Etfw"></a>`;
        //eval("twttr.widgets.load();");
    }
  }
};
</script>