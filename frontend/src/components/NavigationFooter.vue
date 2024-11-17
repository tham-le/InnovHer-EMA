<!-- components/NavigationFooter.vue -->
<template>
  <v-bottom-navigation
    grow
    color="primary"
    class="navigation-footer"
    :elevation="0"
    bg-color="#bf8091"
  >
    <v-btn
      to="/aliments"
      class="custom-nav-btn"
      color="white"
    >
      <template v-slot:prepend>
        <v-icon>mdi-silverware-fork-knife</v-icon>
      </template>
      <span class="nav-text">Alimentation</span>
    </v-btn>

    <v-btn
      to="/activities"
      class="custom-nav-btn"
      color="white"
    >
      <template v-slot:prepend>
        <v-icon>mdi-dumbbell</v-icon>
      </template>
      <span class="nav-text">Activités</span>
    </v-btn>

    <v-btn
      to="/patho"
      class="custom-nav-btn"
      color="white"
    >
      <template v-slot:prepend>
        <v-icon>mdi-account-injury</v-icon>
      </template>
      <span class="nav-text">Pathologie</span>
    </v-btn>

    <v-btn
      to="/ME"
      class="custom-nav-btn"
      color="white"
    >
      <template v-slot:prepend>
        <v-icon>mdi-account</v-icon>
      </template>
      <span class="nav-text">Profil</span>
    </v-btn>

    <v-btn
      to="/microbiote"
      class="custom-nav-btn"
      color="white"
    >
      <template v-slot:prepend>
        <v-icon>mdi-bacteria-outline</v-icon>
      </template>
      <span class="nav-text">Microbiote</span>
    </v-btn>
  </v-bottom-navigation>
</template>

<script setup>
// No additional script needed
</script>

<style scoped>
.navigation-footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: 100;
  padding-bottom: env(safe-area-inset-bottom);
}

.custom-nav-btn {
  flex-direction: column !important;
  height: auto !important;
  padding: 8px 0 !important;
  min-width: 0 !important;
  flex: 1;
}

.custom-nav-btn .v-btn__content {
  flex-direction: column;
  gap: 4px;
}

.nav-text {
  font-size: 12px;
  color: white;
  line-height: 1;
  margin-top: 4px;
}

.v-icon {
  color: white !important;
}

/* For iPhone safe area */
@supports (padding: max(0px)) {
  .navigation-footer {
    padding-bottom: max(env(safe-area-inset-bottom), 0px);
  }
}
</style>