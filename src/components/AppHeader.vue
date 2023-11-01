<template>
  <header class="app-header">
    <div class="header-content">
      <h1>{{ title }}</h1>
      <nav>
        <ul class="tabs">
          <li v-for="tab in tabs" :key="tab.path" :class="{ active: isActiveTab(tab.path) }">
            <RouterLink :to="tab.path">{{ tab.label }}</RouterLink>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { RouterLink, useRoute } from "vue-router";

const title = 'Course Registration';

const tabs = [
  { path: '/', label: 'Home' },
  { path: '/fetch', label: 'Create an Account' },
  { path: { name: 'form' }, label: 'Form Example' },
  { path: '/schedule', label: 'Schedule View' },
  { path: '/mycourses', label: 'Course View' },
  { path: '/admin/createcourse', label: 'Create Course' },
  { path: '/login', label: 'Login' },
];

const route = useRoute();

function isActiveTab(path) {
  return path === route.path || (path === '/' && route.path === '');
}
</script>

<style>
.app-header {
  background-color: #fcfcfc;
  border-bottom: 1px solid #e0e0e0;
  padding: 1rem;
}

.app-header .header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.app-header h1 {
  font-size: 2rem;
  font-weight: bold;
  margin: 0;
}

.tabs {
  list-style: none;
  padding: 0;
  display: flex;
}

.tabs li {
  margin-right: 10px;
}

.tabs li a {
  text-decoration: none;
  color: #333;
  padding: 8px 12px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.tabs li a:hover {
  background-color: #f0f0f0;
}

.tabs li.active a {
  background-color: #333;
  color: #fff;
}
</style>
