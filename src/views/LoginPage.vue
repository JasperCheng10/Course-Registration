<template>
    <div class="login">
      <h2>Login</h2>
      <div class="image">
        <img src="https://cdn-icons-png.flaticon.com/512/2815/2815428.png">
      </div>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
          <p>
          <router-link to="/forgot-password">Forgot Password</router-link>
        </p>
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        password: '',
      };
    },
    methods: {
      login() {
        // You can add your login logic here
        // For example, send a POST request to a server with email and password
        // If login is successful, you can navigate to another page
        // If login fails, you can display an error message
      },
    },
  };
  </script>
  
  <style scoped>

h2{
  font-size: xx-large;
  text-align: center;
}
  .image{
    height: 200px;
    display: flex;
    justify-content: center;
  }

  .login {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    font-weight: bold;
  }
  
  input[type="text"],
  input[type="password"],
  input[type="email"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
  }
  
  button {
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    cursor: pointer;
    display: block;
    margin: 0 auto;
  }
  </style>
  