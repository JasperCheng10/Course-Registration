<template>
  <div class="course-container">
    <h1>My Courses</h1>
    <input type="text" v-model="search" placeholder="Search for a course" />
    <table class="course-table">
      <thead>
        <tr>
          <th>Courses</th>
          <th>Credits</th>
          <th>Professor</th>
          <th>Time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="course in filteredCourses" :key="course.id" @click="selectCourse(course)">
          <td>{{ course.name }}</td>
          <td>{{ course.credits }}</td>
          <td>{{ course.professor }}</td>
          <td>{{ course.time }}</td>
        </tr>
      </tbody>
    </table>
    <div v-if="selectedCourse" class="course-details">
      <h2>Selected Course Details</h2>
      <p><strong>Course:</strong> {{ selectedCourse.name }}</p>
      <p><strong>Credits:</strong> {{ selectedCourse.credits }}</p>
      <p><strong>Professor:</strong> {{ selectedCourse.professor }}</p>
      <p><strong>Time:</strong> {{ selectedCourse.time }}</p>
    </div>
    <div v-if="!isLoggedIn">
      <p><router-link to="/login">Log in</router-link></p>
      <p>
        <router-link to="/fetch">Create an Account</router-link>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentMyCourses",
  data() {
    return {
      search: "",
      selectedCourse: null,
    };
  },
  props: {
    courses: {
      type: Array,
      required: true,
      default: () => [],
      validator: (courses) => {
        return courses.every(
          (course) =>
            course.hasOwnProperty("id") &&
            course.hasOwnProperty("name") &&
            course.hasOwnProperty("credits") &&
            course.hasOwnProperty("professor") &&
            course.hasOwnProperty("time")
        );
      },
    },
    isLoggedIn: {
      type: Boolean,
      required: true,
      default: false,
    },
  },
  computed: {
    filteredCourses() {
      if (this.search) {
        return this.courses.filter((course) =>
          course.name.toLowerCase().includes(this.search.toLowerCase())
        );
      } else {
        return this.courses;
      }
    },
  },
  mounted() {
    this.animateTable();
  },
  methods: {
    animateTable() {
      const rows = document.querySelectorAll(".course-table tr");
      rows.forEach((row, index) => {
        setTimeout(() => {
          row.classList.add("visible");
        }, index * 200);
      });
    },
    selectCourse(course) {
      this.selectedCourse = course;
    },
  },
};
</script>

<style scoped>
.course-container {
  font-family: "Arial", sans-serif;
  width: 80%;
  margin: 0 auto;
  padding: 2rem;
  background: url("background.jpg") no-repeat center center fixed;
  background-size: cover;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1,
h2 {
  text-align: center;
  font-size: 2rem;
  color: #333;
  margin-bottom: 1rem;
}

input {
  display: block;
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.course-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
  cursor: pointer;
}

.course-table thead {
  background-color: #0077cc;
  color: #fff;
}

.course-table th,
.course-table td {
  padding: 1rem;
  text-align: left;
  border: 1px solid #ddd;
}

.course-table tr {
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}

.course-table tr.visible {
  opacity: 1;
}

.course-table tr:hover {
  background-color: #f5f5f5;
}

.course-details {
  margin-top: 2rem;
  padding: 1rem;
  background-color: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

p {
  text-align: center;
  margin: 1rem 0;
}

p a {
  color: #0077cc;
  text-decoration: none;
}

p a:hover {
  text-decoration: underline;
}
</style>
