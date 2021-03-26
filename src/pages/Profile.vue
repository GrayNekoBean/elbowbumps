<template>
<section>

<div class="profile-page">
    <div class="top-part">
        <div class="profile-title">
            <img src="../assets/test.jpg" class="avatar" />
            <FileUpload mode="basic" name="image" :customUpload="true" @uploader="uploadAvatar" />
            <div style="text-align: center;">
                <h2>
                    {{firstName}} {{lastName}}
                </h2>
            </div>
        </div>
    </div>
    <div class="bottom-part">
        <div class="info-area">
            <div class="names">
            <EditableText textID="first_name" v-model:textVar="firstName">
                First Name
            </EditableText>
            <EditableText textID="surname" v-model:textVar="lastName">
                Surname
            </EditableText>
            </div>
            <div class="contacts">
            <EditableText textID="email" v-model:textVar="email">
                Email
            </EditableText>
            <EditableText textID="telephone" v-model:textVar="phoneNumber">
                Phone Number
            </EditableText>
            </div>
            <div class="social-media">
            <EditableText textID="twitter" v-model:textVar="twitter">
                Twitter
            </EditableText>
            </div>
            <div class="buttons">
            <Button @click="logout">
                Logout
            </Button>
            <Button @click="updateProfile">
                Save
            </Button>
            <Button id="button" @click="$router.push('Matches')">
            Matching Page
            </Button>
            <Button id="button" @click="$router.push('SocialMediaInfo')">
            Twitter
            </Button>
            </div>
        </div>
    </div>
</div>
</section>
</template>

<script>

import axios from "axios";
import EditableText from "../components/EditableText";

export default {
    components: { EditableText },
    data(){
        return {
            currentEdit: '',
            firstName: '',
            lastName: '',
            email: '',
            phoneNumber: '',
            twitter: '',
            facebook: '',
            snapchat: '',
            instgram: '',
            telegram: '',
            personalSite: '',
            userId: "",
            avatar: "../assets/test.jpg"
        };
    },
    methods: {
        logout: function(){
            sessionStorage.removeItem("current_user");
            localStorage.removeItem("current_user");

            this.$store.dispatch("logOut");
            this.$root.setLogoutState();
            this.$root.route_to('/');
        },
        updateProfile: function(){
            let profileData = {
                userId: this.$store.getters.userId,
                data: {
                    fName: this.firstName,
                    sName: this.lastName,
                    emailAdd: this.email,
                    phone: this.phoneNumber,
                    twitter: this.twitter,
                }
            };

            axios.post(this.$store.getters.URL + "user_info", profileData).then(
                (response) => {
                    if (response.data['STATUS_CODE'] == 200){
                        console.log('upload avatar successful!');
                    }else{
                        console.warn("Issues happened when updating avatar.");
                        console.log(response);
                    }
                }
            ).catch(
                (e) => console.error(e)
            );
        },
        uploadAvatar: function(event){
            let header = {Authorization: 'Client-ID 7a7f16c6427fe66'};
            let postData = {
                image: event.files[0],
                name: "elbowbumps_avatar_"+this.$store.getters.userId,
                //album: "X1mK7aP",
                type: "file"
            }

            let formData = new FormData();
            for (let dat in postData){
                formData.append(dat, postData[dat]);
            }

            axios.post('https://api.imgur.com/3/image', formData, {headers: header}).then(
                (response) => {
                    this.avatar = response.data.id;
                    let updateAvatarData = {
                        userId: this.$store.getters.userId,
                        data: {avatar: this.avatar}
                    };
                    axios.post(this.$store.getters.URL + "/user_info", updateAvatarData).then(
                        (response) => {
                            if (response.data['STATUS_CODE'] == 200){
                                console.log('upload avatar successful!');
                            }else{
                                console.warn("Issues happened when updating avatar.");
                                console.log(response);
                            }
                        }
                    ).catch(
                        (e) => {console.error(e);}
                    )
                }
            ).catch((e) => {
                console.error(e)
            });
        },
        switchEditable: function(target){
            let inputText = target.getAttribute('id');
            if (this.currentEdit == inputText){
                this.currentEdit = "";
            }else{
                this.currentEdit = inputText;
            }
        },
        editable: function(target){
            if (target != null){
                let text = target.getAttribute('id');
                return text == this.currentEdit;
            }else{
                return false;
            }
        },
        getCurrentUserInfo: function(){

            if (this.$store.getters.userId){

                let getterInfo = {
                    user_id: this.$store.getters.userId
                };

                axios.get(this.$store.getters.URL + 'user_data', {params: getterInfo})
                .then((response) => {
                    let data = response.data['data'];
                    this.avatar = data['avatar'];
                    this.firstName = data['fName'];
                    this.lastName = data['sName'];
                    this.email = data['email'];
                    this.phoneNumber = data['phone'];
                    this.twitter = data['twitter'];

                });
            }else{
                console.warn("not logged in")
            }
        }
    },
    mounted() {
        this.getCurrentUserInfo();
    }
}
</script>

<style lang="scss" scoped>

$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #fffaba;

.avatar{
    margin-top: 30%;
    height: 15rem;
    width: 15rem;
    border-radius: 50%;
}

.profile-page{
}

h2{
    color: black;
}

.top-part{
    display: flex;
    height: 30%;
    flex-flow: row;
    justify-content: center;
    background: $primitive-color;
}

.profile-title{
    display: flex;
    flex-flow: column;
    justify-content: center;
}

.bottom-part{
    display: flex;
    justify-content: center;
    align-content: center;
    height: 80%;
}

.info-area{
    width: 60%;
}

.names{
    display: flex;
    justify-content: space-between;
}

.contacts{
    display: flex;
    justify-content: space-between;
}

.social-media{
    display: flex;
    justify-content: center;
}

.buttons{
    display: flex;
    justify-content: space-around;
    margin-bottom: 10%;
}

</style>
