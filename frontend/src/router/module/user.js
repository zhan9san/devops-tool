const userRoutes = [
  {
    path: "/login",
    name: "login",
    component: () => import("@/components/Login.vue")
  },
  {
    path: "/profile",
    name: "profile",
    meta: {
      auth: true
    },
    component: () => import("@/views/Profile.vue")
  }
];

export default userRoutes;
