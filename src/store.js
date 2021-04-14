import { createStore } from "vuex";
import createPresistedState from 'vuex-persistedstate'

export default createStore({
  plugins: [createPresistedState({
    storage: window.sessionStorage,
  })],
  state: {
    isLoggedIn: false,
    userId: null,
    userFName: null,
    userAvatar: null,
    remoteURL: "https://secret-crag-87848.herokuapp.com/",
    localURL: "http://localhost:5000/",
    isUsingRemote: true,
    matchesRetrieved: false,
  },
  mutations: {
    logIn(state, userInfo) {
      state.isLoggedIn = true;
      state.userId = userInfo.id;
      state.userFName = userInfo.fName;
      state.userAvatar = userInfo.avatar;
    },
    logOut(state) {
      state.isLoggedIn = false;
      state.userId = null;
    },
    updateUserInfo(state, userInfo){
      state.userFName = userInfo.fName;
      state.userAvatar = userInfo.avatar;
    },
    matchesRetrieved(state) {
      state.matchesRetrieved = true;
    },
  },
  actions: {
    logIn(context, id) {
      context.commit("logIn", id);
    },
    logOut(context) {
      context.commit("logOut");
    },
    updateUserInfo(context, dat){
      context.commit("updateUserInfo", dat);
    },
    matchesRetrieved(context) {
      context.commit("matchesRetrieved");
    },
  },
  getters: {
    isLoggedIn: (state) => {
      return state.isLoggedIn;
    },
    userId: (state) => {
      return state.userId;
    },
    URL: (state) => {
      return state.isUsingRemote ? state.remoteURL : state.localURL;
    },
    matchesRetrieved: (state) => {
      return state.matchesRetrieved;
    },
    fName: (state) => {
      return state.userFName;
    },
    avatar: (state) => {
      return state.userAvatar;
    }
  },
});
