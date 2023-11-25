<template>
  <header class="site-header">
    <div class="header-content">
      <h1 class="header-title">Section 2 Group 3 </h1>
      <nav>
        <ul class="tabs">
          <li v-for="tab in tabs" :key="tab.path" :class="{ active: isActiveTab(tab.path) }">
            <router-link :to="tab.path">{{ tab.label }}</router-link>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  props: {
    tabs: Array
  },
  methods: {
    isActiveTab(path) {
      return this.$route.path === path;
    }
  }
};
</script>

<style scoped>
/* UConn website header styles */
.site-header {
  background-color: #003366;
  color: #fff;
  padding: 20px;
}

/* Add UConn specific styling for header content */
.site-header .header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Define styles for navigation tabs */
.site-header nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.site-header nav ul li {
  display: inline;
  margin-right: 20px;
}

.site-header nav ul li a {
  text-decoration: none;
  color: #fff;
}

.site-header nav ul li.active a {
  background-color: #fff;
  color: #003366;
  border-radius: 5px;
  padding: 5px 10px;
}

/* Style for the header title */
.header-title {
  font-size: 2.5rem; /* Adjust as needed for the desired size */
  color: #fff; /* White color for better contrast */
  font-weight: bold; /* Emphasize the font weight */
}
</style>
