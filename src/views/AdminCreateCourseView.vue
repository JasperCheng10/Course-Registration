<template>
  <main class="admincreatecourse">
    <h2>Create Course</h2>
    <p>
      Admin - Create Course Page
    </p>

    <form class="create-course">
      <label for="todo">New Course</label>
      <label for="department">Department</label>
      <input type="text" id="department" name="Department" v-model="department" pattern="[A-Z]{4}" required />
      <p> Required: Should consist of 4 letters A-Z </p>
      <label for="coursenumber">Course Number</label>
      <input type="text" id="coursenumber" name="CourseNumber" v-model="coursenumber" pattern="\d{4}" required />
      <p> Required: Should consist of 4 numbers 0-9 </p>
      <label for="coursename">Name</label>
      <input type="text" id="coursename" name="Name" v-model="coursename" maxlength="250" required />
      <p> Required: Should not be longer than 250 characters in length </p>
      <label for="professor">Professor(s)</label>
      <input type="text" id="professor" name="Professor" v-model="professor" required />
      <p> Required </p>
      <label for="starttime">Meeting Start Time</label>
      <input type="time" id="starttime" name="Meeting Start Time" v-model="starttime" required/>
      <p> Required </p>
      <label for="endtime">Meeting End Time</label>
      <input type="time" id="endtime" name="Meeting End Time" v-model="endtime" required />
      <p> Required </p>
      <label for="location">Meeting Location</label>
      <input type="text" id="location" name="Meeting Location" v-model="location" required />
      <p> Required </p>
      <label for="credits">Credits</label>
      <input type="number" id="credits" name="Credits" v-model="credits" min="1.00" max="15.00" step="1.00" required/>
      <p> Required: Can be any whole credit amount from 1.00 - 15.00 </p>
      <label for="capacity">Capacity</label>
      <input type="text" id="capacity" name="Capacity" v-model="capacity" required/>
      <p> Required </p>
      <div class="waitlist">
        <label for="waitlist">Waitlist Open</label>
        <input type="checkbox" id="waitlist" name="WaitlistOpen" v-model="waitlist" required/>
        <p> Required </p>
      </div>
      <label for="coursetype">Course Type</label>
      <select id="coursetype" name="Course Type" v-model="coursetype" required>
        <option value="lecture">Lecture</option>
        <option value="discussion">Discussion</option>
        <option value="lab">Lab</option>
        <option value="seminar">Seminar</option>
      </select>
      <p> Required </p>
      <label for="prereqs">Pre-requirements</label>
      <input type="text" id="prereqs" name="Pre-requirements" v-model="prereqs" />
      <p> Optional </p>
      <label for="description">Description</label>
      <textarea id="description" name="description" v-model="description" ></textarea>
      <p> Optional </p>
      <button type="reset">Clear</button>
      <button type="submit">Save</button>
    </form>
  </main>  
</template>

<style>
.create-course {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.create-course select {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  background-color: white;
  color: #333;
}

.create-course textarea {
  width: 100%;
  height: 150px; /* Adjust the height as needed */
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.create-course label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.create-course p {
  margin-bottom: 10px;
}

.create-course input.invalid {
  border: 5px solid red;
}

.create-course input {
  width: 100%;
  padding: 10px;
  margin-bottom: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.create-course button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-right: 10px;
}

.create-course button[type="reset"] {
  background-color: #ccc;
}

.create-course button[type="submit"] {
  background-color: #28a745;
}

</style>
