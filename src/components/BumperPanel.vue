<template>
    <Card style="width: 16rem; height: 24rem;">
        <template #content>
            <div class="bumper-panel">
                <Avatar size="xlarge" :image="require('../assets/test.jpg')" shape="circle" />
                <h3>{{userName}}</h3>
                <p>{{bio}}</p>
                <Tag v-for="tag in tags" :key="tag" class="p-mr-2" :severity="getTagType(tag)" :value="tag.value" rounded></Tag>
                <Button @click="bump">Bump</Button>
                <div style="display: flex; justify-content: space-between;">
                    <IconButton hint="Open Page Twitter" icon="pi-twitter" color="rgb(29, 161, 242)" @click="openTwitterPage()"></IconButton>
                    <IconButton hint="Block User" icon="pi-times" color="red" @click="blockUser()"></IconButton>
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
                        dataPack = response.data.data;
                        this.userName = `${dataPack.fName} ${dataPack.sName}`;
                        if (dataPack.avatar != ""){
                            this.avatar = dataPack.avatar;
                        }else{
                            this.avatar = "../assets/test.jpg";
                        }
                        if (dataPack.bio){
                            this.bio = dataPack.bio;
                        }else{
                            this.bio = "This person don't have a bio.";
                        }
                        this.twitter = dataPack.twitter;
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
            this.showBumpCard = true;
            console.log("bumped");
        },
        confirmBump(){
            console.log("Send Bump message: " + this.bumpMsg);
        },
        blockUser(){
            return null;
        },
        openTwitterPage(){
            return null;
        }
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