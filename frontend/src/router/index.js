import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store";
import Home from "../views/Home.vue";
import userRoutes from "./module/user.js";

Vue.use(VueRouter);

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err);
};

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/current",
    name: "Current",
    component: () => import("@/views/Current.vue")
  },
  ...userRoutes
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if (to.meta.auth) {
    if (store.state.userModule.token) {
      next();
    } else {
      router.push({ name: "login" });
    }
  } else next();
});

export default router;
