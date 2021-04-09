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
        <div style="display: flex; justify-content: left; top: 0.2rem;">
            <IconButton style="margin: 0.2rem;" hint="What's this?"  @onClick="displayHint = true"/>
        </div>
        
        <EditableText 
        style="position: absolute; margin-left: -6rem; margin-top: 0; width: 80%;" 
        fullWidth="true" textID="intro" 
        placeholder="Describe yourself in a sentence or two (160 character limit)" 
        v-model:textVar="intro" />
        <Button style="position: absolute; right: 0rem; margin: 3rem;" icon="pi pi-save" label="Save" class="p-button-raised" @click="updateProfile" />
        <TabView class="profile-tab">
            <TabPanel header="Personal Info" style="margin-top: 6rem;">
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
            </TabPanel>
            <TabPanel header="Bio">
                <Dialog header="About your bio" v-model:visible="displayHint" >
                    <p>
                        This is where you can edit & view your bio. 
                    </p>
                    <p>
                         You can write your bio using <a href="https://zh.wikipedia.org/wiki/Markdown">Markdown</a> 
                         Here's a <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet">helpful Markdown cheatsheet</a>. 
                    </p>
                    <p>
                         A good bio is key to making a good first impression. 
                    </p>
                </Dialog>
                <Card>
                    <template #content>
                        <div style="display: flex; justify-content: space-between; width: 100%;">
                            <div style="display: flex; justify-content: left;">
                                <IconButton style="margin: 0.7rem;" hint="What's this?" icon="pi-question-circle" @onClick="displayHint = true"/>
                                <div> <p> You can edit your bio using markdown. Click on the tick to see what it looks like compiled. (2000 character limit) </p> </div>
                            </div>
                            <div style="display: flex; justify-content: right;">
                                <IconButton style="margin: 0.7rem;" hint="compile" icon="pi-check-circle" color="green" @onClick="compileMarkdown" />
                            </div>
                        </div>
                    </template>
                </Card>
                <Splitter>
                    <SplitterPanel class="p-d-flex p-ai-center p-jc-center">
                        <TextArea style="height: 36rem; width: 100%" v-model="bio" placeholder="Edit markdown document here..." />
                        <!-- <Editor v-model="bio" editorStyle="height: 36rem; width: 100%">
                            <template #toolbar>
                                <div style="display: flex; justify-contents: left;">
                                    <IconButton hint="compile" icon="pi-check-circle" color="green" @onClick="compileMarkdown" />
                                    <IconButton hint="save" icon="pi-save" color="blue" @onClick="saveDoc" />
                                </div>
                            </template>
                        </Editor> -->
                    </SplitterPanel>
                    <SplitterPanel class="p-d-flex p-ai-center p-jc-center">
                        <ScrollPanel style="height: 36rem; width: 100%">
                            <div class="rendered-markdown" ref="rendered_md">

                            </div>
                        </ScrollPanel>
                    </SplitterPanel>
                </Splitter>
            </TabPanel>
            <TabPanel header="Twitter">
                <div v-if="twitter != ''">
                    <p >Current Twitter account: @{{twitter}}</p>
                    <Button label="Refresh your sentiment scores for your current account or authorise a new Twitter account" autofocus @click="openURL()"></Button>
                </div>
                <div v-else>
                    <p> You haven't registered your Twitter account with us yet!</p>
                    <Button label="Authorise a new Twitter account" autofocus @click="openURL()"></Button>
                </div>

          
                <h2>Enter the PIN you recieved above</h2>
                <div id ="textbox">
                    <form @submit.prevent="submitPIN">
                    <label for="twitterPIN"></label>
                    <input
                        type="text"
                        id="twitterPIN"
                        name="twitterPIN"
                        v-model="twitterPIN" 
                        value @click="getValue"
                    />
                    <br /><br />
                    <div id="button"><Button type="submit" id="button">Submit</Button></div> <br /><br />
                    <Dialog v-model:visible="hasErrors" header="Oh no!" class="error">
                        {{ error }} <br/><br/>
                        <Button label="Got it!" autofocus @click="removeErrors"></Button>
                    </Dialog>
                    </form>
                </div>
            </TabPanel>
            <TabPanel header="Questionnaire">
          
                <p>Fill out the questionnaire</p>
                <div id ="textbox">
                    <Button label="Go to the questionnaire page" autofocus @click="questionnaireRoute()"></Button>
                    <Dialog v-model:visible="hasErrors" header="Oh no!" class="error">
                        {{ error }} <br/><br/>
                        <Button label="Got it!" autofocus @click="removeErrors"></Button>
                    </Dialog>
                </div>
            </TabPanel>
        </TabView>
    </div>
</div>
</section>
</template>

<script>

import axios from "axios";
import MarkdownIt from "markdown-it";

import EditableText from "../components/EditableText";
import IconButton from "../components/IconButton";

export default {
    components: { EditableText, IconButton },
    data(){
        return {
            displayHint: false,
            currentEdit: '',
            firstName: '',
            lastName: '',
            intro: '',
            email: '',
            phoneNumber: '',
            twitter: '',
            facebook: '',
            snapchat: '',
            instgram: '',
            telegram: '',
            personalSite: '',
            userId: "",
            avatar: "../assets/test.jpg",
            bio: "",
            markdown: null,
            twitterPIN: "",
            error: "",
            oauthToken: "",
            oauthTokenSecret: "",
            oauthURL: ""
        };
    },
    methods: {
        updateProfile: function(){

            let localURL = `${this.$store.getters.URL}user_data`;

            const form = new FormData()

            form.append('id', this.$store.getters.userId)
            form.append('phoneNum', this.phoneNumber)
            form.append('fName', this.firstName)
            form.append('sName', this.lastName)
            form.append('emailAdd', this.email)
            form.append('bio', this.bio)
            form.append('intro', this.intro)

            axios.post(localURL, form).then(
                (response) => {
                    if (response.data['STATUS_CODE'] == 200){
                        this.$store.dispatch("updateUserInfo", {fName: this.firstName, avatar: this.avatar});
                        this.$root.updateHeader();
                        
                        this.$root.displaySuccessLog("Save Successful!", 'Your new profile has been uploaded.');
                    }else{
                        this.$root.displayWarn("Update Profile Failed", response.data.Message);
                    }
                }
            ).catch(
                (e) => this.$root.displayError("Network Error", e)
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
                    this.bio = data['bio'];
                    this.intro = data['intro'];

                });
            }else{
                console.warn("not logged in")
            }
        },
        compileMarkdown(){
          let compiled = this.markdown.render(this.bio);
          this.$refs.rendered_md.innerHTML = compiled;
        },
        submitPIN() {
            let localURL = `${this.$store.getters.URL}/social_media_info`;

            const form = new FormData()

            form.append('id', this.$store.getters.userId)
            form.append('OAUTH_TOKEN', this.oauthToken)
            form.append('OAUTH_TOKEN_SECRET', this.oauthTokenSecret)
            form.append('pin', this.twitterPIN)
            axios
                .post(localURL, form)
                .then((res) => {
                if (res.data.STATUS_CODE == 200) {
                    this.$router.push("/matches");
                } else {
                    this.error = res.data.Message;
                }
                })
                .catch((err) => {
                console.log(err);
                });
            this.twitterUsername = "";
            this.$router.push('/profile');
        },
        removeErrors() {
            this.error = ""
        },
        generateURL() {
            if (this.oauthURL == ""){
            let localURL = `${this.$store.getters.URL}/twitter_oauth_url`;
            axios
            .post(localURL)
            .then((res) => {
                if (res.data.STATUS_CODE == 200) {
                this.oauthURL = res.data.oauthURL;
                this.oauthToken = res.data.oauthToken;
                this.oauthTokenSecret = res.data.oauthTokenSecret;   
                } else {
                this.error = res.data.Message;
                }
            })
            .catch((err) => {
                console.log(err);
            });}
            return this.oauthURL;
        },
        openURL(){
            window.open(this.generateURL(), "_blank");
        },
        questionnaireRoute(){
            this.$router.push('/questionnaire');
        }
    },
    mounted() {
        this.markdown = new MarkdownIt();
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

.profile-tab{
    position: absolute;
    margin-top: 6rem;
    left: 2rem;
    width: 85%;
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
    width: 80%;
    margin-top: 2rem;
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
