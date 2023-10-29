<template>
  <div class="signup">
    <h2>Create an Account</h2>
    <form @submit.prevent="registerUser">
      <div class="form-group">
        <label for="username">Username <span class="required">*</span></label>
        <input type="text" id="username" v-model="username" required />
      </div>

      <div class="form-group">
        <label for="email">Email<span class="required">*</span></label>
        <input type="email" id="email" v-model="email" required />
      </div>

      <div class="form-group">
        <label for="password">Password<span class="required">*</span></label>
        <input type="password" id="password" v-model="password" required />
      </div>

      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    registerUser() {
      const userData = {
        username: this.username,
        email: this.email,
        password: this.password,
      };

      axios
        .post('https://uu9xl4bi58.execute-api.us-east-1.amazonaws.com/signupstage/login', userData) // Replace with your actual API endpoint
        .then(response => {
          console.log(response.data);
          // Optionally, you can redirect the user to a login page or display a success message.
        })
        .catch(error => {
          console.error(error);
          // Handle any error, e.g., display an error message to the user.
        });
    },
  },
};
</script>

<style scoped>
.signup {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc; /* Add a border around the form */
  border-radius: 5px; /* Rounded corners */
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px; /* Increase spacing between inputs */
}

button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 10px; /* Increase spacing between inputs and the button */
}
</style>
