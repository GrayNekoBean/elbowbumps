<template>
  <section>
    <div class="profile-page">
      <div class="top-part">
        <div class="profile-title">
          <img :src="avatar" class="avatar" />
          <!-- <FileUpload mode="basic" name="image" :customUpload="true" @uploader="uploadAvatar" /> -->
          <div class="user-name">
            <h2>{{ firstName }} {{ lastName }}</h2>
          </div>
        </div>
      </div>
      <div class="bottom-part">
        <div style="display: flex; justify-content: left; top: 0.2rem">
          <IconButton
            style="margin: 0.2rem"
            hint="What's this?"
            @onClick="displayHint = true"
          />
        </div>

        <EditableText
          style="
            position: absolute;
            margin-left: -6rem;
            margin-top: 0;
            width: 80%;
          "
          fullWidth="true"
          textID="intro"
          placeholder="Describe yourself in a sentence or two (160 character limit)"
          v-model:textVar="intro"
          @onSave="updateProfile"
        />
        <TabView class="profile-tab">
          <TabPanel header="Personal Info" style="margin-top: 6rem">
            <Dialog header="Welcome to Elbow Bumps!" v-model:visible='firstRegister'>
              <p>
                If you would like to get more accurate results, go to the Twitter tab on this page and log into your Twitter!
              </p>
              <p>
                Once you're ready to see your matches, open the hamburger menu on the top right and select "My Matches"!
              </p>
              <Button @click='toggleIt'>Okay!</Button>
            </Dialog>
            <div class="info-area">
              <div class="names">
                <EditableText textID="first_name" v-model:textVar="firstName" @onSave="updateProfile">
                  First Name
                </EditableText>
                <EditableText textID="surname" v-model:textVar="lastName" @onSave="updateProfile">
                  Surname
                </EditableText>
              </div>
              <div class="contacts">
                <EditableText textID="email" v-model:textVar="email" @onSave="updateProfile">
                  Email
                </EditableText>
                <EditableText textID="telephone" v-model:textVar="phoneNumber" @onSave="updateProfile">
                  Phone Number
                </EditableText>
              </div>
            </div>
          </TabPanel>
          <TabPanel header="Bio">
            <Dialog header="About your bio" v-model:visible="displayHint" @onSave="updateProfile">
              <p>This is where you can edit & view your bio.</p>
              <p>
                You can write your bio using
                <a href="https://zh.wikipedia.org/wiki/Markdown">Markdown</a>
                Here's a
                <a
                  href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
                  >helpful Markdown cheatsheet</a
                >.
              </p>
              <p>A good bio is key to making a good first impression.</p>
            </Dialog>
            <Card>
              <template #content>
                <div
                  style="
                    display: flex;
                    justify-content: space-between;
                    width: 100%;
                  "
                >
                  <div style="display: flex; justify-content: left">
                    <IconButton
                      style="margin: 0.7rem"
                      hint="What's this?"
                      icon="pi-question-circle"
                      @onClick="displayHint = true"
                    />
                    <div>
                      <p>
                        You can edit your bio using markdown. Click on the tick
                        to see what it looks like compiled. (2000 character
                        limit)
                      </p>
                    </div>
                  </div>
                  <div style="display: flex; justify-content: right">
                    <IconButton
                      style="margin: 0.7rem"
                      hint="compile"
                      icon="pi-check-circle"
                      color="green"
                      @onClick="compileMarkdown"
                    />
                    <IconButton
                      style="margin: 0.7rem"
                      hint="save"
                      icon="pi-pencil"
                      color="green"
                      @onSave="save"
                    />
                  </div>
                </div>
              </template>
            </Card>
            <Splitter style="margin-bottom: 6rem;">
              <SplitterPanel class="p-d-flex p-ai-center p-jc-center">
                <TextArea
                  style="height: 36rem; width: 100%"
                  v-model="bio"
                  placeholder="Edit markdown document here..."
                />
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
                <ScrollPanel style="height: 36rem; width: 42rem;">
                  <div class="rendered-markdown" ref="rendered_md"></div>
                </ScrollPanel>
              </SplitterPanel>
            </Splitter>
          </TabPanel>
          <TabPanel header="Twitter">
            <div v-if="twitter != ''">
              <p>Current Twitter account: @{{ twitter }}</p>
               <Button
                label="Authorise a new Twitter account"
                autofocus
                @click="openURL()"
                style="margin-right:3rem;"
              ></Button>
                <Button
                label="Refresh your sentiment scores for your current account"
                autofocus
                @click="refreshTwitter()"
                style="margin-left:30%;"
              ></Button>
            </div>
            <div v-else>
              <p>You haven't registered your Twitter account with us yet!</p>
              <Button
                label="Authorise a new Twitter account"
                autofocus
                @click="openURL()"
              ></Button>
            </div>

            <h2 v-if="userAuthoriseTwitter != false">Enter the PIN you recieved above</h2>

         
              <div v-if="userAuthoriseTwitter != false" id="textbox">
                <form @submit.prevent="submitPIN">
                  <label for="twitterPIN"></label>
                  <input
                    type="text"
                    id="twitterPIN"
                    name="twitterPIN"
                    v-model="twitterPIN"
                    value
                    @click="getValue"
                  />
                  <br /><br />
                  <div id="button">
                    <Button type="submit" id="button">Submit</Button>
                  </div>
                  <br /><br />
                  <Dialog
                    v-model:visible="hasErrors"
                    header="Oh no!"
                    class="error"
                  >
                    {{ error }} <br /><br />
                    <Button
                      label="Got it!"
                      autofocus
                      @click="removeErrors"
                    ></Button>
                  </Dialog>
                </form>
              </div>

          </TabPanel>
          <TabPanel header="Questionnaire">
            <p>Fill out the questionnaire</p>
            <div id="textbox">
              <Button
                label="Go to the questionnaire page"
                autofocus
                @click="questionnaireRoute()"
              ></Button>
              <Dialog v-model:visible="hasErrors" header="Oh no!" class="error">
                {{ error }} <br /><br />
                <Button
                  label="Got it!"
                  autofocus
                  @click="removeErrors"
                ></Button>
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
import Markdown from "markdown-it";
import emoji from "markdown-it-emoji";

import EditableText from "../components/EditableText";
import IconButton from "../components/IconButton";

export default {
  components: { EditableText, IconButton },
  data() {
    return {
      displayHint: false,
      currentEdit: "",
      firstName: "",
      lastName: "",
      intro: "",
      email: "",
      phoneNumber: "",
      twitter: "",
      facebook: "",
      snapchat: "",
      instgram: "",
      telegram: "",
      personalSite: "",
      userId: "",
      avatar: "../assets/test.jpg",
      bio: "",
      markdown: null,
      twitterPIN: "",
      error: "",
      oauthToken: "",
      oauthTokenSecret: "",
      oauthURL: "",
      userAuthoriseTwitter: false
    };
  },
  computed: {
    firstRegister() {
      return this.$store.getters.firstRegister
    }
  },
  methods: {
    toggleIt() {
      this.$store.dispatch('toggleFirstRegister')
    },
    updateProfile: function () {
      let localURL = `${this.$store.getters.URL}user_data`;

      const form = new FormData();

      form.append("id", this.$store.getters.userId);
      form.append("phoneNum", this.phoneNumber);
      form.append("fName", this.firstName);
      form.append("sName", this.lastName);
      form.append("emailAdd", this.email);
      form.append("bio", this.bio);
      form.append("intro", this.intro);

      axios
        .post(localURL, form)
        .then((response) => {
          if (response.data["STATUS_CODE"] == 200) {
            this.$store.dispatch("updateUserInfo", {
              fName: this.firstName,
              avatar: this.avatar,
            });
            this.$root.updateHeader();

            this.$root.displaySuccessLog(
              "Save Successful!",
              "Your new profile has been uploaded."
            );
          } else {
            this.$root.displayWarn(
              "Update Profile Failed",
              response.data.Message
            );
          }
        })
        .catch((e) => this.$root.displayError("Network Error", e));
    },
    switchEditable: function (target) {
      let inputText = target.getAttribute("id");
      if (this.currentEdit == inputText) {
        this.currentEdit = "";
      } else {
        this.currentEdit = inputText;
      }
    },
    editable: function (target) {
      if (target != null) {
        let text = target.getAttribute("id");
        return text == this.currentEdit;
      } else {
        return false;
      }
    },
    getCurrentUserInfo: function () {
      if (this.$store.getters.userId) {
        let getterInfo = {
          user_id: this.$store.getters.userId,
        };

        axios
          .get(this.$store.getters.URL + "user_data", { params: getterInfo })
          .then((response) => {
            let data = response.data["data"];
            this.avatar = data["avatar"];
            this.firstName = data["fName"];
            this.lastName = data["sName"];
            this.email = data["email"];
            this.phoneNumber = data["phone"];
            this.twitter = data["twitter"];
            this.bio = data["bio"];
            this.intro = data["intro"];
          });
      } else {
        console.warn("not logged in");
      }
    },
    compileMarkdown() {
      let compiled = this.markdown.render(this.bio);
      this.$refs.rendered_md.innerHTML = compiled;
    },
    refreshTwitter(){
      let localURL = `${this.$store.getters.URL}refresh_twitter_score`;
      const form = new FormData();
      form.append("id", this.$store.getters.userId);
      axios
        .post(localURL, form)
        .then((res) => {
          if (res.data.STATUS_CODE == 200) {
            this.getCurrentUserInfo()
            this.$root.displayLog(res.data.Message + this.twitter);
          } else {
            this.error = res.data.Message;
            this.$root.displayLog("That wasn't right, please try again!");
          }
        })
      .catch((err) => {
        console.log(err);
      });   
    },
    submitPIN() {
      let localURL = `${this.$store.getters.URL}social_media_info`;

      const form = new FormData();

      form.append("id", this.$store.getters.userId);
      form.append("OAUTH_TOKEN", this.oauthToken);
      form.append("OAUTH_TOKEN_SECRET", this.oauthTokenSecret);
      form.append("pin", this.twitterPIN);
      axios
        .post(localURL, form)
        .then((res) => {
          if (res.data.STATUS_CODE == 200) {
            this.getCurrentUserInfo()
            this.$root.displayLog(res.data.Message + this.twitter);
          } else {
            this.error = res.data.Message;
            this.$root.displayLog("That wasn't right, please try again!");
          }
        })
        .catch((err) => {
          console.log(err);
        }); 
        this.userAuthoriseTwitter = false;
        this.oauthURL="";     
    },
    removeErrors() {
      this.error = "";
    },
    generateURL() {
      if (this.oauthURL == "") {
        let localURL = `${this.$store.getters.URL}twitter_oauth_url`;
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
          });
      }
      return this.oauthURL;
    },
    openURL() {
      this.userAuthoriseTwitter = true;
      this.generateURL();
      window.open(this.oauthURL, "_blank");
    },
    questionnaireRoute() {
      this.$router.push("/questionnaire");
    },
  },
  mounted() {
    this.markdown = new Markdown({
      html:         true,        // Enable HTML tags in source
      xhtmlOut:     true,        // Use '/' to close single tags (<br />).
                                  // This is only for full CommonMark compatibility.
      breaks:       false,        // Convert '\n' in paragraphs into <br>
      langPrefix:   'language-',  // CSS language prefix for fenced blocks. Can be
                                  // useful for external highlighters.
      linkify:      true,        // Autoconvert URL-like text to links
      // Enable some language-neutral replacement + quotes beautification
      // For the full list of replacements, see https://github.com/markdown-it/markdown-it/blob/master/lib/rules_core/replacements.js
      typographer:  true,
      // Double + single quotes replacement pairs, when typographer enabled,
      // and smartquotes on. Could be either a String or an Array.
      //
      // For example, you can use '«»„“' for Russian, '„“‚‘' for German,
      // and ['«\xA0', '\xA0»', '‹\xA0', '\xA0›'] for French (including nbsp).
      quotes: '“”‘’',
      // Highlighter function. Should return escaped HTML,
      // or '' if the source string is not changed and should be escaped externally.
      // If result starts with <pre... internal wrapper is skipped.
      highlight: function (/*str, lang*/) { return ''; }
    });
    this.markdown.use(emoji);
    this.getCurrentUserInfo();
  },
};
</script>

<style lang="scss" scoped>
$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: #fffaba;

.avatar {
  position: absolute;
  padding: 2rem;
  //margin-top: 30%;
  height: 15rem;
  width: 15rem;
  border-radius: 50%;
}

h2 {
  color: black;
}

.user-name {
  text-align: center;
  margin-top: 4%;
  margin-left: 18%;
}

.top-part {
  display: flex;
  height: 30%;
  flex-flow: row;
  justify-content: left;
  background: $primitive-color;
}

.profile-tab {
  position: absolute;
  margin-top: 6rem;
  left: 2rem;
  width: 85%;
}

.profile-title {
  display: flex;
  flex-flow: row;
  justify-content: left;
  margin-top: 12%;
  width: 100%;
}

.bottom-part {
  display: flex;
  justify-content: center;
  //align-content: center;
  height: 80%;
}

.info-area {
  width: 80%;
  margin-top: 2rem;
}

.names {
  display: flex;
  justify-content: space-between;
}

.contacts {
  display: flex;
  justify-content: space-between;
}

.social-media {
  display: flex;
  justify-content: center;
}

.buttons {
  display: flex;
  justify-content: space-around;
  margin-bottom: 10%;
}
</style>
