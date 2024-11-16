import { ref, onMounted, onUnmounted } from 'vue'

export function useScreen() {
  const width = ref(window.innerWidth)
  const height = ref(window.innerHeight)

  function update() {
    width.value = window.innerWidth
    height.value = window.innerHeight
  }

  onMounted(() => window.addEventListener('resize', update))
  onUnmounted(() => window.removeEventListener('resize', update))

  const isMobile = computed(() => width.value < 600)
  const isTablet = computed(() => width.value >= 600 && width.value < 960)
  const isDesktop = computed(() => width.value >= 960)

  return {
    width,
    height,
    isMobile,
    isTablet,
    isDesktop
  }
}