<template>
    <div id="frame">
        <div class="content-section introduction">
            <div class="feature-intro">
                <h1 id="how-it-works" style = "color: #ffffff">HOW <span style = "color:  #a9edfe">IT</span> <span style = "color: #ffaaaa">WORKS</span></h1>
                <h3> <span class='pi pi-github'></span> <a href="https://github.com/bioBean/elbowbumps">  View our GitHub Repository</a></h3>
            </div>
            <AppDemoActions />
        </div>

        <div class="content-section implementation">

            <div class="card">
                <Timeline :value="events1" align="alternate" class="customized-timeline" style="background: #ffffff; padding:1rem;">
                     <template #marker="slotProps">
                        <span class="custom-marker p-shadow-2" :style="{backgroundColor: slotProps.item.color}">
                            <i :class="slotProps.item.icon"></i>
                        </span>
                    </template>
                    <template #content="slotProps">
                        <Card>
                            <template #title>
                                <div style="margin-right: 1rem; margin-left: 1rem; padding-top: 1rem;">
                                    {{slotProps.item.status}}
                                </div>
                            </template>
                            <template #subtitle>
                                <div style="margin-right: 1rem; margin-left: 1rem;"> 
                                    {{slotProps.item.date}}
                                </div>
                            </template>
                            <template #content>
                                <img v-if="slotProps.item.image" :src="'../assets/' + slotProps.item.image" :alt="slotProps.item.name" width="200" class="p-shadow-2" />
                                <p>{{slotProps.item.par}}</p>
                                <Button v-if="slotProps.item.link" :label="slotProps.item.linktext" class="p-button-text" @click="openLink(slotProps.item.link)"></Button>
                            </template>
                        </Card>
                    </template>
                </Timeline>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            events1: [
                {status: 'Questionnaire', date: 'Step 1', icon: 'pi pi-question', color: '#a9edfe',
                par: "In order to recommend other users with similar interests to you, we first need to gather data about your interests using a questionnaire in four key categories- music, film/tv, sports and video games. We combine your scores and store them in the database."},
                {status: 'Twitter Analysis', date: 'Step 2', icon: 'pi pi-twitter', color: '#ffe38f',
                 par: "If you give permission, we extract your Tweets related to our four key interest categories. We then perform sentiment analysis and store aggregrated scores in the database. To top it off, we also record scores for sub-categories related to our initial four categories if we detect them in your Tweets"},
                {status: 'Recommendation Algorithm', date: 'Step 3', icon: 'pi pi-user', color: '#ffaaaa',
                 par: "Using your category scores, we then map your score as an n-dimensional vector, n being the number of categories for which we have data gathered about your user. We then take the n-nearest neighbours of you in that n-dimensional space using an adaptation of a SQL query.", 
                 link: "http://nocurve.com/virtual-lab/nearest-neighbours-using-sql/", linktext:"Check out this blog post for more information on our recommendation algorithm"},
                {status: 'Bump Elbows and Make Friends', date: 'Step 4', icon: 'pi pi-check', color: '#80929F',
                 par: "With your neighbours calculated, we are able to recommend people to you who have the most in common with you, so that you're able to meet new people who feel as strongly about what you care as you do! If you bump someone and they bump you back you can get information on their socials and get in touch."}
            ]
        }
    },
    methods:{
        openLink(link) {
            window.open(link, "_blank");
        }
    }
}
</script>

<style lang="scss" scoped>

* {
    //margin-top: 4%;
    margin-bottom: 3%;
} 


h1,h3 {
    display: inline-block;
}

h3 {
    padding-top: 4%;
    float: right;
}

p {
    margin-right: 1rem;
    margin-left: 1rem;
    padding-bottom: 1rem;
}
.p-button-text {
    padding-top: 0;
    border-top: 0;
    bottom: 20%;
}

#frame {
  position: relative;
  height: auto;
  width: 100%;
  background:#80929F;
}

#how-it-works {
  font-size: 60px;
  font-family: 'Montserrat', sans-serif;
  text-align: left;

}

.custom-marker {
    display: flex;
    width: 2rem;
    height: 2rem;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    border-radius: 50%;
    z-index: 1;
}
::v-deep(.p-timeline-event-content)
::v-deep(.p-timeline-event-opposite) {
    line-height: 1;
}
@media screen and (max-width: 960px) {
    ::v-deep(.customized-timeline) {
            .p-timeline-event:nth-child(even) {
                flex-direction: row !important;
                
                .p-timeline-event-content {
                    text-align: left !important;
                }
            }
            .p-timeline-event-opposite {
                flex: 0;
            }
            .p-card {
                margin-top: 1rem;
            }
        }
}
</style>