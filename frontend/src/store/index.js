import Vue from "vue";
import Vuex from "vuex";
import userModule from "./module/user";

Vue.use(Vuex);

const store = new Vuex.Store({
  strict: process.env.NODE_ENV !== "production",
  state: {},
  actions: {},
  mutations: {},
  modules: {
    userModule
  }
});

export default store;
