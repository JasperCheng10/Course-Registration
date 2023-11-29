<template>
  <div>
    <div v-if="isAuthenticated" class="user-info">
      <p>Name: {{ parsedName }}</p>
      <p>Email: {{ parsedEmail }}</p>
    </div>

    <!-- View Schedule Button -->
    <button v-if="isAuthenticated" @click="viewSchedule" class="view-schedule-btn">View Schedule</button>

    <!-- Schedule Section -->
    <section class="schedule">
      <h3>My Schedule</h3>
      <div class="card-container" v-if="schedule.length > 0">
        <div class="card" v-for="(course, index) in schedule" :key="index">
          <div class="card-content">
            <h4>{{ course.courseName ? course.courseName.S : 'Course Name N/A' }}</h4>
            <button @click="unenroll(course.courseName.S)" class="unenroll-btn">Unenroll</button>
          </div>
        </div>
      </div>
      <p v-else>No classes in your schedule.</p>
    </section>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';
import axios from 'axios';

export default {
  setup() {
    const { user, isAuthenticated } = useAuth0();
    const userJsonString = JSON.stringify(user, null, 2);
    const parsedUser = JSON.parse(userJsonString);
    const parsedName = parsedUser._value.name;
    const parsedEmail = parsedUser._value.email;
    const schedule = ref([]);

    const viewSchedule = () => {
      const url = 'https://xb55sqy2kf.execute-api.us-east-1.amazonaws.com/prod/testing';

      axios.get(url, {
        params: {
          name: parsedName,
        },
      })
      .then(response => {
        schedule.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching schedule:', error);
      });
    };

    const unenroll = (courseName) => {
      const url = 'https://xb55sqy2kf.execute-api.us-east-1.amazonaws.com/prod/delete';

      axios.delete(url, {
        data: {
          name: parsedName,
          courseName: courseName,
        },
      })
      .then(response => {
        // Update the schedule after successful unenrollment
        viewSchedule();
      })
      .catch(error => {
        console.error('Error unenrolling:', error);
      });
    };

    return {
      isAuthenticated,
      parsedName,
      parsedEmail,
      schedule,
      viewSchedule,
      unenroll,
    };
  },
}
</script>

<style>
.user-info {
  margin-bottom: 20px;
}

.view-schedule-btn {
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.schedule {
  margin-top: 20px;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
}

.card {
  background-color: #f4f4f4;
  border: 1px solid #ddd;
  margin: 10px;
  padding: 15px;
  border-radius: 5px;
}

.card-content {
  text-align: center;
}

.unenroll-btn {
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #e53935;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

/* Add more styles as needed */
</style>
