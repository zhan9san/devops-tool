import storageService from "@/service/storageService";
import userService from "@/service/userService.js";

const userModule = {
  namespaced: true,
  state: {
    token: storageService.get(storageService.USER_TOKEN),
    name: storageService.get(storageService.USER_NAME)
  },
  mutations: {
    SET_USER_TOKEN(state, token) {
      storageService.set(storageService.USER_TOKEN, token);
      state.token = token;
    },
    SET_USER_NAME(state, name) {
      storageService.set(storageService.USER_NAME, name);
      state.name = name;
    }
  },
  actions: {
    login(context, { username, password }) {
      return new Promise((resolve, reject) => {
        userService
          .login({ username, password })
          .then(res => {
            context.commit("SET_USER_TOKEN", res.data.access);
            return userService.user();
          })
          .then(res => {
            context.commit("SET_USER_NAME", res.data.username);
            resolve(res);
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    logout({ commit }) {
      commit("SET_USER_TOKEN", "");
      storageService.set(storageService.USER_TOKEN, "");
      commit("SET_USER_NAME", "");
      storageService.set(storageService.USER_NAME, "");

      window.location.reload();
    }
  }
};

export default userModule;
