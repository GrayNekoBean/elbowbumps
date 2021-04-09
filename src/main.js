import { createApp } from "vue";
import App from "./App.vue";
import router from "./router.js";
import store from "./store.js";
import primevue from "primevue/config";
import ToastService from 'primevue/toastservice';

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
import FileUpload from "primevue/fileupload";
import Toast from 'primevue/toast';
import Menubar from 'primevue/menubar';
import Menu from 'primevue/menu';
import Avatar from 'primevue/avatar';
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
import ScrollPanel from 'primevue/scrollpanel';
import Tag from 'primevue/tag';
import Sidebar from 'primevue/sidebar';
import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';
import TextArea from 'primevue/textarea';
import Dialog from 'primevue/dialog'

import "primevue/resources/themes/saga-blue/theme.css"; // theme
import "primevue/resources/primevue.min.css"; // core css
import "primeicons/primeicons.css"; // icons

import "./scss/colour-theme.scss";

const app = createApp(App);
app.use(router);
app.use(primevue);
app.use(store);
app.use(ToastService);

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
app.component("FileUpload", FileUpload);
app.component("Toast", Toast);
app.component("Menubar", Menubar);
app.component("Menu", Menu);
app.component("Avatar", Avatar);
app.component("Accordion", Accordion);
app.component("AccordionTab", AccordionTab);
app.component("ScrollPanel", ScrollPanel);
app.component("Tag", Tag);
app.component("Sidebar", Sidebar);
app.component("Splitter", Splitter);
app.component("SplitterPanel", SplitterPanel);
app.component("TextArea", TextArea);
app.component("Dialog", Dialog);

app.mount("#app");
