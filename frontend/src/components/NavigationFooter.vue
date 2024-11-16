<!-- components/NavigationFooter.vue -->
<template>
  <v-bottom-navigation
    v-model="value"
    grow
    color="primary"
    class="navigation-footer"
  >
    <v-btn to="/aliments">
      <v-icon>mdi-food-apple</v-icon>
      <span>Alimentation</span>
    </v-btn>

    <v-btn to="/activities">
      <v-icon>mdi-run</v-icon>
      <span>Activités</span>
    </v-btn>

    <v-btn to="/patho">
      <v-icon>mdi-heart-pulse</v-icon>
      <span>Pathologie</span>
    </v-btn>

    <v-btn to="/profile">
      <v-icon>mdi-account</v-icon>
      <span>Profil</span>
    </v-btn>

    <v-btn to="/microbiote">
      <v-icon>mdi-bacteria</v-icon>
      <span>Microbiote</span>
    </v-btn>
  </v-bottom-navigation>
</template>

<script setup>
import { ref } from 'vue'

const value = ref(0)
</script>

<style scoped>
.navigation-footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: 100;
}

/* Hide on larger screens if desired */
@media (min-width: 960px) {
  .navigation-footer {
    display: none;
  }
}
</style>
