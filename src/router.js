import { createRouter, createWebHistory } from "vue-router";
import PrivacyPolicy from "./pages/PrivacyPolicy.vue";
import ContactUs from "./pages/ContactUs.vue";
import TermsAndConditions from "./pages/TermsAndConditions.vue";
import HomePage from "./pages/HomePage.vue";
import Login from "./pages/Login.vue";
import ForgotPassword from "./pages/ForgotPassword.vue";
import Register from "./pages/Register.vue";
import Questionnaire from "./pages/Questionnaire.vue";
import SocialMediaInfo from "./pages/SocialMediaInfo.vue";
import About from "./pages/About.vue";
import Report from "./pages/Report.vue";
import Profile from "./pages/Profile.vue";
import Matches from "./pages/Matches.vue";
import Bumps from "./pages/Bumps.vue";
import AccessDenied from "./pages/AccessDenied";
import HomePageAfter from "./pages/HomePageAfter.vue"

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      name: "index",
      path: "/",
      components: {
        default: HomePage,
      },
    },
    {
      name: "bumps",
      path: "/bumps",
      component: Bumps
    },
    {
      name: "forgot",
      path: "/forgot_password",
      component: ForgotPassword,
    },
    {
      name: "register",
      path: "/register",
      component: Register,
    },
    {
      name: "login",
      path: "/login",
      component: Login,
    },
    {
      name: "questionnaire",
      path: "/questionnaire",
      component: Questionnaire,
    },
    {
      name: "socialmediainfo",
      path: "/socialmediainfo",
      component: SocialMediaInfo,
    },
    {
      name: "about",
      path: "/about",
      component: About,
    },
    {
      name: "matches",
      path: "/matches",
      component: Matches,
    },
    {
      name: "report",
      path: "/report",
      component: Report,
    },
    {
      name: "privacy",
      path: "/privacy",
      component: PrivacyPolicy,
    },
    {
      name: "contact",
      path: "/contact",
      component: ContactUs,
    },
    {
      name: "terms",
      path: "/terms",
      component: TermsAndConditions,
    },
    {
      name: "profile",
      path: "/profile",
      component: Profile,
    },
    {
      name: "access_denied",
      path: "/access-denied",
      component: AccessDenied
    },
    {
      name: "HPA",
      path: "/hpa",
      component: HomePageAfter
    }
  ],
  linkActiveClass: "active",
  scrollBehavior(_, __, savedPosition) {
    if (savedPosition) return savedPosition;
    return { left: 0, top: 0 };
  },
});
