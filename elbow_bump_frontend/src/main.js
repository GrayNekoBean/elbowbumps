import { createApp } from "vue";
import App from "./App.vue";
import router from "./router.js";
import store from "./store.js";
import primevue from "primevue/config";

import Button from "primevue/button";
import Checkbox from "primevue/checkbox";
import Card from "primevue/card";
import Panel from "primevue/panel";
import Password from "primevue/password";
import InputText from "primevue/inputtext";
import TabMenu from "primevue/tabmenu";
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";
import RadioButton from "primevue/radiobutton";

import "primevue/resources/themes/saga-blue/theme.css"; // theme
import "primevue/resources/primevue.min.css"; // core css
import "primeicons/primeicons.css"; // icons

import "./scss/colour-theme.scss";

const app = createApp(App);
app.use(router);
app.use(primevue);
app.use(store);

app.component("Button", Button);
app.component("Checkbox", Checkbox);
app.component("Card", Card);
app.component("Panel", Panel);
app.component("Password", Password);
app.component("InputText", InputText);
app.component("TabView", TabView);
app.component("TabPanel", TabPanel);
app.component("TabMenu", TabMenu);
app.component("RadioButton", RadioButton);

app.mount("#app");
