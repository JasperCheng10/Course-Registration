// this file creates the router instance that is used by our application

// we start by importing the createRouter and createWebHistory functions, as well as the components describing each of our views
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ClassSearch from "../views/ClassSearch.vue";
import AdminCreateCourseView from "../views/AdminCreateCourseView.vue";
import LoginPage from "../views/LoginPage.vue";
import SignUp from "../views/SignUp.vue";
import ScheduleView from "../views/ScheduleView.vue";
import StudentCourseView from "../views/StudentCourseView.vue";
import Test from "../views/Test.vue";
import Profile from "../views/Profile.vue";

const router = createRouter({
  // the history mode determines how vue router interacts with the url.
  // createWebHistory() simulates the default browser behavior of changing
  // the path of the url based on the current document.
  // import.meta.env.BASE_URL is a vite feature that you don't need to worry about
  // and can safely use. it refers to the current path to the directory being
  // served by vite, which in this project is always the same directory
  // (and therefore import.meta.env.BASE_URL is '/')
  history: createWebHistory(import.meta.env.BASE_URL),

  // each entry to this routes array has a path (what goes in the URL to access
  // this page), a name (check out components/AppHeader.vue for how this is used)
  // and, most importantly, the component that should be rendered for the view
  routes: [
    {
      path: "/home",
      name: "home",
      component: HomeView,
    },
    {
      path: "/search",
      name: "search",
      component: ClassSearch,
    },
    {
      path: "/fetch",
      name: "fetch",
      component: SignUp,
    },
    {
      path: "/admin/createcourse",
      name: "admincreatecourse",
      component: AdminCreateCourseView,
    },
    {
      path: "/login",
      name: "Login",
      component: LoginPage,
    },
    {
      path: "/schedule",
      name: "schedule",
      component: ScheduleView,
    },
    {
      path: "/mycourses",
      name: "mycourses",
      component: StudentCourseView,
    },
    {
      path: "/",
      name: "Test",
      component: Test,
    },
    {
      path: "/profile",
      name: "Profile",
      component: Profile,

    },
  ],
});

export default router;
