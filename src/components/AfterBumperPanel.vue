<template>
    <Card style="width: 16rem; height: 24rem;">
        <template #content>
            <div class="bumper-panel">
                <Avatar size="xlarge" :image="require('../assets/test.jpg')" shape="circle" />
                <h3>{{userName}}</h3>
                <p>{{intro}}</p>
                <p style="color:#bb2e2e; font-size:small;">Interests: {{interests}}</p>
            <!-- <Tag v-for="tag in tags" :key="tag" class="p-mr-2" :severity="getTagType(tag)" :value="tag.value" rounded></Tag> -->
                <div style="display: flex; justify-content: space-between;">
                    <IconButton hint="Report User" icon="pi-times" color="red" @click="reportUser()"></IconButton>
                </div>
            </div>
        </template>
    </Card>
</template>

<script>
import axios from "axios";
import IconButton from "./IconButton";

export default {
    data(){
        return {
            userName: "",
            interests: "",
            bio: "",
            twitter: "",
            tags: [],
            intro: "",
            firstName: "",
            lastName: "",
            email: "",
            avatar: require("../assets/test.jpg"),
        };
    },
    components: {IconButton},
    props: [ "userID" ],
    methods: {
        FetchUserInterests(){
            let args = {
                user_id: this.userID
            };
            axios.get(this.$store.getters.URL + "get_interests", {params: args}).then(
            (response) => {
                if (response.data.STATUS_CODE == 200){
                    let dat = response.data.Data;
                    // this.$root.displayLog("Fetching interest data successed", dat);
                    dat.forEach( interest =>{
                        this.interests = this.interests + " " + interest
                    });
                }
            });
        },
        FetchUserInfo(){
            let address = this.$store.getters.URL + "user_data";
            let args = {
                user_id: this.userID
            };
            let dataPack = null;
            axios.get(address, {params: args}).then(
                (response) => {
                    if (response.data.STATUS_CODE == "200"){
                        let data = response.data['data'];
                        this.avatar = data['avatar'];
                        this.firstName = data['fName'];
                        this.lastName = data['sName'];
                        this.twitter = data['twitter'];
                        this.bio = data['bio'];
                        this.intro = data['intro'];
                        this.userName = this.firstName + " " + this.lastName;
                        this.email = data['email']

                        if (this.avatar != ""){
                            this.avatar = "../assets/test.jpg";
                        }
                        if (this.intro == ""){
                            this.intro = "This person doesn't have an intro :( ";
                        }
                        if (this.bio == ""){
                            this.bio = "This person doesn't have an bio :( ";
                        }
                    }else{
                        console.error(response.STATUS);
                        console.error(response.Message);
                    }
                }
            ).catch((e) => {
                console.error(e);
            });
        },
        reportUser(){
            console.log(this.userID)
            this.$router.push({name:'report', params: {user_id: this.userID}});
        },
        openTwitterPage(){
            window.open("https://twitter.com/" + this.twitter, "_blank");
        },
        openEmail(){
            window.open("mailto:" + this.email, "_blank");
        }
    },
    mounted: function(){
        this.FetchUserInfo();
        this.FetchUserInterests();
    }
}
</script>

<style lang="scss" scoped>

.bumper-panel{
    display: flex;
    flex-flow: column;
    justify-content: space-around;
    align-items: center;
    height: 24rem;
    width: 16rem;
}

.edit-icon{
    height: 2rem;
    width: 2rem;
    padding: 25%;
    cursor: pointer;
}

.edit-button-blue{
    color: rgb(29, 161, 242);
    :hover{
        border-radius: 50%;
        background: rgba(29, 161, 242, 0.3);
    }
}

.edit-button-red{
    color: rgb(128, 16, 16);
    :hover{
        border-radius: 50%;
        background: rgba(128, 16, 16, 0.3);
    }
}
</style>