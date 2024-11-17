<!-- components/NavigationHeader.vue -->
<template>
  <v-app-bar 
    :elevation="0"
    class="navigation-header"
    :color="backgroundColor"
    v-if="showHeader"
  >
    <v-container class="px-2">
      <div class="d-flex align-center">
        <!-- Back/Home Button -->
        <v-btn
          icon
          variant="text"
          color="#bf8091"
          size="large"
          to="/"
          class="me-2"
        >
          <v-icon size="32">mdi-home</v-icon>
        </v-btn>

        <!-- Page Title -->
        <v-app-bar-title 
          class="page-title"
          :style="{ color: '#bf8091' }"
        >
          {{ currentPageTitle }}
        </v-app-bar-title>

        <!-- Profile Icon (optional) -->
        <v-btn
          icon
          variant="text"
          color="#bf8091"
          size="large"
          to="/ME"
        >
          <v-icon>mdi-account-circle</v-icon>
        </v-btn>
      </div>
    </v-container>
  </v-app-bar>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const showHeader = computed(() => {
  return route.path !== '/'
})

const backgroundColor = computed(() => {
  return '#FAD5B5'
})

const currentPageTitle = computed(() => {
  const titles = {
    '/aliments': 'Alimentation',
    '/activities': 'Activités',
    '/patho': 'Pathologie',
    '/ME': 'Profil',
    '/microbiote': 'Microbiote'
  }
  return titles[route.path] || 'EMA'
})
</script>

<style scoped>
.navigation-header {
  border-bottom: 1px solid rgba(71, 52, 99, 0.1);
}

.page-title {
  font-family: 'Agbalumo', sans-serif;
  font-size: 24px !important;
  font-weight: 500;
}

/* iPhone safe area support */
@supports (padding: max(0px)) {
  .navigation-header {
    padding-top: max(env(safe-area-inset-top), 0px);
  }
}
</style>
