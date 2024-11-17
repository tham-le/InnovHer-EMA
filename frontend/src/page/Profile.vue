<template>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1 class="text-h4 mb-4">Mon Profil</h1>
        </v-col>
      </v-row>
  
      <!-- Loading State -->
      <v-row v-if="loading">
        <v-col cols="12" class="text-center">
          <v-progress-circular indeterminate color="primary"></v-progress-circular>
        </v-col>
      </v-row>
  
      <template v-else>
        <!-- Personal Information Section -->
        <v-row>
          <v-col cols="12" md="6">
            <v-card class="mb-4">
              <v-card-title class="d-flex align-center">
                <v-icon icon="mdi-account" class="mr-2"></v-icon>
                Informations Personnelles
              </v-card-title>
              <v-card-text>
                <v-form @submit.prevent="updateUserInfo">
                  <!-- Required Fields -->
                  <v-text-field
                    v-model="userData.username"
                    label="Nom d'utilisateur*"
                    variant="outlined"
                    density="comfortable"
                    :rules="[
                      v => !!v || 'Le nom d\'utilisateur est requis',
                      v => (v && v.length >= 3) || 'Le nom d\'utilisateur doit contenir au moins 3 caractères',
                      v => (v && v.length <= 100) || 'Le nom d\'utilisateur doit contenir moins de 100 caractères'
                    ]"
                    required
                  ></v-text-field>
                  
                  <v-text-field
                    v-model="userData.email"
                    label="Email*"
                    variant="outlined"
                    density="comfortable"
                    :rules="[v => !!v || 'L\'email est requis', v => /.+@.+\..+/.test(v) || 'L\'email doit être valide']"
                    required
                  ></v-text-field>
  
                  <!-- Optional Fields -->
                  <v-row>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="userData.first_name"
                        label="Prénom"
                        variant="outlined"
                        density="comfortable"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="userData.last_name"
                        label="Nom"
                        variant="outlined"
                        density="comfortable"
                      ></v-text-field>
                    </v-col>
                  </v-row>
  
                  <v-row>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model.number="userData.age"
                        label="Âge"
                        type="number"
                        variant="outlined"
                        density="comfortable"
                        :rules="[
                          v => !v || Number.isInteger(Number(v)) || 'L\'âge doit être un nombre entier',
                          v => !v || (v >= 0 && v <= 120) || 'L\'âge doit être entre 0 et 120'
                        ]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-select
                        v-model="userData.gender"
                        :items="[{value: 'male', title: 'Homme'}, {value: 'female', title: 'Femme'}, {value: 'other', title: 'Autre'}]"
                        label="Genre"
                        variant="outlined"
                        density="comfortable"
                      ></v-select>
                    </v-col>
                  </v-row>
  
                  <v-btn 
                    color="primary" 
                    type="submit" 
                    :loading="updating"
                    :disabled="updating"
                  >
                    Enregistrer les Informations Personnelles
                  </v-btn>
                </v-form>
              </v-card-text>
            </v-card>
          </v-col>
  
          <!-- Health Information Section -->
          <v-col cols="12" md="6">
            <v-card class="mb-4">
              <v-card-title class="d-flex align-center">
                <v-icon icon="mdi-heart-pulse" class="mr-2"></v-icon>
                Informations de Santé
              </v-card-title>
              <v-card-text>
                <v-form @submit.prevent="updateHealthInfo">
                  <v-row>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model.number="userData.height"
                        label="Taille (cm)"
                        type="number"
                        step="0.1"
                        variant="outlined"
                        density="comfortable"
                        :rules="[v => !v || (typeof v === 'number' && !isNaN(v)) || 'La taille doit être un nombre valide']"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model.number="userData.weight"
                        label="Poids (kg)"
                        type="number"
                        step="0.1"
                        variant="outlined"
                        density="comfortable"
                        :rules="[v => !v || (typeof v === 'number' && !isNaN(v)) || 'Le poids doit être un nombre valide']"
                      ></v-text-field>
                    </v-col>
                  </v-row>
  
                  <v-text-field
                    v-model="userData.condition"
                    label="Condition de Santé Principale"
                    variant="outlined"
                    density="comfortable"
                  ></v-text-field>
  
                  <v-switch
                    v-model="userData.diagnosed"
                    color="success"
                    label="Diagnostiqué par un professionnel de santé"
                    class="mb-3"
                  ></v-switch>
  
                  <v-textarea
                    v-model="userData.allergies"
                    label="Allergies"
                    variant="outlined"
                    density="comfortable"
                    rows="2"
                    auto-grow
                  ></v-textarea>
  
                  <v-textarea
                    v-model="userData.medications"
                    label="Médicaments Actuels"
                    variant="outlined"
                    density="comfortable"
                    rows="2"
                    auto-grow
                  ></v-textarea>
  
                  <v-btn 
                    color="primary" 
                    type="submit"
                    :loading="updating"
                    :disabled="updating"
                  >
                    Enregistrer les Informations de Santé
                  </v-btn>
                </v-form>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </template>
  
      <!-- Alert Component -->
      <v-snackbar
        v-model="alert.show"
        :color="alert.type"
        :timeout="3000"
        location="top"
      >
        {{ alert.message }}
        <template v-slot:actions>
          <v-btn
            variant="text"
            @click="alert.show = false"
          >
            Fermer
          </v-btn>
        </template>
      </v-snackbar>
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const baseUrl = import.meta.env.VITE_API_URL
  const userData = ref({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    age: null,
    gender: '',
    height: null,
    weight: null,
    condition: '',
    diagnosed: false,
    allergies: '',
    medications: ''
  })
  
  const loading = ref(false)
  const updating = ref(false)
  const alert = ref({
    show: false,
    type: 'success',
    message: ''
  })
  
  // Fetch user data from API
  async function fetchUserData() {
    loading.value = true
    try {
      // For testing, using user ID 1. In production, this should come from auth
      const userId = 1
      const response = await fetch(`https://2p0sciic95.execute-api.eu-central-1.amazonaws.com/v1_0/getUser`)
      const data = await response.json()
      
      if (response.ok) {
        // Update the reactive userData object with fetched data
        Object.assign(userData.value, data)
      } else {
        showAlert('error', data.error || 'Échec du chargement des données utilisateur')
      }
    } catch (error) {
      showAlert('error', 'Échec de la connexion au serveur')
    } finally {
      loading.value = false
    }
  }
  
  // Update user information
  async function updateUserInfo() {
    updating.value = true
    try {
      const userId = 1 // For testing
      const response = await fetch(`${baseUrl}/users/${userId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: userData.value.username,
          email: userData.value.email,
          first_name: userData.value.first_name,
          last_name: userData.value.last_name,
          age: userData.value.age,
          gender: userData.value.gender
        })
      })
  
      const data = await response.json()
      
      if (response.ok) {
        showAlert('success', 'Informations personnelles mises à jour avec succès')
      } else {
        showAlert('error', data.error || 'Échec de la mise à jour des informations personnelles')
      }
    } catch (error) {
      showAlert('error', 'Échec de la connexion au serveur')
    } finally {
      updating.value = false
    }
  }
  
  // Update health information
  async function updateHealthInfo() {
    updating.value = true
    try {
      const userId = 1 // For testing
      const response = await fetch(`${baseUrl}/users/${userId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          height: userData.value.height,
          weight: userData.value.weight,
          condition: userData.value.condition,
          diagnosed: userData.value.diagnosed,
          allergies: userData.value.allergies,
          medications: userData.value.medications
        })
      })
  
      const data = await response.json()
      
      if (response.ok) {
        showAlert('success', 'Informations de santé mises à jour avec succès')
      } else {
        showAlert('error', data.error || 'Échec de la mise à jour des informations de santé')
      }
    } catch (error) {
      showAlert('error', 'Échec de la connexion au serveur')
    } finally {
      updating.value = false
    }
  }
  
  // Show alert message
  function showAlert(type, message) {
    alert.value = {
      show: true,
      type,
      message
    }
  }
  
  // Fetch user data when component mounts
  onMounted(() => {
    fetchUserData()
  })
  </script>
  
  <style scoped>
  .v-container {
    max-width: 1200px;
  }
  </style>