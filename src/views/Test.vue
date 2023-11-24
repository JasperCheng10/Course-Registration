<template>
    <header>This is a test page</header>
    <div>
      <button @click="handleLogin">Log in</button>
    </div>
  </template>

 <!--From Lab  -->
<script setup>
import { useAuth0 } from "@auth0/auth0-vue";

const { loginWithRedirect } = useAuth0();

const handleLogin = () => {
  loginWithRedirect({
    appState: {
      target: "/profile",
    },
  });
};
</script>

<!-- From Auth0 Quickstart Tutorial -->
  <!-- <script>
    import { useAuth0 } from '@auth0/auth0-vue';
  
    export default {
      setup() {
        const { loginWithRedirect } = useAuth0();
  
        return {
          login: () => {
            loginWithRedirect();
          }
        };
      }
    };
  </script> -->