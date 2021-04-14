<template>
<section>

<div class="profile-page">
        <TabView class="profile-tab" style="margin-top: 3rem;">
            <TabPanel header="New Matches" style="margin-top: 0rem;">
                    <Matches> </Matches>
            </TabPanel>
            <TabPanel header="Accepted Bumps">
                <Bumps></Bumps>
            </TabPanel>

        </TabView>
    
</div>
</section>
</template>

<script>

import axios from "axios";
import MarkdownIt from "markdown-it";


import Matches from "./Matches";
import Bumps from "./Bumps";

export default {
    components: { Matches, Bumps },
   
       
}
</script>

<style lang="scss" scoped>

$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #fffaba;



</style>
