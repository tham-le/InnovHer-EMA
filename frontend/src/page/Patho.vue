<template>
  <div class="min-h-screen bg-gradient-to-b from-[#FFE4D6] to-[#ffd6c3] relative">
    <!-- Top Navigation -->
    <header class="sticky top-0 z-50 bg-transparent backdrop-blur-sm pt-4 px-4 pb-2">
      <nav class="flex gap-2 bg-white/80 p-1.5 rounded-2xl shadow-lg">
        <button 
          v-for="tab in tabs" 
          :key="tab"
          @click="currentTab = tab"
          :class="[
            'flex-1 py-2 px-3 rounded-xl font-medium transition-all text-sm',
            currentTab === tab 
              ? 'bg-[#D88C9A] text-white shadow-lg' 
              : 'text-gray-600 hover:bg-[#D88C9A]/10'
          ]"
        >
          {{ tab }}
        </button>
      </nav>
    </header>

    <main class="p-4 space-y-6 mb-20 max-w-4xl mx-auto">
      <!-- User Profile -->
      <section class="bg-white/90 backdrop-blur rounded-3xl p-4 shadow-xl">
        <div class="flex items-center gap-4">
          <div class="relative">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-[#D88C9A] to-[#c77b89] flex items-center justify-center">
              <span class="text-2xl text-white font-bold">E</span>
            </div>
            <div class="absolute -bottom-2 -right-2 w-8 h-8 rounded-xl bg-[#FFE4D6] flex items-center justify-center">
              <span class="text-[#D88C9A] font-bold">{{ painScore }}</span>
            </div>
          </div>
          <div>
            <h1 class="text-xl font-bold text-[#D88C9A]">Journal de Douleur d'Ema</h1>
            <p class="text-sm text-gray-500">Dernière mise à jour: {{ lastUpdated }}</p>
          </div>
        </div>
      </section>

      <!-- Pain Tracking -->
      <section class="bg-white/90 backdrop-blur rounded-3xl p-4 shadow-xl space-y-4">
        <header class="flex justify-between items-center">
          <h2 class="text-lg font-bold text-gray-800">Niveau de Douleur Actuel</h2>
          <button @click="toggleHistory" class="text-[#D88C9A] flex items-center gap-2">
            <span class="text-sm">{{ showHistory ? 'Masquer' : 'Afficher Historique' }}</span>
          </button>
        </header>

        <!-- Pain Level Selector -->
        <div class="flex justify-between items-center">
          <div class="flex gap-2">
            <button
              v-for="level in levels"
              :key="level"
              @click="setPainLevel(level)"
              :class="[
                'w-12 h-12 rounded-2xl flex items-center justify-center transition-all font-bold',
                painLevel === level
                  ? 'bg-[#D88C9A] text-white shadow-lg' 
                  : 'bg-gray-100'
              ]"
            >
              {{ level }}
            </button>
          </div>
        </div>

        <!-- Pain Types -->
        <div class="flex flex-wrap gap-2">
          <button 
            v-for="type in painTypes"
            :key="type"
            @click="togglePainType(type)"
            :class="[
              'px-4 py-2 rounded-xl text-sm font-medium transition-all',
              selectedTypes.includes(type)
                ? 'bg-[#D88C9A] text-white'
                : 'bg-gray-100'
            ]"
          >
            {{ type }}
          </button>
        </div>

        <!-- Notes -->
        <textarea
          v-model="notes"
          rows="3"
          class="w-full p-4 rounded-2xl bg-gray-50 resize-none"
          placeholder="Notes sur la douleur..."
        ></textarea>

        <button
          @click="savePainEntry"
          class="w-full py-3 bg-[#D88C9A] text-white rounded-2xl font-semibold"
        >
          Enregistrer
        </button>

        <!-- History Chart -->
        <div v-if="showHistory" class="h-48">
          <LineChart
            :chart-data="chartData"
            :chart-options="chartOptions"
          />
        </div>
      </section>

      <!-- Tips Section -->
      <section class="bg-white/90 backdrop-blur rounded-3xl p-4 shadow-xl">
        <h2 class="text-lg font-bold text-gray-800 mb-4">Conseils du Jour</h2>
        <ul class="space-y-3">
          <li 
            v-for="(tip, index) in dailyTips"
            :key="index"
            class="p-3 rounded-2xl bg-gray-50 flex gap-2 items-start"
          >
            <span class="w-8 h-8 bg-[#D88C9A] text-white flex items-center justify-center rounded-xl font-bold">
              {{ index + 1 }}
            </span>
            <div>
              <h3 class="font-semibold text-[#D88C9A]">{{ tip.title }}</h3>
              <p class="text-sm text-gray-600">{{ tip.description }}</p>
            </div>
          </li>
        </ul>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Line as LineChart } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip)

const tabs = ['Quotidien', 'Hebdomadaire', 'Mensuel']
const levels = [0, 1, 2, 3, 4]
const painTypes = ['Articulaire', 'Musculaire', 'Inflammatoire', 'Raideur', 'Fatigue', 'Gonflement']
const dailyTips = [
  { title: 'Exercice Doux', description: 'Commencez la journée avec 10 minutes d\'étirements.' },
  { title: 'Alimentation', description: 'Mangez des aliments riches en antioxydants aujourd\'hui.' },
  { title: 'Gestion du Stress', description: 'Prenez un moment pour pratiquer une méditation rapide.' }
]

const painHistory = ref([
  { date: '2024-03-10', level: 3, types: ['Articulaire'], notes: 'Douleur matinale' },
  { date: '2024-03-11', level: 2, types: ['Musculaire'], notes: 'Amélioration après exercice' },
  { date: '2024-03-12', level: 1, types: ['Articulaire'], notes: 'Bonne journée' }
])

const currentTab = ref('Quotidien')
const painLevel = ref(null)
const notes = ref('')
const selectedTypes = ref([])
const showHistory = ref(false)

const lastUpdated = computed(() => new Date().toLocaleString('fr-FR', { dateStyle: 'full', timeStyle: 'short' }))
const painScore = computed(() => {
  const recent = painHistory.value.slice(-3)
  return recent.length ? Math.round(recent.reduce((acc, curr) => acc + curr.level, 0) / recent.length * 100) : 0
})

const chartData = computed(() => ({
  labels: painHistory.value.map(record => new Date(record.date).toLocaleDateString('fr-FR', { weekday: 'short' })),
  datasets: [{ label: 'Niveau de Douleur', data: painHistory.value.map(record => record.level), backgroundColor: '#D88C9A', borderColor: '#D88C9A' }]
}))

const chartOptions = {
  responsive: true,
  scales: { y: { beginAtZero: true, max: 4, ticks: { stepSize: 1 } } },
  plugins: { legend: { display: false } }
}

function setPainLevel(level) {
  painLevel.value = level
}

function togglePainType(type) {
  if (selectedTypes.value.includes(type)) selectedTypes.value = selectedTypes.value.filter(t => t !== type)
  else selectedTypes.value.push(type)
}

function toggleHistory() {
  showHistory.value = !showHistory.value
}

function savePainEntry() {
  if (painLevel.value === null) {
    alert('Veuillez sélectionner un niveau de douleur.')
    return
  }
  painHistory.value.push({ date: new Date().toISOString(), level: painLevel.value, types: [...selectedTypes.value], notes: notes.value })
  notes.value = ''
  painLevel.value = null
  selectedTypes.value = []
  alert('Entrée enregistrée avec succès !')
}
</script>

<style scoped>
.backdrop-blur {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}
.transition-all {
  transition: all 0.3s ease;
}
</style>
