<template>
    <div>
        <graphs></graphs>
        <interest-data-table/>
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
}
</style>