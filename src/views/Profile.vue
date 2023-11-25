<template>
  <div>
    <h2>User Profile</h2>
    <div v-if="isAuthenticated">
      <p>Name: {{ parsedName }}</p>
      <p>Email: {{ parsedEmail }}</p>
      <button @click="sendUserData">Send User Data</button>
    </div>
  </div>
</template>

<script>
import { useAuth0 } from '@auth0/auth0-vue';
import axios from 'axios';

export default {
  setup() {
    const { user, isAuthenticated } = useAuth0();
    console.log(user);
    const userJsonString = JSON.stringify(user, null, 2);
    console.log(userJsonString);
    const parsedUser = JSON.parse(userJsonString);
    const parsedName = parsedUser._value.name;
    const parsedEmail = parsedUser._value.email;

    const sendUserData = async () => {
      try {
        const response = await axios.post('https://5ctsolryl1.execute-api.us-east-1.amazonaws.com/prod/create', {
          name: parsedName,
          email: parsedEmail
        });

        console.log('POST Request Response:', response.data);
      } catch (error) {
        console.error('Error sending POST request:', error);
      }
    };

    return {
      isAuthenticated,
      parsedName,
      parsedEmail,
      sendUserData
    };
  }
};
</script>
