<!-- Landing.vue -->
<template>
  <div class="main-container">
    <span class="ema">EMA</span>
    <!-- Profile Circle -->
    <router-link to="/ME" class="circle-container">
      <div class="circle-content">
        <v-icon size="32" color="white">mdi-account</v-icon>
        <span class="circle-text">{{ userName }}</span>
      </div>
    </router-link>
    <!-- Circle Row -->
    <div class="circle-row">
      <router-link to="/aliments" class="circle">
        <div class="circle-content">
          <v-icon size="32" color="white">mdi-silverware-fork-knife</v-icon>
          <span class="circle-text">Alimentation</span>
        </div>
      </router-link>
      <router-link to="/activities" class="circle">
        <div class="circle-content">
          <v-icon size="32" color="white">mdi-dumbbell</v-icon>
          <span class="circle-text">Activité</span>
        </div>
      </router-link>
    </div>
    <!-- Circle Row 2 -->
    <div class="circle-row">
      <router-link to="/patho" class="circle">
        <div class="circle-content">
          <v-icon size="32" color="white">mdi-account-injury</v-icon>
          <span class="circle-text">Pathologie</span>
        </div>
      </router-link>
      <router-link to="/microbiote" class="circle">
        <div class="circle-content">
          <v-icon size="32" color="white">mdi-bacteria</v-icon>
          <span class="circle-text">Microbiote</span>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">

import { ref, onMounted } from 'vue'

const baseUrl = import.meta.env.VITE_API_URL
const userName = ref('')

onMounted(async () => {
  try {
    const userId = 1
    const response = await fetch(`${baseUrl}/users/${userId}`)
    const data = await response.json()
    userName.value = data.first_name
  } catch (error) {
    console.error('Error fetching user profile:', error)
    userName.value = 'Guest'
  }
})
// No additional script needed
</script>

<style scoped>
:root {
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Ubuntu, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --primary-color: #bf8091;
}

.main-container {
  position: relative;
  width: 100%;
  max-width: 393px;
  height: 100vh;
  margin: 0 auto;
  background: #fad5b5;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
}

.ema {
  margin-top: 30px;
  color: #bf8091;
  font-family: 'Agbalumo', sans-serif;
  font-size: 50px;
  font-weight: 400;
  line-height: 74px;
  text-align: center;
  letter-spacing: 2.5px;
}

.circle-container {
  width: clamp(120px, 30vw, 140px);
  height: clamp(120px, 30vw, 140px);
  margin: 25px 0;
  background: #bf8091;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  cursor: pointer;
  transition: transform 0.2s;
}

.circle-container:hover {
  transform: scale(1.05);
}

.circle {
  width: clamp(120px, 30vw, 140px);
  height: clamp(120px, 30vw, 140px);
  background: #bf8091;
  border-radius: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  transition: transform 0.2s;
}

.circle:hover {
  transform: scale(1.25);
}

.circle-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.circle-text {
  color: white;
  font-size: 16px;
  font-weight: 500;
  font-family: Helvetica, var(--default-font-family);
}

.circle-row {
  width: 100%;
  max-width: 340px;
  margin: 35px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

@media (max-width: 320px) {
  .circle-text {
    font-size: 14px;
  }
}
</style>