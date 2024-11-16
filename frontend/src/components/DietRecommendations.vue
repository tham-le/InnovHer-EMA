<template>
    <div>
      <h1 class="text-h4 mb-6">Diet Recommendations for Rheumatism</h1>
      
      <v-row>
        <!-- Anti-inflammatory Foods -->
        <v-col cols="12" md="4">
          <v-card class="mb-4">
            <v-card-title class="primary white--text">
              Anti-inflammatory Foods
            </v-card-title>
            <v-card-text>
              <v-list>
                <v-list-item v-for="food in recommendations.anti_inflammatory_foods" :key="food.name">
                  <v-list-item-content>
                    <v-list-item-title>{{ food.name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ food.benefits }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
  
        <!-- Foods to Avoid -->
        <v-col cols="12" md="4">
          <v-card class="mb-4">
            <v-card-title class="secondary white--text">
              Foods to Avoid
            </v-card-title>
            <v-card-text>
              <v-list>
                <v-list-item v-for="food in recommendations.foods_to_avoid" :key="food.name">
                  <v-list-item-content>
                    <v-list-item-title>{{ food.name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ food.reason }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
  
        <!-- Sample Meal Plan -->
        <v-col cols="12" md="4">
          <v-card>
            <v-card-title class="accent white--text">
              Sample Meal Plan
            </v-card-title>
            <v-card-text>
              <v-timeline dense>
                <v-timeline-item v-for="meal in recommendations.meal_plan_example" 
                               :key="meal.meal"
                               small>
                  <template v-slot:opposite>
                    <strong>{{ meal.meal }}</strong>
                  </template>
                  <div>{{ meal.suggestion }}</div>
                </v-timeline-item>
              </v-timeline>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </template>
  
  <script>
  import { getDietRecommendations } from '@/services/api'
  
  export default {
    name: 'DietRecommendations',
    
    data: () => ({
      recommendations: {
        anti_inflammatory_foods: [],
        foods_to_avoid: [],
        meal_plan_example: []
      },
      loading: false,
      error: null
    }),
  
    async created() {
      try {
        this.loading = true
        const { data } = await getDietRecommendations()
        this.recommendations = data
      } catch (error) {
        this.error = 'Failed to load diet recommendations'
        console.error(error)
      } finally {
        this.loading = false
      }
    }
  }
  </script>