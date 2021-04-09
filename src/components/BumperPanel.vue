<template>
    <Card style="width: 16rem; height: 24rem;">
        <template #content>
            <div class="bumper-panel">
                <Avatar size="xlarge" :image="require('../assets/test.jpg')" shape="circle" />
                <h3>{{userName}}</h3>
                <p>{{intro}}</p>
                <Tag v-for="tag in tags" :key="tag" class="p-mr-2" :severity="getTagType(tag)" :value="tag.value" rounded></Tag>
                <Button @click="bump">Bump</Button>
                <div style="display: flex; justify-content: space-between;">
                    <IconButton hint="Block User" icon="pi-times" color="red" @click="reportUser()"></IconButton>
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
            bio: "",
            twitter: "",
            tags: [],
            intro: "",
            firstName: "",
            lastName: "",
            avatar: require("../assets/test.jpg"),
        };
    },
    components: {IconButton},
    props: [ "userID" ],
    methods: {
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
        bump(){
            // this.showBumpCard = true;
            // console.log("bumped");
            const URL = `${this.$store.getters.URL}bump`;
            console.log(`${this.$store.getters.userId} ${this.userID}`);
            const form = new FormData();
            form.append("userId", this.$store.getters.userId);
            form.append("matchId", this.userID);
            axios.post(URL, form).then((res) => {
                if (res.data.STATUS_CODE == "200") {
                console.log("success!");
                }
            });
        },
        confirmBump(){
            console.log("Send Bump message: " + this.bumpMsg);
        },
        reportUser(){
            console.log(this.userID)
            this.$router.push({name:'report', params: {user_id: this.userID}});
        },
        openTwitterPage(){
            window.open("https://twitter.com/" + this.twitter, "_blank");
        },
    },
    mounted: function(){
        this.FetchUserInfo();
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