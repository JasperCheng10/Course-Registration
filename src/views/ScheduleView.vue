<!-- ScheduleView.vue -->
<template>
    <div>
      <h1>Weekly Class Schedule</h1>
      <div class="week-calendar">
        <div class="header">
          <div v-for="day in weekDays" :key="day" class="day-header">{{ day }}</div>
        </div>
        <div class="calendar">
          <div v-for="day in weekDays" :key="day" class="day-column">
            <div v-for="classItem in getClassesByDay(getDayIndex(day))" :key="classItem.id" class="class-item">
              <h4>{{ classItem.title }}</h4>
              <p>Professor: {{ classItem.professor }}</p>
              <p>Time: {{ classItem.time }}</p>
              <p>Location: {{ classItem.location }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        courses: [
          // Example courses for each day of the week
          { id: 1, title: 'Mathematics', professor: 'Dr. Smith', time: '8:00 AM - 9:30 AM', location: 'Room 101', day: 'Monday' },
          { id: 2, title: 'Physics', professor: 'Prof. Johnson', time: '10:00 AM - 11:30 AM', location: 'Room 205', day: 'Tuesday' },
          { id: 3, title: 'Literature', professor: 'Dr. Brown', time: '12:00 PM - 1:30 PM', location: 'Room 303', day: 'Wednesday' },
          { id: 4, title: 'Computer Science', professor: 'Prof. Davis', time: '2:00 PM - 3:30 PM', location: 'Room 402', day: 'Thursday' },
          { id: 5, title: 'History', professor: 'Dr. Lee', time: '4:00 PM - 5:30 PM', location: 'Room 505', day: 'Friday' }
          // Add more courses as necessary
        ],
        weekDays: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
      };
    },
    methods: {
      getDayIndex(day) {
        return this.weekDays.indexOf(day);
      },
      getClassesByDay(dayIndex) {
        return this.courses.filter(course => course.day === this.weekDays[dayIndex]);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  .week-calendar {
    display: flex;
    flex-direction: column;
    margin-top: 20px;
    font-family: 'Arial', sans-serif;
  }
  
  .header {
    display: flex;
    background-color: #f0f0f0;
    border-bottom: 1px solid #ccc;
  }
  
  .day-header {
    flex: 1;
    border-right: 1px solid #ccc;
    padding: 15px;
    text-align: center;
    font-weight: bold;
  }
  
  .calendar {
    display: flex;
  }
  
  .day-column {
    flex: 1;
    border: 1px solid #ccc;
    padding: 10px;
    margin-right: 10px;
  }
  
  .class-item {
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .class-item h4 {
    margin-bottom: 10px;
    color: #333;
  }
  
  .class-item p {
    margin-bottom: 5px;
    color: #666;
  }
  </style>
  