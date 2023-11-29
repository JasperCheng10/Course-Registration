<template>
  <div>
    <div class="center-button">
      <button @click="viewSchedule" v-if="isAuthenticated">View Schedule</button>
    </div>

    <!-- Schedule Section -->
    <section class="schedule">
      <h3>Schedule</h3>
      <div class="card-container" v-if="scheduleItems.length > 0">
        <div class="card" v-for="(item, index) in scheduleItems" :key="index">
          <div class="card-content">
            <h4>{{ item.name }}</h4>
            <div class="card-details">
              <strong>Course Name:</strong> {{ item.courseName }}
            </div>
          </div>
        </div>
      </div>
      <p v-else>No schedule available.</p>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  data() {
    return {
      isAuthenticated: true, // Change this to your authentication logic
      scheduleItems: [],
    };
  },
  methods: {
    viewSchedule() {
      const requestData = {
        name: 'Jack Psaras',
      };

      let url = 'https://xb55sqy2kf.execute-api.us-east-1.amazonaws.com/prod/enroll';

      // Constructing the URL with query parameters
      url += `?name=${requestData.name}`;

      axios.get(url)
        .then(response => {
          if (response.data.statusCode === 200) {
            this.scheduleItems = response.data.body.items;
          } else {
            console.error('Error fetching schedule:', response.data.body.message);
          }
        })
        .catch(error => {
          console.error('Error fetching schedule:', error.message);
        });
    },
  },
};
</script>

<style>
.center-button {
  text-align: center;
  margin-top: 50vh; /* Adjust this value to center the button vertically */
}

.center-button button {
  padding: 10px 20px;
  border: 1px solid #003366;
  border-radius: 5px;
  background-color: #003366;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}

.schedule {
  text-align: center;
  margin-top: 20px;
}

.schedule h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #003366;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.card {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  width: 500px;
  background-color: #f9f9f9;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  margin: 20px auto;
  display: flex;
}

.card-content {
  flex: 1;
}

.card h4 {
  font-size: 1.3rem;
  margin: 0 0 20px;
  color: #003366;
}

.card-details {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.card-details strong {
  font-weight: bold;
  margin-right: 5px;
}
</style>
