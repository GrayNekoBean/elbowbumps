<template>
    <div>
        <br><br><br><br><br>
        <p>Data: {{dat}}</p>

        <ul id="example-1">
            <li v-for="item in dat" :key="item.uid_interest_type">
                {{ dat.uid_interest_type }}
                {{ dat.uid_interest_weight }}
            </li>
        </ul>

    </div>
</template>


<script>
import axios from "axios";
// import datatale from ""
export default {
    data(){
        return {dat:[]}
    },
    mounted(){
        axios.get(this.$store.getters.URL + "get_interest_data", {params: {user_id: this.$store.getters.userId}}).then(
            (response) => {
                if (response.data.STATUS_CODE == 200){
                    this.dat = response.data.Data;
                    this.$root.displayLog("Successfully fetched data!", this.dat);
                }
                else{
                    this.$root.displayLog("Data fetch failed");
                }
            }
        )
    }
}
</script>
