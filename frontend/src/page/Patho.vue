<template>
  <div class="min-h-screen bg-gradient-to-b from-[#FFE4D6] to-[#ffd6c3] relative">
    <!-- Top Navigation Tabs -->
    <div class="sticky top-0 z-50 bg-transparent backdrop-blur-sm pt-4 px-4 pb-2">
      <div class="flex gap-2 bg-white/80 p-1.5 rounded-2xl shadow-lg">
        <button 
          v-for="tab in ['Daily', 'Weekly', 'Monthly']" 
          :key="tab"
          @click="currentTab = tab"
          :class="[
            'flex-1 py-2 sm:py-2.5 px-3 sm:px-5 rounded-xl font-medium transition-all duration-300 text-sm sm:text-base',
            currentTab === tab 
              ? 'bg-[#D88C9A] text-white shadow-lg transform scale-105' 
              : 'text-gray-600 hover:bg-[#D88C9A]/10'
          ]"
        >
          {{ tab }}
        </button>
      </div>
    </div>

    <div class="p-3 sm:p-5 space-y-4 sm:space-y-6 mb-20 sm:mb-24 max-w-4xl mx-auto">
      <!-- User Profile Card -->
      <div class="bg-white/90 backdrop-blur rounded-3xl p-4 sm:p-6 shadow-xl">
        <div class="flex items-center gap-3 sm:gap-5">
          <div class="relative">
            <div class="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl bg-gradient-to-br from-[#D88C9A] to-[#c77b89] flex items-center justify-center shadow-lg">
              <UserIcon class="w-8 h-8 sm:w-10 sm:h-10 text-white" />
            </div>
            <div class="absolute -bottom-2 -right-2 w-8 h-8 sm:w-10 sm:h-10 rounded-xl bg-[#FFE4D6] flex items-center justify-center shadow-md">
              <span class="text-[#D88C9A] font-bold text-base sm:text-lg">86</span>
            </div>
          </div>
          <div>
            <h1 class="text-xl sm:text-2xl font-bold bg-gradient-to-r from-[#D88C9A] to-[#c77b89] bg-clip-text text-transparent">
              Andrea's Pain Diary
            </h1>
            <p class="text-sm sm:text-base text-gray-500 font-medium">Last updated: {{ lastUpdated }}</p>
          </div>
        </div>
      </div>

      <!-- Quick Actions -->
      <div class="grid grid-cols-2 gap-3 sm:gap-5">
        <button 
          v-for="action in quickActions" 
          :key="action.name"
          @click="action.action"
          class="bg-white/90 backdrop-blur p-4 sm:p-6 rounded-3xl shadow-lg flex flex-col items-center gap-2 sm:gap-3 transition-all duration-300 hover:bg-[#D88C9A] hover:text-white group transform hover:scale-105"
        >
          <component 
            :is="action.icon" 
            class="w-6 h-6 sm:w-8 sm:h-8 transition-colors group-hover:text-white"
            :class="action.iconColor"
          />
          <span class="font-semibold text-base sm:text-lg">{{ action.name }}</span>
        </button>
      </div>

      <!-- Pain Tracking Card -->
      <div class="bg-white/90 backdrop-blur rounded-3xl p-4 sm:p-8 shadow-xl space-y-6 sm:space-y-8">
        <div class="flex justify-between items-center">
          <h2 class="text-lg sm:text-xl font-bold text-gray-800">Current Pain Level</h2>
          <button 
            @click="showHistory = !showHistory"
            class="text-[#D88C9A] hover:text-[#c77b89] flex items-center gap-2 font-medium transition-colors text-sm sm:text-base"
          >
            <ActivityIcon class="w-4 h-4 sm:w-5 sm:h-5" />
            {{ showHistory ? 'Hide History' : 'Show History' }}
          </button>
        </div>

        <!-- Pain Level Selector -->
        <div class="flex justify-between items-center">
          <div class="flex gap-2 sm:gap-4">
            <button
              v-for="level in 5"
              :key="level-1"
              @click="setPainLevel(level-1)"
              :class="[
                'w-12 h-12 sm:w-14 sm:h-14 rounded-2xl flex items-center justify-center transition-all duration-300 font-bold text-base sm:text-lg',
                painLevel === level-1 
                  ? 'bg-gradient-to-br from-[#D88C9A] to-[#c77b89] text-white shadow-xl scale-110' 
                  : 'bg-gray-100 hover:bg-gray-200'
              ]"
            >
              {{ level-1 }}
            </button>
          </div>
          <div class="w-12 h-12 sm:w-14 sm:h-14 flex items-center justify-center">
            <ActivityIcon 
              :class="[
                'w-6 h-6 sm:w-8 sm:h-8 transition-all duration-300',
                painLevel >= 3 ? 'text-red-500' : painLevel >= 1 ? 'text-yellow-500' : 'text-green-500'
              ]"
            />
          </div>
        </div>

        <!-- Pain Description -->
        <div class="space-y-4 sm:space-y-6" v-if="painLevel !== null">
          <div class="flex flex-wrap gap-2 sm:gap-3">
            <button 
              v-for="tag in painTags"
              :key="tag"
              @click="toggleTag(tag)"
              :class="[
                'px-4 sm:px-5 py-2 sm:py-2.5 rounded-xl text-xs sm:text-sm font-medium transition-all duration-300',
                selectedTags.includes(tag)
                  ? 'bg-gradient-to-br from-[#D88C9A] to-[#c77b89] text-white shadow-lg'
                  : 'bg-gray-100 hover:bg-gray-200'
              ]"
            >
              {{ tag }}
            </button>
          </div>

          <div class="relative">
            <textarea
              v-model="painNotes"
              rows="4"
              class="w-full p-4 sm:p-5 rounded-2xl bg-gray-50 focus:ring-[#D88C9A] focus:border-[#D88C9A] resize-none shadow-inner text-gray-700 text-sm sm:text-base"
              placeholder="Describe your pain (optional)..."
            ></textarea>
            <button 
              @click="startVoiceInput"
              class="absolute right-3 sm:right-4 bottom-3 sm:bottom-4 p-2 sm:p-3 rounded-xl bg-gray-100 hover:bg-[#D88C9A] hover:text-white transition-all duration-300 shadow-md"
            >
              <MicIcon class="w-5 h-5 sm:w-6 sm:h-6" />
            </button>
          </div>

          <button
            @click="recordPain"
            class="w-full py-3 sm:py-4 bg-gradient-to-r from-[#D88C9A] to-[#c77b89] text-white rounded-2xl hover:shadow-xl transition-all duration-300 flex items-center justify-center gap-2 sm:gap-3 font-semibold text-base sm:text-lg transform hover:scale-105"
          >
            <span>Save Entry</span>
            <ActivityIcon class="w-5 h-5 sm:w-6 sm:h-6" />
          </button>
        </div>

        <!-- Pain History Chart -->
        <TransitionSlide>
          <div v-if="showHistory && painHistory.length" class="pt-4 sm:pt-6">
            <LineChart
              :chart-data="chartData"
              :chart-options="chartOptions"
              class="h-56 sm:h-72"
            />
          </div>
        </TransitionSlide>
      </div>

      <!-- Daily Tips -->
      <div class="bg-white/90 backdrop-blur rounded-3xl p-4 sm:p-8 shadow-xl space-y-4 sm:space-y-6">
        <h2 class="text-lg sm:text-xl font-bold flex items-center gap-2 sm:gap-3 text-gray-800">
          <HeartPulseIcon class="w-5 h-5 sm:w-6 sm:h-6 text-[#D88C9A]" />
          Daily Tips
        </h2>
        <div class="space-y-3 sm:space-y-5">
          <div 
            v-for="(tip, index) in dailyTips"
            :key="index"
            class="flex items-start gap-3 sm:gap-5 p-4 sm:p-5 rounded-2xl bg-gradient-to-br from-gray-50 to-gray-100 hover:shadow-lg transition-all duration-300 transform hover:scale-[1.02]"
          >
            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-xl bg-[#FFE4D6] flex items-center justify-center shrink-0 shadow-md">
              <component :is="tip.icon" class="w-5 h-5 sm:w-6 sm:h-6 text-[#D88C9A]" />
            </div>
            <div>
              <h3 class="font-semibold text-base sm:text-lg text-gray-800">{{ tip.title }}</h3>
              <p class="text-sm sm:text-base text-gray-600">{{ tip.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <nav class="fixed bottom-0 left-0 right-0 bg-white/90 backdrop-blur shadow-xl rounded-t-[2rem] sm:rounded-t-[2.5rem]">
      <div class="max-w-4xl mx-auto px-6 sm:px-8 py-4 sm:py-6">
        <div class="flex justify-around items-center">
          <router-link 
            v-for="item in navigation"
            :key="item.path"
            :to="item.path"
            class="flex flex-col items-center gap-1 sm:gap-2 transition-all duration-300 transform hover:scale-110"
            :class="$route.path === item.path ? 'text-[#D88C9A]' : 'text-gray-400'"
          >
            <component :is="item.icon" class="w-6 h-6 sm:w-7 sm:h-7" />
            <span class="text-xs sm:text-sm font-medium">{{ item.name }}</span>
          </router-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { Line as LineChart } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'
import {
  XIcon,
  MicIcon,
  UserIcon,
  DumbbellIcon,
  UtensilsIcon,
  HeartPulseIcon,
  ActivityIcon,
  BrainIcon
} from 'lucide-vue-next'

// Register ChartJS
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

// State
const currentTab = ref('Daily')
const painLevel = ref(null)
const painNotes = ref('')
const painHistory = ref([])
const showHistory = ref(false)
const selectedTags = ref([])
const userId = ref('1')

// Computed
const lastUpdated = computed(() => {
  return new Date().toLocaleDateString('fr-FR', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
})

// Quick Actions
const quickActions = [
  {
    name: 'Record Pain',
    icon: ActivityIcon,
    iconColor: 'text-[#D88C9A]',
    action: () => showPainRecorder()
  },
  {
    name: 'View History',
    icon: HeartPulseIcon,
    iconColor: 'text-[#D88C9A]',
    action: () => toggleHistory()
  }
]

// Pain Tags
const painTags = ['Muscle', 'Joint', 'Nerve', 'Sharp', 'Dull', 'Throbbing']

// Daily Tips
const dailyTips = [
  {
    icon: DumbbellIcon,
    title: 'Exercise Tip',
    description: 'Try gentle stretching exercises to reduce muscle tension'
  },
  {
    icon: UtensilsIcon,
    title: 'Nutrition Tip',
    description: 'Include anti-inflammatory foods in your diet today'
  },
  {
    icon: HeartPulseIcon,
    title: 'Wellness Tip',
    description: 'Practice deep breathing exercises for natural pain relief'
  }
]

// Chart Configuration
const chartData = computed(() => ({
  labels: painHistory.value.map(record => new Date(record.created_at).toLocaleDateString()),
  datasets: [{
    label: 'Pain Level',
    backgroundColor: '#D88C9A',
    borderColor: '#D88C9A',
    borderWidth: 2,
    pointBackgroundColor: '#FFE4D6',
    pointBorderColor: '#D88C9A',
    pointHoverBackgroundColor: '#D88C9A',
    pointHoverBorderColor: '#FFE4D6',
    data: painHistory.value.map(record => record.pain_level)
  }]
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
      max: 4,
      ticks: { stepSize: 1 }
    }
  },
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      backgroundColor: '#D88C9A',
      titleColor: '#FFE4D6',
      bodyColor: '#FFE4D6',
      displayColors: false,
      callbacks: {
        label: (context) => `Pain Level: ${context.raw}`
      }
    }
  }
}

// Methods
const setPainLevel = (level) => {
  painLevel.value = level
}

const toggleTag = (tag) => {
  const index = selectedTags.value.indexOf(tag)
  if (index === -1) {
    selectedTags.value.push(tag)
  } else {
    selectedTags.value.splice(index, 1)
  }
}

const startVoiceInput = () => {
  // Implement voice input functionality
}

const recordPain = async () => {
  try {
    const response = await fetch(`${baseUrl}/users/${userId.value}/pain-history`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        pain_level: painLevel.value,
        pain_type: selectedTags.value.join(', '),
        description: painNotes.value
      })
    })

    if (response.ok) {
      painNotes.value = ''
      selectedTags.value = []
      await fetchPainHistory()
      showSuccessMessage('Pain entry recorded successfully')
    }
  } catch (err) {
    showErrorMessage('Failed to record pain entry')
  }
}

const fetchPainHistory = async () => {
  try {
    const response = await fetch(`${baseUrl}/users/${userId.value}/pain-history`)
    if (response.ok) {
      painHistory.value = await response.json()
    }
  } catch (err) {
    showErrorMessage('Failed to fetch pain history')
  }
}

// Lifecycle
onMounted(() => {
  fetchPainHistory()
})
</script>

<style scoped>
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}

.router-link-active {
  color: #D88C9A;
}

/* Glassmorphism effect */
.backdrop-blur {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

/* Smooth transitions */
.transform {
  transition: transform 0.3s ease;
}

/* Card hover effects */
.hover\:shadow-xl:hover {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}
</style>