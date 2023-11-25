<template>
  <div>
    <header>Login Page</header>
    <div>
      <button v-if="!isAuthenticated" @click="handleLogin">Log in</button>
      <button v-if="isAuthenticated" @click="handleLogout">Log out</button>
    </div>
  </div>
</template>

<script setup>
import { useAuth0 } from "@auth0/auth0-vue";

const { isAuthenticated, loginWithRedirect, logout } = useAuth0();

const handleLogin = () => {
  loginWithRedirect({
    appState: {
      target: "/profile",
    },
  });
};

const handleLogout = () => {
  logout({
    returnTo: window.location.origin,
  });
};
</script>
