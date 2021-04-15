<template>
    <div>
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
}
</style>