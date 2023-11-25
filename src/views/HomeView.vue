<template>
  <main class="home">
    <!-- Existing Welcome Section -->
    <section class="welcome">
      <div class="welcome-content">
        <h2>Welcome to Section 2 Group 3 University</h2>
        <p>Explore our vibrant academic community dedicated to excellence.</p>
        
      </div>
    </section>

    <!-- Existing Programs Section -->
    <section class="grid-section">
      <h3>Discover Our Programs</h3>
      <div class="grid">
        <div class="grid-item item1">
          <h4>Computer Science</h4>
          <p>Explore the world of technology with our innovative Computer Science program.</p>
        </div>
        <div class="grid-item item2">
          <h4>Business Administration</h4>
          <p>Learn essential business skills and strategies in our Business Administration program.</p>
        </div>
        <div class="grid-item item3">
          <h4>Engineering</h4>
          <p>Shape the future with our comprehensive Engineering program.</p>
        </div>
        <div class="grid-item item4">
          <h4>Health Sciences</h4>
          <p>Join the dynamic field of healthcare with our Health Sciences program.</p>
        </div>
        <!-- Add more grid items as needed -->
      </div>
    </section>

    <!-- New Services Section -->
    <section class="services">
      <h3>Our Services</h3>
      <div class="service-grid">
        <div class="service-item">
          <h4>Housing</h4>
          <p>Discover our comfortable and modern housing options.</p>
        </div>
        <div class="service-item">
          <h4>Dining Halls</h4>
          <p>Explore diverse culinary experiences at our dining halls.</p>
        </div>
        <div class="service-item">
          <h4>Library</h4>
          <p>Access our extensive collection and academic resources at the library.</p>
        </div>
        <div class="service-item">
          <h4>Health Center</h4>
          <p>Get quality healthcare services at our health center.</p>
        </div>
        <!-- Add more service items as needed -->
      </div>
    </section>

    <!-- New Events Section -->
    <section class="events">
      <h3>Upcoming Events</h3>
      <div class="event-list">
        <div class="event-item">
          <h4>Open House</h4>
          <p>Join us for an open house event to explore campus life.</p>
        </div>
        <div class="event-item">
          <h4>Career Fair</h4>
          <p>Connect with leading employers at our career fair.</p>
        </div>
        <div class="event-item">
          <h4>Concert Series</h4>
          <p>Enjoy our upcoming musical concert series.</p>
        </div>
        <div class="event-item">
          <h4>Sports Events</h4>
          <p>Cheer for our teams at exciting sports events.</p>
        </div>
        <!-- Add more event items as needed -->
      </div>
    </section>
  </main>
</template>

<style>
/* Existing styles for Welcome and Programs sections */

.welcome {
  background-color: #003366;
  color: #fff;
  padding: 3rem 0;
  text-align: center;
}

.welcome-content {
  max-width: 800px;
  margin: 0 auto;
}

.welcome h2, .welcome p {
  color: #fff; /* Changing text color to white for better visibility */
}

.welcome h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

/* Programs Section Styles */
.grid-section {
  margin: 3rem 0;
}

.grid-section h3 {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 2rem;
  color: #003366; /* Changing the color for better visibility */
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.grid-item {
  padding: 20px;
  border-radius: 10px;
  background-color: #f0f0f0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: #333; /* Adjusted font color for better contrast */
}

.item1 {
  grid-column: span 2;
}

.item2 {
  background-color: #e9f4f9;
}

.item3 {
  background-color: #f9ebf4;
}

.item4 {
  grid-column: span 2;
  background-color: #e9f9f4;
}

/* Styles for Services Section */
.services, .events {
  margin: 3rem 0;
}

.services h3, .events h3 {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 2rem;
  color: #003366; /* Adjusted the color for better visibility */
}

.service-grid, .event-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.service-item, .event-item {
  padding: 20px;
  border-radius: 10px;
  background-color: #f0f0f0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: #333; /* Adjusted font color for better contrast */
}

.service-item:nth-child(even), .event-item:nth-child(even) {
  background-color: #e9f4f9;
}
</style>
