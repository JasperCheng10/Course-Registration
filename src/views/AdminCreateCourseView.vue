<template>
  <main class="admincreatecourse">
    <h2>Create Course</h2>
    <p>Admin - Create Course Page</p>

    <form class="create-course" @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Course Name (e.g., Math 101)</label>
        <input type="text" id="name" name="Name" v-model="name" required />
        <p class="requirement-note">Required</p>
      </div>

      <div class="form-group">
        <label for="days">Days (e.g., Mon, Wed, Fri)</label>
        <input type="text" id="days" name="Days" v-model="days" required />
        <p class="requirement-note">Required</p>
      </div>

      <div class="form-group">
        <label for="location">Location (e.g., Room 101)</label>
        <input type="text" id="location" name="Location" v-model="location" required />
        <p class="requirement-note">Required</p>
      </div>

      <div class="form-group">
        <label for="major">Major (e.g., Computer Science)</label>
        <input type="text" id="major" name="Major" v-model="major" required />
        <p class="requirement-note">Required</p>
      </div>

      <div class="form-group">
        <label for="professor">Professor(s) (e.g., Dr. Smith)</label>
        <input type="text" id="professor" name="Professor" v-model="professor" required />
        <p class="requirement-note">Required</p>
      </div>

      <div class="form-group">
        <label for="seats">Seats (e.g., 30)</label>
        <input type="number" id="seats" name="Seats" v-model="seats" required />
        <p class="requirement-note">Required</p>
      </div>

      <div class="form-group">
        <label for="time">Time (e.g., 10:00 AM - 11:30 AM)</label>
        <input type="text" id="time" name ="Time" v-model="time" required />
        <p class="requirement-note">Required</p>
      </div>

      <div class="form-group">
        <label for="type">Course Type</label>
        <select id="type" name="Type" v-model="type" required>
          <option value="lecture">Lecture</option>
          <option value="discussion">Discussion</option>
          <option value="lab">Lab</option>
          <option value="seminar">Seminar</option>
        </select>
        <p class="requirement-note">Required</p>
      </div>

      <!-- Your other form inputs as needed -->

      <div class="form-group">
        <button type="reset" class="btn-clear">Clear</button>
        <button type="submit" class="btn-save">Save</button>
      </div>
    </form>
    <div class="form-group">
      <a href="http://jack-s-bucket.s3-website-us-east-1.amazonaws.com" target="_blank" class="btn-help">Help</a>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      days: '',
      location: '',
      major: '',
      professor: '',
      seats: '',
      time: '',
      type: 'lecture',
      // Other data properties as needed
    };
  },
  methods: {
    submitForm() {
      const courseData = {
        name: this.name,
        days: this.days,
        location: this.location,
        major: this.major,
        professor: this.professor,
        seats: this.seats,
        time: this.time,
        type: this.type,
        // Other data properties as needed
      };

      axios.post('https://8dbuywnj95.execute-api.us-east-1.amazonaws.com/Final_stage_course/course', courseData)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
.create-course {
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
select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

input[type="number"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.btn-clear {
  background-color: #ccc;
  color: #333;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  margin-right: 10px; /* Add margin between buttons */
}

.btn-save {
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
}

.requirement-note {
  font-size: 12px;
  color: #999;
}
</style>