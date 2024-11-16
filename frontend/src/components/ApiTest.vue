<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h1 class="text-h4 mb-4">Health API Test Dashboard</h1>
      </v-col>
    </v-row>

    <!-- User Management Section -->
    <v-row>
      <v-col cols="12" md="6">
        <v-card class="mb-4">
          <v-card-title>User Management</v-card-title>
          <v-card-text>
            <v-text-field
              v-model="userId"
              label="User ID"
              variant="outlined"
              density="compact"
              :error-messages="userIdError"
            ></v-text-field>
            <v-text-field
              v-model="userName"
              label="User Name"
              variant="outlined"
              density="compact"
            ></v-text-field>
            <v-btn-group>
              <v-btn color="primary" @click="createUser" :disabled="!userName">Create User</v-btn>
              <v-btn color="info" @click="getUser" :disabled="!userId">Get User</v-btn>
              <v-btn color="warning" @click="updateUser" :disabled="!userId || !userName">Update User</v-btn>
              <v-btn color="error" @click="deleteUser" :disabled="!userId">Delete User</v-btn>
            </v-btn-group>
          </v-card-text>
        </v-card>
      </v-col>


      <!-- Pain History Section -->
      <v-col cols="12" md="6">
        <v-card class="mb-4">
          <v-card-title>Pain History</v-card-title>
          <v-card-text>
            <v-slider
              v-model="painLevel"
              label="Pain Level"
              min="0"
              max="10"
              thumb-label
            ></v-slider>
            <v-textarea
              v-model="painNotes"
              label="Pain Notes"
              variant="outlined"
              density="compact"
            ></v-textarea>
            <v-btn-group>
              <v-btn color="primary" @click="recordPain">Record Pain</v-btn>
              <v-btn color="info" @click="getPainHistory">Get History</v-btn>
            </v-btn-group>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Mood History Section -->
    <v-row>
      <v-col cols="12" md="6">
        <v-card class="mb-4">
          <v-card-title>Mood History</v-card-title>
          <v-card-text>
            <v-select
              v-model="moodLevel"
              :items="['Happy', 'Neutral', 'Sad', 'Anxious', 'Excited']"
              label="Mood"
              variant="outlined"
              density="compact"
            ></v-select>
            <v-textarea
              v-model="moodNotes"
              label="Mood Notes"
              variant="outlined"
              density="compact"
            ></v-textarea>
            <v-btn-group>
              <v-btn color="primary" @click="recordMood">Record Mood</v-btn>
              <v-btn color="info" @click="getMoodHistory">Get History</v-btn>
            </v-btn-group>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Recipe Management Section -->
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>Recipe Management</v-card-title>
          <v-card-text>
            <v-text-field
              v-model="recipeId"
              label="Recipe ID"
              variant="outlined"
              density="compact"
            ></v-text-field>
            <v-btn-group>
              <v-btn color="primary" @click="getAllRecipes">Get All Recipes</v-btn>
              <v-btn color="info" @click="getRecipe">Get Recipe</v-btn>
              <v-btn color="success" @click="addFavoriteRecipe">Add to Favorites</v-btn>
              <v-btn color="warning" @click="getFavoriteRecipes">Get Favorites</v-btn>
              <v-btn color="error" @click="removeFavoriteRecipe">Remove Favorite</v-btn>
            </v-btn-group>




          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Response Section -->
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>API Response</v-card-title>
          <v-card-text>
            <v-alert
              v-if="response"
              :type="responseType"
              border="left"
              :title="responseType === 'error' ? 'Error' : 'Success'"
              class="mb-4"
            >
              <pre>{{ response }}</pre>
            </v-alert>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const userId = ref('')
const userName = ref('')
const painLevel = ref(5)
const painNotes = ref('')
const moodLevel = ref('Neutral')
const moodNotes = ref('')
const recipeId = ref('')
const response = ref('')
const responseType = ref('info')
const baseUrl = 'http://localhost:5000/api'

async function makeRequest(url, method = 'GET', body = null) {
  try {
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json'
      }
    }
    if (body) {
      options.body = JSON.stringify(body)
    }
    const res = await fetch(`${baseUrl}${url}`, options)
    const data = await res.json()
    response.value = JSON.stringify(data, null, 2)
    responseType.value = res.ok ? 'success' : 'error'
    return data
  } catch (error) {
    response.value = error.message
    responseType.value = 'error'
  }
}

// User Management
const createUser = () => makeRequest('/users', 'POST', { name: userName.value })
const getUser = () => makeRequest(`/users/${userId.value}`)
const updateUser = () => makeRequest(`/users/${userId.value}`, 'PUT', { name: userName.value })
const deleteUser = () => makeRequest(`/users/${userId.value}`, 'DELETE')

// Pain History
const recordPain = () => makeRequest(`/users/${userId.value}/pain-history`, 'POST', {
  level: painLevel.value,
  notes: painNotes.value
})
const getPainHistory = () => makeRequest(`/users/${userId.value}/pain-history`)

// Mood History
const recordMood = () => makeRequest(`/users/${userId.value}/mood-history`, 'POST', {
  mood: moodLevel.value,
  notes: moodNotes.value
})
const getMoodHistory = () => makeRequest(`/users/${userId.value}/mood-history`)

// Recipe Management
const getAllRecipes = () => makeRequest('/recipes')
const getRecipe = () => makeRequest(`/recipes/${recipeId.value}`)
const addFavoriteRecipe = () => makeRequest(`/users/${userId.value}/favorite-recipes`, 'POST', {
  recipe_id: recipeId.value
})
const getFavoriteRecipes = () => makeRequest(`/users/${userId.value}/favorite-recipes`)
const removeFavoriteRecipe = () => makeRequest(`/users/${userId.value}/favorite-recipes/${recipeId.value}`, 'DELETE')
</script>

<style scoped>
pre {
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>