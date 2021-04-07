<template>
    <div>
        <Card>
            <template #header>
                <h3>People I bumped with</h3>
                <p>You have bumped {{ bumpUserIDs.length }}</p>
            </template>
            <template #contents>
                <ScrollPanel>
                    
                </ScrollPanel>
            </template>
        </Card>
    </div>
</template>

<script>
import getUserData from "../tools/getUserData";

export default {
    data(){
        return {
            bumpUserIDs: [],
            bumpedUserIDs: [],
            bumpLoaded: 0,
            bumpedLoaded: 0
        }
    }
}
</script>