<!-- src/components/CircleMenuItem.vue -->
<template>
  <div class="menu-item-container" @click="$emit('click')">
    <div class="circular-progress-wrapper">
      <!-- Progress circle -->
      <svg class="circular-progress" viewBox="0 0 120 120">
        <!-- Background circle -->
        <circle
          class="progress-background"
          cx="60"
          cy="60"
          r="54"
          stroke-width="4"
          fill="none"
        />
        <!-- Progress circle with gradient -->
        <circle
          class="progress-bar"
          cx="60"
          cy="60"
          r="54"
          stroke-width="4"
          fill="none"
          :stroke-dasharray="circumference"
          :stroke-dashoffset="dashOffset"
          :stroke="`url(#gradient-${id})`"
        />
        <!-- Gradient definition -->
        <defs>
          <linearGradient :id="'gradient-' + id" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" :style="{ 'stop-color': startColor }" />
            <stop offset="100%" :style="{ 'stop-color': endColor }" />
          </linearGradient>
        </defs>
      </svg>
      <!-- Icon and label container -->
      <div class="content-container">
        <div class="icon-container" :style="{ backgroundColor: iconBgColor }">
          <slot name="icon"></slot>
        </div>
        <div class="label" :class="{ 'has-progress': showProgress }">
          <slot name="label"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  percentage: {
    type: Number,
    default: 0
  },
  id: {
    type: String,
    required: true
  },
  startColor: {
    type: String,
    default: '#FF6B6B'
  },
  endColor: {
    type: String,
    default: '#4ECDC4'
  },
  iconBgColor: {
    type: String,
    default: '#bf8091' // Your original purple/mauve color
  },
  showProgress: {
    type: Boolean,
    default: true
  }
})

const radius = 54
const circumference = computed(() => 2 * Math.PI * radius)
const dashOffset = computed(() =>
  circumference.value - (props.percentage / 100 * circumference.value)
)

defineEmits(['click'])
</script>

<style scoped>
.menu-item-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 1rem;
  width: clamp(120px, 30vw, 140px);
  height: clamp(120px, 30vw, 140px);
}

.circular-progress-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
}

.circular-progress {
  position: absolute;
  top: 0;
  left: 0;
  transform: rotate(-90deg);
  width: 100%;
  height: 100%;
}

.progress-background {
  stroke: rgba(177, 142, 142, 0.3);
}

.progress-bar {
  stroke-linecap: round;
  transition: stroke-dashoffset 0.8s ease-in-out;
}

.content-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.icon-container {
  width: 80%;
  height: 80%;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.5rem;
}

.label {
  font-size: 1.1rem;
  color: #000;
  text-align: center;
}
</style>