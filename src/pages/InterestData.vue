<template>
    <div>
        <h2 style="text-align: center; margin-top:5rem; padding-top: 3rem;"> Want to know more about your interests? You are in the right place!</h2>
        <graphs></graphs>
    </div>
</template>


<script>
import axios from "axios";
import Graphs from '../components/Graphs.vue'

export default {
    components: { Graphs },
}
</script> 

<style scoped>
* {
    margin-top: 4%;
    margin-bottom: 4%;
}


</style>