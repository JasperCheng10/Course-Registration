<template>
  <div id="app" style="padding-bottom: 60px;">
    <Header :tabs="tabs" />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
  data() {
    return {
      tabs: [
        { path: '/home', label: 'Home' },
        //{ path: '/fetch', label: 'Create an Account' },
        { path: { name: 'search' }, label: 'Course Search' },
        { path: '/schedule', label: 'Schedule View' },
        { path: '/admin/createcourse', label: 'Create Course' },
        //{ path: '/login', label: 'Login' },
        { path: '/', label: 'Login' },
        { path: '/profile', label: 'Profile' },
      ]
    };
  },
  components: {
    Header,
    Footer
  }
};
</script>