// composables/useResponsive.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useResponsive() {
  const windowWidth = ref(window.innerWidth)
  const isMobile = ref(windowWidth.value < 600)
  const isTablet = ref(windowWidth.value >= 600 && windowWidth.value < 960)
  const isDesktop = ref(windowWidth.value >= 960)

  const updateWidth = () => {
    windowWidth.value = window.innerWidth
    isMobile.value = windowWidth.value < 600
    isTablet.value = windowWidth.value >= 600 && windowWidth.value < 960
    isDesktop.value = windowWidth.value >= 960
  }

  onMounted(() => {
    window.addEventListener('resize', updateWidth)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', updateWidth)
  })

  return {
    windowWidth,
    isMobile,
    isTablet,
    isDesktop
  }
}