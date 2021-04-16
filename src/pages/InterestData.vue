<template>
    <div>
        <h2 style="text-align: center; margin-top:5rem; padding-top: 3rem;"> Want to know more about your interests? You are in the right place!</h2>
        <Graphs :userId="$store.getters.userId" :showTable="true"></Graphs>
    </div>
</template>


<script>
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