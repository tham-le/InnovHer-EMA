<!-- App.vue -->
<template>
  <v-app>
    <!-- App Bar -->
    <v-app-bar 
      app 
      :elevation="2"
      class="px-3"
    >
      <!-- Mobile menu button -->
      <v-app-bar-nav-icon
        @click="drawer = !drawer"
        class="d-flex d-md-none"
      ></v-app-bar-nav-icon>

      <!-- App title/logo -->
      <v-app-bar-title>EMA</v-app-bar-title>

      <!-- Desktop navigation -->
      <v-container class="d-none d-md-flex align-center">
        <v-row justify="end">
          <v-col cols="auto" v-for="item in menuItems" :key="item.path">
            <v-btn
              :to="item.path"
              variant="text"
              :ripple="false"
            >
              {{ item.title }}
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>

    <!-- Mobile navigation drawer -->
    <v-navigation-drawer
      v-model="drawer"
      temporary
      class="d-md-none"
    >
      <v-list>
        <v-list-item
          v-for="item in menuItems"
          :key="item.path"
          :to="item.path"
          :title="item.title"
          :prepend-icon="item.icon"
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Main content -->
    <v-main>
      <v-container fluid class="fill-height pa-0">
        <router-view v-slot="{ Component }">
          <v-fade-transition mode="out-in">
            <component :is="Component" />
          </v-fade-transition>
        </router-view>
      </v-container>
    </v-main>

    <!-- Bottom Navigation for Mobile -->
    <navigation-footer class="d-md-none" />
  </v-app>
</template>

