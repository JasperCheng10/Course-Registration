<template>
  <div>
    <div v-if="isAuthenticated">
      <p>Name: {{ parsedName }}</p>
      <p>Email: {{ parsedEmail }}</p>
    </div>

    <!-- Search Form -->
    <section class="search-form">
      <h3>Class Search</h3>
      <form @submit.prevent="searchClasses">
        <label for="courseName">Course Name:</label>
        <input type="text" id="courseName" v-model="courseName" /><br /><br />

        <label for="professor">Professor (Optional):</label>
        <input type="text" id="professor" v-model="professor" /><br /><br />

        <label for="courseID">Course ID (Optional):</label>
        <input type="text" id="courseID" v-model="courseID" /><br /><br />

        <button type="submit">Search</button>
      </form>
    </section>

    <!-- Search Results Section -->
    <section class="search-results">
      <h3>Search Results</h3>
      <div class="card-container" v-if="results">
        <div class="card">
          <div class="card-content">
            <h4>{{ results.name ? results.name.S : 'Course Name N/A' }}</h4>
            <div class="card-details">
              <div v-for="(value, name) in results" :key="name" v-if="name !== 'name'">
                <strong>{{ name }}:</strong>
                {{ formatValue(value) }}
              </div>
            </div>
          </div>

          <!-- Enroll button -->
          <div class="enroll-button">
            <button @click="enrollClass">Enroll</button>
          </div>
        </div>
      </div>
      <p v-else>No results found.</p>
    </section>
  </div>
</template>

<script>
import { useAuth0 } from '@auth0/auth0-vue';
import axios from 'axios';

export default {
  setup() {
    const { user, isAuthenticated } = useAuth0();
    const userJsonString = JSON.stringify(user, null, 2);
    const parsedUser = JSON.parse(userJsonString);
    const parsedName = parsedUser._value.name;
    const parsedEmail = parsedUser._value.email;

    return {
      isAuthenticated,
      parsedName,
      parsedEmail,
    };
  },

  data() {
    return {
      courseName: '',
      professor: '',
      courseID: '',
      results: null,
    };
  },
  methods: {
    searchClasses() {
      let url = `https://8dbuywnj95.execute-api.us-east-1.amazonaws.com/Final_stage_course/search?name=${this.courseName}`;

      if (this.professor) {
        url += `&professor=${this.professor}`;
      }

      if (this.courseID) {
        url += `&id=${this.courseID}`;
      }

      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          this.results = data;
          console.log(this.results.name.S);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    formatValue(value) {
      if (value && value.S) return value.S;
      if (value && value.N) return value.N;
      return value || 'N/A';
    },
    enrollClass() {
      const courseData = {
        name: this.parsedName,
        courseName: this.results.name.S,
      };

      axios.post('https://xb55sqy2kf.execute-api.us-east-1.amazonaws.com/prod/enroll', courseData)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
      },
  }
}
</script>

<style>
.search-form {
  text-align: center;
  margin-bottom: 20px;
}

.search-form h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #003366;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #333; /* Darkened label text color for better contrast */
}

input {
  padding: 10px;
  width: 400px;
  border: 1px solid #777; /* Darker border color for better contrast */
  border-radius: 5px;
  margin-bottom: 10px;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  border: 1px solid #003366; /* Darker border color for contrast */
  border-radius: 5px;
  background-color: #003366;
  color: #fff; /* Text color */
  font-size: 16px;
  cursor: pointer;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.card {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px; /* Added padding */
  width: 500px; /* Set width to make it more horizontal */
  background-color: #f9f9f9;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  margin: 20px auto; /* Center the card horizontally */
  display: flex; /* Set display to flex */
}

.card-content {
  flex: 1; /* Fill the space evenly for horizontal alignment */
}

.card h4 {
  font-size: 1.3rem;
  margin: 0 0 20px; /* Add margin for spacing */
  color: #003366;
}

.card-details {
  display: flex;
  flex-direction: column;
  gap: 10px; /* Added gap for spacing between details */
}

.card-details div {
  margin-bottom: 5px;
}

.card-details strong {
  font-weight: bold;
  margin-right: 5px;
}

/* Styles for the enroll button */
.enroll-button {
  display: flex;
  align-items: center;
}

.enroll-button button {
  padding: 10px 20px;
  margin-left: auto; /* Push the button to the right */
  border: 1px solid #003366;
  border-radius: 5px;
  background-color: #003366;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}
</style>
