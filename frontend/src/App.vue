<!-- App.vue -->
<template>
  <v-app>
    <!-- Custom Header - Hidden on landing page -->
    <navigation-header />

    <!-- Main content -->
    <v-main>
      <v-container 
        fluid 
        class="pa-0 fill-height main-container"
        :style="{ backgroundColor: '#FAD5B5' }"
      >
        <router-view v-slot="{ Component }">
          <v-fade-transition mode="out-in">
            <component :is="Component" :userId="1" />
          </v-fade-transition>
        </router-view>
      </v-container>
    </v-main>

    <!-- Custom Navigation Footer - Hidden on landing page -->
    <navigation-footer v-if="!isLandingPage" />
  </v-app>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import NavigationFooter from './components/NavigationFooter.vue'
import NavigationHeader from './components/NavigationHeader.vue'

const route = useRoute()

// Check if we're on the landing page
const isLandingPage = computed(() => {
  return route.path === '/'
})
</script>

<style>
/* Global styles */
:root {
  --footer-height: 64px;
  --header-height: 56px;
  --safe-area-bottom: env(safe-area-inset-bottom, 0px);
  --safe-area-top: env(safe-area-inset-top, 0px);
}

.v-application {
  background-color: #FAD5B5 !important;
}

.main-container {
  /* Adjust padding based on whether we're on the landing page */
  padding-bottom: v-bind(isLandingPage ? '0px' : 'calc(var(--footer-height) + var(--safe-area-bottom))') !important;
  padding-top: v-bind(isLandingPage ? '0px' : 'calc(var(--header-height) + var(--safe-area-top))') !important;
}

/* Remove default button styles */
.v-btn {
  text-transform: none !important;
  letter-spacing: normal !important;
}

/* Custom theme colors */
.v-theme--light {
  --v-theme-primary: 198, 155, 155;
  --v-theme-surface: 250, 213, 181;
}

/* For the Agbalumo font */
@font-face {
  font-family: 'Agbalumo';
  src: url('/fonts/Agbalumo-Regular.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
</style>