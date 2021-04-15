<template>
    <div>
        <graphs></graphs>
        <interest-data-table/>
    </div>
</template>


<script>
import Graphs from '../components/Graphs.vue'
import InterestDataTable from '../components/InterestDataTable.vue'

export default {
    components: { Graphs, InterestDataTable },
}
</script> 

<style scoped>
* {
    margin-top: 4%;
}
</style>