import { createStore } from "vuex";

export default createStore({
  state: {
    isLoggedIn: false,
    userId: null,
    remoteURL: "http://ec2-54-198-73-79.compute-1.amazonaws.com/",
    localURL: "http://localhost:5000/",
    matchesRetrieved: false,
  },
  mutations: {
    logIn(state, id) {
      state.isLoggedIn = true;
      state.userId = id;
    },
    logOut(state) {
      state.isLoggedIn = false;
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
    remoteURL: (state) => {
      return state.remoteURL;
    },
    localURL: (state) => {
      return state.localURL;
    },
    matchesRetrieved: (state) => {
      return state.matchesRetrieved;
    },
  },
});
