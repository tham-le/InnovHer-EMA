<template>
    <div class="progress-circle-container" :style="containerStyle">
      <svg :width="size" :height="size" :viewBox="`0 0 ${size} ${size}`" class="progress-circle">
        <!-- Background circle -->
        <circle
          :cx="center"
          :cy="center"
          :r="radius"
          :style="backgroundCircleStyle"
        />
        
        <!-- Progress circle -->
        <circle
          :cx="center"
          :cy="center"
          :r="radius"
          :style="progressCircleStyle"
        />
      </svg>
      <div class="progress-content">
        <slot></slot>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    progress: {
      type: Number,
      default: 0
    },
    size: {
      type: Number,
      default: 140
    },
    strokeWidth: {
      type: Number,
      default: 4
    },
    circleColor: {
      type: String,
      default: '#ffffff'
    },
    backgroundColor: {
      type: String,
      default: 'rgba(255, 255, 255, 0.2)'
    }
  })
  
  const center = computed(() => props.size / 2)
  const radius = computed(() => (props.size - props.strokeWidth) / 2)
  const circumference = computed(() => 2 * Math.PI * radius.value)
  const progressOffset = computed(() => 
    ((100 - props.progress) / 100) * circumference.value
  )
  
  const containerStyle = computed(() => ({
    width: `${props.size}px`,
    height: `${props.size}px`
  }))
  
  const backgroundCircleStyle = computed(() => ({
    fill: 'none',
    stroke: props.backgroundColor,
    strokeWidth: `${props.strokeWidth}px`
  }))
  
  const progressCircleStyle = computed(() => ({
    fill: 'none',
    stroke: props.circleColor,
    strokeWidth: `${props.strokeWidth}px`,
    strokeLinecap: 'round',
    strokeDasharray: circumference.value,
    strokeDashoffset: progressOffset.value,
    transform: 'rotate(-90deg)',
    transformOrigin: '50% 50%',
    transition: 'stroke-dashoffset 0.5s ease'
  }))
  </script>
  
  <style scoped>
  .progress-circle-container {
    position: relative;
    display: inline-flex;
    justify-content: center;
    align-items: center;
  }
  
  .progress-circle {
    position: absolute;
    top: 0;
    left: 0;
  }
  
  .progress-content {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 1;
    width: 100%;
    height: 100%;
  }
  </style>