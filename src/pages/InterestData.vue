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
    mounted(){
        axios.get(this.$store.getters.URL + "get_interest_data", {params: {user_id: this.$store.getters.userId}}).then(
            (response) => {
                if (response.data.STATUS_CODE == 200){
                    // let dat = response.data.Data;
                    // this.$root.displayLog("Fetching interest data successed", dat);
                }
            }
        )
    }
}
</script> 