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
            <!-- Display additional course information -->
            <div v-if="courseDetails[index]">
              <p><strong>Location:</strong> {{ courseDetails[index].location.S }}</p>
              <p><strong>Days:</strong> {{ courseDetails[index].days.S }}</p>
              <p><strong>Seats:</strong> {{ courseDetails[index].seats.N }}</p>
              <p><strong>Professor:</strong> {{ courseDetails[index].professor.S }}</p>
              <p><strong>Major:</strong> {{ courseDetails[index].major.S }}</p>
              <p><strong>Time:</strong> {{ courseDetails[index].time.S }}</p>
              <p><strong>Type:</strong> {{ courseDetails[index].type.S }}</p>
            </div>
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
    const courseDetails = ref([]);

    const viewSchedule = async () => {
      const url = 'https://xb55sqy2kf.execute-api.us-east-1.amazonaws.com/prod/testing';

      try {
        const response = await axios.get(url, {
          params: {
            name: parsedName,
          },
        });

        schedule.value = response.data;

        // Fetch additional course details for each course
        const promises = schedule.value.map(course => {
          const courseDetailsUrl = 'https://8dbuywnj95.execute-api.us-east-1.amazonaws.com/Final_stage_course/search';
          return axios.get(courseDetailsUrl, {
            params: {
              name: course.courseName.S,
            },
          });
        });

        const detailsResponses = await Promise.all(promises);
        courseDetails.value = detailsResponses.map(response => response.data);
      } catch (error) {
        console.error('Error fetching schedule:', error);
      }
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
      courseDetails,
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
