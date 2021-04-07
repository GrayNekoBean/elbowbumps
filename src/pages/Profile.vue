<template>
<section>

<div class="profile-page">
    <div class="top-part">
        <div class="profile-title">
            <img src="../assets/test.jpg" class="avatar" />
            <!-- <FileUpload mode="basic" name="image" :customUpload="true" @uploader="uploadAvatar" /> -->
            <div class="user-name">
                <h2>
                    {{firstName}} {{lastName}}
                </h2>
            </div>
        </div>
    </div>
    <div class="bottom-part">
        <EditableText style="position: absolute; margin-left: -6rem; margin-top: 0; width: 80%;" fullWidth="true" textID="bio" v-model:textVar="bio"></EditableText>
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
        </div>
        <Button style="position: absolute; right: 2rem; bottom: 4rem;" icon="pi pi-save" label="Save" class="p-button-raised" @click="updateProfile" />
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
            bio: '',
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
        updateProfile: function(){

            let localURL = `${this.$store.getters.URL}/user_data`;

            const form = new FormData() 

            form.append('id', this.$store.getters.userId)
            form.append('phoneNum', this.phoneNumber)
            form.append('fName', this.firstName)
            form.append('sName', this.lastName)
            form.append('emailAdd', this.email)

            axios.post(localURL, form).then(
                (response) => {
                    if (response.data['STATUS_CODE'] == 200){
                        console.log(this.$store.getters.userId)
                        console.log(this.firstName)
                        console.log(this.email)
                        console.log(this.phoneNumber)
                        console.log('Updating profile successful');
                    }else{
                        console.log(this.$store.getters.userId)
                        console.log(this.firstName)
                        console.log(this.email)
                        console.log(this.phoneNumber)
                        console.warn("Issues with updating profile");
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
    position: absolute;
    padding: 2rem;
    //margin-top: 30%;
    height: 15rem;
    width: 15rem;
    border-radius: 50%;
}

.profile-page{
}

h2{
    color: black;
}

.user-name{
    text-align: center;
    margin-top: 4%;
    margin-left: 18%;
}

.top-part{
    display: flex;
    height: 30%;
    flex-flow: row;
    justify-content: left;
    background: $primitive-color;
}

.profile-title{
    display: flex;
    flex-flow: row;
    justify-content: left;
    margin-top: 12%;
    width: 100%;
}

.bottom-part{
    display: flex;
    justify-content: center;
    //align-content: center;
    height: 80%;
}

.info-area{
    width: 60%;
    margin-top: 8rem;
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
