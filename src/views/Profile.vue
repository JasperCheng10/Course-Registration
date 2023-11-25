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
  
      // Save user data as a JSON string
      const userJsonString = JSON.stringify(user, null, 2);
  
      // Parse userJsonString to get name and email
      const parsedUser = JSON.parse(userJsonString);
      const parsedName = parsedUser._value.name; // Access name from _value
      const parsedEmail = parsedUser._value.email; // Access email from _value
  
      // Print name and email to the console
      console.log('Parsed Name:', parsedName);
      console.log('Parsed Email:', parsedEmail);
  
      // Function to send user data via POST request
      const sendUserData = async () => {
        try {
          // Send POST request to the specified endpoint
          const response = await axios.post('https://5ctsolryl1.execute-api.us-east-1.amazonaws.com/prod/create', {
            name: parsedName,
            email: parsedEmail
          });
  
          // Log the response
          console.log('POST Request Response:', response.data);
        } catch (error) {
          // Log any errors
          console.error('Error sending POST request:', error);
        }
      };
  
      return {
        user,
        userJsonString,
        isAuthenticated,
        parsedName,
        parsedEmail,
        sendUserData
      };
    }
  };
  </script>
  