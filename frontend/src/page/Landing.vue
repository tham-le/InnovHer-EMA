<template>
  <div class="main-container">
    <router-link to="/AboutUs">
      <span class="ema">EMA</span>
    </router-link>
    
    <!-- Profile Circle -->
    <router-link to="/ME" class="circle-container">
      <progress-circle
        :progress="profileProgress" 
        :size="circleSize"
        :strokeWidth="8"
        circle-color="#ffffff"
        background-color="rgba(255, 255, 255, 0.2)"
      >
        <div class="circle-content">
          <v-icon :size="iconSize" color="white">mdi-account</v-icon>
          <span class="circle-text">{{ userName }}</span>
          <span class="progress-percentage">{{ profileProgress }}%</span>
        </div>
      </progress-circle>
    </router-link>

    <!-- Circle Row -->
    <div class="circle-row">
      <router-link to="/aliments" class="circle aliments">
        <progress-circle
          :progress="alimentProgress"
          :size="circleSize"
          :strokeWidth="8"
          circle-color="#ffffff"
          background-color="rgba(255, 255, 255, 0.2)"
        >
          <div class="circle-content">
            <v-icon :size="iconSize" color="white">mdi-silverware-fork-knife</v-icon>
            <span class="circle-text">Alimentation</span>
            <span class="progress-percentage">{{ alimentProgress }}%</span>
          </div>
        </progress-circle>
      </router-link>

      <router-link to="/activities" class="circle activities">
        <progress-circle
          :progress="activitiesProgress"
          :size="circleSize"
          :strokeWidth="8"
          circle-color="#ffffff"
          background-color="rgba(255, 255, 255, 0.2)"
        >
          <div class="circle-content">
            <v-icon :size="iconSize" color="white">mdi-dumbbell</v-icon>
            <span class="circle-text">Activité</span>
            <span class="progress-percentage">{{ activitiesProgress }}%</span>
          </div>
        </progress-circle>
      </router-link>
    </div>

    <!-- Circle Row 2 -->
    <div class="circle-row">
      <router-link to="/patho" class="circle patho">
        <progress-circle
          :progress="pathoProgress"
          :size="circleSize"
          :strokeWidth="8"
          circle-color="#ffffff"
          background-color="rgba(255, 255, 255, 0.2)"
        >
          <div class="circle-content">
            <v-icon :size="iconSize" color="white">mdi-account-injury</v-icon>
            <span class="circle-text">Pathologie</span>
            <span class="progress-percentage">{{ pathoProgress }}%</span>
          </div>
        </progress-circle>
      </router-link>

      <router-link to="/microbiote" class="circle microbiote">
        <progress-circle
          :progress="microbioteProgress"
          :size="circleSize"
          :strokeWidth="8"
          circle-color="#ffffff"
          background-color="rgba(255, 255, 255, 0.2)"
        >
          <div class="circle-content">
            <v-icon :size="iconSize" color="white">mdi-bacteria</v-icon>
            <span class="circle-text">Microbiote</span>
            <span class="progress-percentage">{{ microbioteProgress }}%</span>
          </div>
        </progress-circle>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import ProgressCircle from '../components/CircleProgress.vue'

const baseUrl = import.meta.env.VITE_API_URL
const userName = ref('')
const profileProgress = ref(85)
const alimentProgress = ref(70)
const activitiesProgress = ref(60)
const pathoProgress = ref(90)
const microbioteProgress = ref(75)

// Responsive circle size based on viewport width
const circleSize = computed(() => {
  const vw = Math.min(document.documentElement.clientWidth, window.innerWidth)
  return Math.min(Math.max(vw * 0.25, 100), 140) // Between 100px and 140px
})

// Responsive icon size
const iconSize = computed(() => {
  return circleSize.value * 0.23 // Approximately 32px when circle is 140px
})

// Get user data from API
const getUser = async (userId) => {
  try {
    const response = await fetch(`https://2p0sciic95.execute-api.eu-central-1.amazonaws.com/v1_0/getUser`)
    if (!response.ok) {
      throw new Error('Failed to fetch user data')
    }
    return await response.json()
  } catch (error) {
    console.error('Error fetching user:', error)
    return null
  }
}

onMounted(async () => {
  try {
    const userId = 1
    const userData = await getUser(userId)
    if (userData) {
      userName.value = userData.first_name
    } else {
      userName.value = 'Guest'
    }

    // You can add API calls here to fetch real progress data
    // For now using static values for demonstration
  } catch (error) {
    console.error('Error in component initialization:', error)
    userName.value = 'Guest'
  }
  
  // Add resize listener for responsive updates
  window.addEventListener('resize', () => {
    // Force recompute of circle and icon sizes
    circleSize.value
    iconSize.value
  })
})
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
  margin-top: clamp(20px, 5vh, 30px);
  color: #bf8091;
  font-family: 'Agbalumo', sans-serif;
  font-size: clamp(40px, 8vw, 50px);
  font-weight: 400;
  line-height: 1.5;
  text-align: center;
  letter-spacing: 2.5px;
}

.circle-container {
  margin: clamp(15px, 4vh, 25px) 0;
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
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  transition: transform 0.2s;
}

.circle.aliments {
  background: #98D8AA;  /* Pastel green */
}

.circle.activities, .circle.patho {
  background: #A7C7E7;  /* Pastel blue */
}

.circle.microbiote {
  background: #C8A2C8;  /* Pastel purple */
}

.circle:hover {
  transform: scale(1.25);
}

.circle-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: clamp(4px, 1vh, 8px);
}

.progress-percentage {
  font-size: clamp(12px, 2.5vw, 14px);
  color: white;
  opacity: 0.9;
}

.circle {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
}

.circle-text {
  color: white;
  font-size: clamp(14px, 3vw, 16px);
  font-weight: 500;
  font-family: Helvetica, var(--default-font-family);
}

.circle-row {
  width: 100%;
  max-width: clamp(280px, 80vw, 340px);
  margin: clamp(20px, 5vh, 35px) 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

@media (max-width: 320px) {
  .circle-text {
    font-size: 12px;
  }
  
  .progress-percentage {
    font-size: 10px;
  }
}

.progress-text {
  font-size: clamp(12px, 2.5vw, 14px);
  color: white;
  margin-top: clamp(4px, 1vh, 6px);
  opacity: 0.9;
}

.circle-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: clamp(4px, 1vh, 8px);
  z-index: 1;
}

/* Update circle styles to accommodate progress bar */
.circle-container, .circle {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* Animation for progress bars */
@keyframes progress {
  from {
    stroke-dashoffset: 100;
  }
  to {
    stroke-dashoffset: 0;
  }
}
</style>