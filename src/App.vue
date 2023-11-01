<template>
  <div id="app">
    <Header :tabs="tabs" />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
export default {
  data() {
    return {
      tabs: [
        { path: "/", label: "Home" },
        { path: "/fetch", label: "Create an Account" },
        { path: { name: "form" }, label: "Form Example" },
        { path: "/schedule", label: "Schedule View" },
        { path: "/mycourses", label: "Course View" },
        { path: "/admin/createcourse", label: "Create Course" },
        { path: "/login", label: "Login" },
      ],
    };
  },
  components: {
    Header,
    Footer,
  },
};
</script>
