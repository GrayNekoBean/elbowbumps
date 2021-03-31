<template>
    <div>
        <Card>
            <template #content>
            <div class="info-area">
                <Avatar :image="require('../assets/test.jpg')" class="avatar-area" size="xlarge" shape="circle"/>
                <div class="name-and-bio">
                    <h3> {{ userName }} </h3>
                    <p> {{ bio }} </p>
                </div>
                <Card style="position: absolute; margin-left: 60%; height: 20%; width: 30%; z-index: 10;" v-if="showBumpCard">
                    <template #header>
                        <h4>What do you what to say to him/her?</h4>
                    </template>
                    <template #content>
                        <InputText style="margin: 2%; width: 90%;" type="text" v-model="value"></InputText>
                        <br>
                        <div style="display: flex; justify-content: space-around;">
                            <Button @click="() => showBumpCard = false"> Cancle </Button>
                            <Button @click="confirmBump"> Confirm </Button>
                        </div>
                    </template>
                </Card>
                <Button @click="bump" style="height: 3rem; margin-top: 1.5rem;">
                    Bump!
                </Button>
                <div class="edit-button-blue lower">
                <i title="View Twitter" class="pi pi-twitter edit-icon" @click="openTwitterPage"></i>
                </div>
                <div class="edit-button-red lower">
                <i title="Block this user" class="pi pi-times edit-icon" @click="blockUser"></i>
                </div>
            </div>
            </template>
        </Card>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return {
            userName: "",
            avatar: require("../assets/test.jpg"),
            bio: "",
            twitter: "",
            bumpMsg: "",
            showBumpCard: ""
        }
    },
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
                            this.bio = "This person don't have a bio."
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
        }
    },
    mounted: function(){
        this.FetchUserInfo();
    }
}
</script>

<style lang="scss" scoped>

.info-area{
    display: flex;
    flex-flow: row;
    justify-content: space-between;
    height: 6rem;
}

.avatar-area{
    margin: 1rem;
}

.name-and-bio{
    display: block;
    text-align: left;
    width: 60%;
}

.edit-icon{
    height: 2rem;
    width: 2rem;
    padding: 25%;
    cursor: pointer;
}

.lower{
    margin-top: 2rem;
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