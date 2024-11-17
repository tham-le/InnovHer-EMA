<template>
  <v-container class="mx-auto" style="max-width: 1200px">

    <!-- Week Calendar navigation -->
    <v-row justify="center" align="center" class="mb-4">
      <v-col cols="auto">
        <v-btn icon @click="previousWeek">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-col>
      
      <v-col cols="auto">
        <div class="text-h6">
          <v-icon>mdi-calendar</v-icon>
          {{ formattedDateRange }}
        </div>
      </v-col>
      
      <v-col cols="auto">
        <v-btn icon @click="nextWeek">
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <!-- View Toggle -->
    <v-row justify="center" class="mb-4">
      <v-col cols="auto">
        <v-btn-toggle
          v-model="viewMode"
          mandatory
          color="primary"
        >
          <v-btn value="daily">
            <v-icon left>mdi-calendar-today</v-icon>
            Repas du jour
          </v-btn>
          <v-btn value="weekly">
            <v-icon left>mdi-calendar-week</v-icon>
            Plan hebdomadaire
          </v-btn>
        </v-btn-toggle>
      </v-col>
    </v-row>
    

    <!-- Loading State -->
    <v-row v-if="isLoading" justify="center">
      <v-col cols="12">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
      </v-col>
    </v-row>

    <!-- Daily View -->
    <template v-else-if="viewMode === 'daily'">
      <!-- Meal Plan Display -->
      <template v-if="selectedDayMeals">
        <v-row justify="center">
          <v-col cols="12" sm="10" md="8">
            <v-card>
              <v-card-title class="d-flex justify-space-between">
                <span>Plan des repas</span>
                <span class="text-subtitle-1">
                  {{ formatFullDate(selectedDate) }}
                </span>
              </v-card-title>
               <!-- Calendar days -->
              <v-row justify="center" class="flex-nowrap">
                <v-col v-for="day in weekDays" :key="day.date" cols="auto" class="px-1">
                  <v-card
                    :class="{ 'primary lighten-4': isSelectedDay(day.date) }"
                    flat
                    @click="setSelectedDate(day.date)"
                    hover
                    class="calendar-day"
                  >
                    <v-card-text class="text-center pa-2">
                      <div class="text-subtitle-2">{{ formatDay(day.date) }}</div>
                      <div class="text-h6">{{ formatDate(day.date) }}</div>
                      <div class="mt-1">
                        <v-icon v-if="day.meals" small color="success">mdi-check</v-icon>
                        <v-icon v-else small color="grey">mdi-minus</v-icon>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>

              <v-list>
                <!-- Breakfast -->
                <v-card
                  v-if="selectedDayMeals?.breakfast"
                  class="meal-item-card mb-3"
                  outlined
                >
                  <div class="d-flex align-center">
                    <v-img
                      :src="getImageUrl(selectedDayMeals.breakfast.image_url)"
                      :alt="selectedDayMeals.breakfast.name"
                      class="meal-image"
                      width="100"
                      height="100"
                      @click="showRecipeDetails(selectedDayMeals.breakfast)"
                    />
                    
                    <div class="meal-content" @click="showRecipeDetails(selectedDayMeals.breakfast)">
                      <div class="d-flex align-center mb-1">
                        <v-icon small color="orange" class="mr-2">mdi-coffee</v-icon>
                        <span class="meal-type">Petit déjeuner</span>
                      </div>
                      <div class="meal-details">
                        <div class="meal-name">{{ selectedDayMeals.breakfast.name }}</div>
                        <div class="meal-ingredients text-body-2 text--secondary">
                          {{ truncateIngredients(selectedDayMeals.breakfast.ingredients) }}
                        </div>
                      </div>
                    </div>

                    <div class="score-badge">
                      <span>86</span>
                    </div>

                    <v-btn
                      color="error"
                      icon
                      class="mr-2"
                      @click="invalidateMeal('breakfast')"
                    >
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                  </div>
                </v-card>

                <!-- Lunch -->
                <v-card
                  v-if="selectedDayMeals?.lunch"
                  class="meal-item-card mb-3"
                  outlined
                >
                  <div class="d-flex align-center">
                    <v-img
                      :src="getImageUrl(selectedDayMeals.lunch.image_url)"
                      :alt="selectedDayMeals.lunch.name"
                      class="meal-image"
                      width="100"
                      height="100"
                      @click="showRecipeDetails(selectedDayMeals.lunch)"
                    />
                    
                    <div class="meal-content" @click="showRecipeDetails(selectedDayMeals.lunch)">
                      <div class="d-flex align-center mb-1">
                        <v-icon small color="red" class="mr-2">mdi-food-fork-drink</v-icon>
                        <span class="meal-type">Déjeuner</span>
                      </div>
                      <div class="meal-details">
                        <div class="meal-name">{{ selectedDayMeals.lunch.name }}</div>
                        <div class="meal-ingredients text-body-2 text--secondary">
                          {{ truncateIngredients(selectedDayMeals.lunch.ingredients) }}
                        </div>
                      </div>
                    </div>

                    <div class="score-badge">
                      <span>86</span>
                    </div>

                    <v-btn
                      color="error"
                      icon
                      class="mr-2"
                      @click="invalidateMeal('lunch')"
                    >
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                  </div>
                </v-card>

                <!-- Dinner -->
                <v-card
                  v-if="selectedDayMeals?.dinner"
                  class="meal-item-card mb-3"
                  outlined
                >
                  <div class="d-flex align-center">
                    <v-img
                      :src="getImageUrl(selectedDayMeals.dinner.image_url)"
                      :alt="selectedDayMeals.dinner.name"
                      class="meal-image"
                      width="100"
                      height="100"
                      @click="showRecipeDetails(selectedDayMeals.dinner)"
                    />
                    
                    <div class="meal-content" @click="showRecipeDetails(selectedDayMeals.dinner)">
                      <div class="d-flex align-center mb-1">
                        <v-icon small color="purple" class="mr-2">mdi-food-turkey</v-icon>
                        <span class="meal-type">Dîner</span>
                      </div>
                      <div class="meal-details">
                        <div class="meal-name">{{ selectedDayMeals.dinner.name }}</div>
                        <div class="meal-ingredients text-body-2 text--secondary">
                          {{ truncateIngredients(selectedDayMeals.dinner.ingredients) }}
                        </div>
                      </div>
                    </div>

                    <div class="score-badge">
                      <span>86</span>
                    </div>

                    <v-btn
                      color="error"
                      icon
                      class="mr-2"
                      @click="invalidateMeal('dinner')"
                    >
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                  </div>
                </v-card>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </template>

      <!-- No Meal Plan Message -->
      <template v-else>
        <v-row justify="center">
          <v-col cols="12" sm="10" md="8">
            <v-card>
              <v-card-text class="text-center py-8">
                <v-icon large color="grey">mdi-food-off</v-icon>
                <p class="mt-2 text-subtitle-1 grey--text">
                  Aucun plan de repas pour cette journée
                </p>
                <v-btn
                  color="primary"
                  class="mt-4"
                  @click="generateMealPlan"
                  :loading="isGenerating"
                >
                  Générer un plan
                </v-btn>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </template>
    </template>
    <!-- Weekly View -->
    <template v-else-if="viewMode === 'weekly' && mealPlans.length > 0">
      <v-row justify="center">
        <v-col cols="12">
          <!-- Weekly View Toggle -->
          <v-btn-toggle
            v-model="weeklyViewMode"
            mandatory
            color="primary"
            class="mb-4 mt-2"
          >
            <v-btn value="list" :disabled="viewMode !== 'weekly'">
              <v-icon left>mdi-format-list-bulleted</v-icon>
              Vue Liste
            </v-btn>
            <v-btn value="table" :disabled="viewMode !== 'weekly'">
              <v-icon left>mdi-table</v-icon>
              Vue Tableau
            </v-btn>
          </v-btn-toggle>

          <!-- List View -->
          <template v-if="weeklyViewMode === 'list'">
            <v-expansion-panels>
              <v-expansion-panel
                v-for="day in weekDays"
                :key="day.date"
                class="mb-2"
              >
                <v-expansion-panel-title>
                  <div class="d-flex align-center">
                    <v-icon icon="mdi-calendar-today" class="mr-2"></v-icon>
                    <strong>{{ formatDay(day.date) }}</strong>
                  </div>
                </v-expansion-panel-title>
                
                <v-expansion-panel-text>
                  <v-list>
                    <!-- Breakfast -->
                    <v-list-item>
                      <template v-slot:prepend>
                        <v-icon color="orange">mdi-coffee</v-icon>
                      </template>
                      <v-list-item-title>Petit déjeuner</v-list-item-title>
                      <v-list-item-subtitle>
                        <v-chip
                          v-if="day.meals?.breakfast?.name"
                          color="success"
                          variant="outlined"
                          size="small"
                          class="mt-1"
                          @click="showRecipeDetails(day.meals.breakfast)"
                          link
                        >
                          {{ day.meals.breakfast.name }}
                        </v-chip>
                        <span v-else class="text-grey">Non planifié</span>
                      </v-list-item-subtitle>
                    </v-list-item>

                    <!-- Lunch -->
                    <v-list-item>
                      <template v-slot:prepend>
                        <v-icon color="green">mdi-food</v-icon>
                      </template>
                      <v-list-item-title>Déjeuner</v-list-item-title>
                      <v-list-item-subtitle>
                        <v-chip
                          v-if="day.meals?.lunch?.name"
                          color="success"
                          variant="outlined"
                          size="small"
                          class="mt-1"
                          @click="showRecipeDetails(day.meals.lunch)"
                          link
                        >
                          {{ day.meals.lunch.name }}
                        </v-chip>
                        <span v-else class="text-grey">Non planifié</span>
                      </v-list-item-subtitle>
                    </v-list-item>

                    <!-- Dinner -->
                    <v-list-item>
                      <template v-slot:prepend>
                        <v-icon color="purple">mdi-food-turkey</v-icon>
                      </template>
                      <v-list-item-title>Dîner</v-list-item-title>
                      <v-list-item-subtitle>
                        <v-chip
                          v-if="day.meals?.dinner?.name"
                          color="success"
                          variant="outlined"
                          size="small"
                          class="mt-1"
                          @click="showRecipeDetails(day.meals.dinner)"
                          link
                        >
                          {{ day.meals.dinner.name }}
                        </v-chip>
                        <span v-else class="text-grey">Non planifié</span>
                      </v-list-item-subtitle>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>

            <!-- Expand/Collapse All Button -->
            <v-btn
              color="primary"
              class="mt-4"
              @click="toggleAllPanels"
            >
              {{ allPanelsExpanded ? 'Réduire Tout' : 'Développer Tout' }}
            </v-btn>
          </template>

          <!-- Table View -->
          <template v-else>
            <v-table>
              <thead>
                <tr>
                  <th>Jour</th>
                  <th>Petit déjeuner</th>
                  <th>Déjeuner</th>
                  <th>Dîner</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="day in weekDays" :key="day.date">
                  <td>{{ formatDay(day.date) }}</td>
                  <td>
                    <v-chip
                      v-if="day.meals?.breakfast?.name"
                      color="success"
                      variant="outlined"
                      size="small"
                      @click="showRecipeDetails(day.meals.breakfast)"
                      link
                    >
                      {{ day.meals.breakfast.name }}
                    </v-chip>
                    <span v-else class="text-grey">Non planifié</span>
                  </td>
                  <td>
                    <v-chip
                      v-if="day.meals?.lunch?.name"
                      color="success"
                      variant="outlined"
                      size="small"
                      @click="showRecipeDetails(day.meals.lunch)"
                      link
                    >
                      {{ day.meals.lunch.name }}
                    </v-chip>
                    <span v-else class="text-grey">Non planifié</span>
                  </td>
                  <td>
                    <v-chip
                      v-if="day.meals?.dinner?.name"
                      color="success"
                      variant="outlined"
                      size="small"
                      @click="showRecipeDetails(day.meals.dinner)"
                      link
                    >
                      {{ day.meals.dinner.name }}
                    </v-chip>
                    <span v-else class="text-grey">Non planifié</span>
                  </td>
                </tr>
              </tbody>
            </v-table>
          </template>
        </v-col>
      </v-row>
    </template>

    <!-- Recipe Details Dialog -->
    <v-dialog v-model="recipeDialog.show" max-width="600">
      <v-card v-if="recipeDialog.recipe">
        <v-img
          v-if="recipeDialog.recipe.image_url"
          :src="getImageUrl(recipeDialog.recipe.image_url)"
          height="200"
          class="white--text align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        >
          <v-card-title v-text="recipeDialog.recipe.name"></v-card-title>
        </v-img>
        
        <v-card-text class="pt-4">
          <h3 class="mb-3">Ingrédients</h3>
          <v-list dense>
            <v-list-item v-for="(ingredient, index) in recipeDialog.recipe.ingredients" :key="index">
              <v-list-item-content>
                <v-list-item-title class="subtitle-1">
                  • {{ ingredient.quantity }}{{ ingredient.unit }} {{ ingredient.item }}
                </v-list-item-title>
                <v-list-item-subtitle v-if="ingredient.details" class="grey--text">
                  ({{ ingredient.details }})
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>

          <h3 class="mt-4 mb-3">Instructions</h3>
          <v-list dense class="transparent">
            <v-list-item v-for="(instruction, index) in recipeDialog.recipe.instructions" :key="index">
              <v-list-item-content>
                <v-list-item-title class="subtitle-1">
                  {{ index + 1 }}. {{ instruction }}
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card-text>
        
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="recipeDialog.show = false">Fermer</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Invalidate Meal Dialog -->
    <v-dialog v-model="invalidateDialog.show" max-width="400">
      <v-card>
        <v-card-title>Invalider ce repas</v-card-title>
        <v-card-text>
          <v-radio-group v-model="invalidateDialog.reason">
            <v-radio label="Repas à l'extérieur" value="eat_out"></v-radio>
            <v-radio label="Pas bon" value="too_bad"></v-radio>
            <v-radio label="Autre" value="other"></v-radio>
          </v-radio-group>
          <v-text-field
            v-if="invalidateDialog.reason === 'other'"
            v-model="invalidateDialog.otherReason"
            label="Précisez"
            outlined
            dense
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="invalidateDialog.show = false">Annuler</v-btn>
          <v-btn color="error" @click="confirmInvalidateMeal">Confirmer</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Alert Snackbar -->
    <v-snackbar
      v-model="alert.show"
      :color="alert.type"
      :timeout="3000"
    >
      {{ alert.message }}
      <template v-slot:action="{ attrs }">
        <v-btn
          text
          v-bind="attrs"
          @click="alert.show = false"
        >
          Fermer
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue'
import { format, addDays, subDays, startOfWeek, addWeeks, subWeeks, parseISO } from 'date-fns'
import { fr } from 'date-fns/locale'

export default {
  name: 'Aliments',
  
  setup() {
    const userId = 1 // Fixed user ID
    const baseUrl = 'http://localhost:5000/api'
    const selectedDate = ref(new Date())
    const mealPlans = ref([])
    const isLoading = ref(false)
    const isGenerating = ref(false)
    const viewMode = ref('daily')
    const alert = ref({
      show: false,
      type: 'success',
      message: ''
    })

    const recipeDialog = ref({
      show: false,
      recipe: null
    });

    const invalidateDialog = ref({
      show: false,
      mealType: null,
      reason: 'eat_out',
      otherReason: ''
    });

    const invalidateMeal = (mealType) => {
      invalidateDialog.value = {
        show: true,
        mealType,
        reason: 'eat_out',
        otherReason: ''
      };
    };

    const confirmInvalidateMeal = async () => {
      try {
        const reason = invalidateDialog.value.reason === 'other' 
          ? invalidateDialog.value.otherReason 
          : invalidateDialog.value.reason;

        const response = await fetch(`${baseUrl}/users/${userId}/meal-plan/invalidate-recipe`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            date: format(selectedDate.value, 'yyyy-MM-dd'),
            meal_type: invalidateDialog.value.mealType,
            reason: reason
          }),
        });

        if (response.ok) {
          showAlert('success', 'Demande envoyée');
          await fetchMealPlan(); // Refresh the meal plan
        } else {
          showAlert('error', 'Erreur lors de l\'invalidation du repas');
        }
      } catch (error) {
        console.error('Error invalidating meal:', error);
        showAlert('error', 'Erreur de connexion');
      } finally {
        invalidateDialog.value.show = false;
      }
    };

    const showRecipeDetails = (recipe) => {
      recipeDialog.value = {
        show: true,
        recipe
      };
    };

    // Computed Properties
    const formattedDateRange = computed(() => {
      const weekStart = startOfWeek(selectedDate.value, { weekStartsOn: 1 })
      const weekEnd = addDays(weekStart, 6)
      return `${format(weekStart, 'MMM d', { locale: fr })} - ${format(weekEnd, 'd yyyy')}`
    })

    const formatDay = (date) => {
      return format(date, 'E', { locale: fr })
    }

    const formatDate = (date) => {
      return format(date, 'd')
    }

    const formatFullDate = (date) => {
      return format(date, 'd MMM', { locale: fr })
    }

    const weekDays = computed(() => {
      const weekStart = startOfWeek(selectedDate.value, { weekStartsOn: 1 })
      return Array.from({ length: 7 }, (_, i) => {
        const date = addDays(weekStart, i)
        return {
          date,
          meals: getMealPlanForDate(date)
        }
      })
    })

    const selectedDayMeals = computed(() => {
      return getMealPlanForDate(selectedDate.value)
    })

    // Methods
    const getMealPlanForDate = (date) => {
      const dayOfWeek = date.getDay();
      const adjustedDayOfWeek = dayOfWeek === 0 ? 6 : dayOfWeek - 1;
      return mealPlans.value.find(plan => plan.day_of_week === adjustedDayOfWeek);
    }

    const fetchMealPlan = async () => {
      isLoading.value = true;
      try {
        const response = await fetch(`${baseUrl}/users/${userId}/meal-plan`);
        if (response.ok) {
          const data = await response.json();
          console.log('Fetched meal plans:', data);
          
          if (Array.isArray(data)) {
            mealPlans.value = data.map(plan => ({
              ...plan,
              week_start_date: plan.week_start_date,
              day_of_week: plan.day_of_week,
              breakfast: plan.breakfast ? {
                ...plan.breakfast,
                ingredients: typeof plan.breakfast.ingredients === 'string' 
                  ? JSON.parse(plan.breakfast.ingredients)
                  : plan.breakfast.ingredients,
                instructions: typeof plan.breakfast.instructions === 'string'
                  ? JSON.parse(plan.breakfast.instructions)
                  : plan.breakfast.instructions
              } : null,
              lunch: plan.lunch ? {
                ...plan.lunch,
                ingredients: typeof plan.lunch.ingredients === 'string'
                  ? JSON.parse(plan.lunch.ingredients)
                  : plan.lunch.ingredients,
                instructions: typeof plan.lunch.instructions === 'string'
                  ? JSON.parse(plan.lunch.instructions)
                  : plan.lunch.instructions
              } : null,
              dinner: plan.dinner ? {
                ...plan.dinner,
                ingredients: typeof plan.dinner.ingredients === 'string'
                  ? JSON.parse(plan.dinner.ingredients)
                  : plan.dinner.ingredients,
                instructions: typeof plan.dinner.instructions === 'string'
                  ? JSON.parse(plan.dinner.instructions)
                  : plan.dinner.instructions
              } : null
            }));
          } else {
            showAlert('error', 'Format de données incorrect');
          }
        } else {
          showAlert('error', 'Erreur lors du chargement du plan de repas');
        }
      } catch (error) {
        console.error('Fetch error:', error);
        showAlert('error', 'Erreur de connexion');
      } finally {
        isLoading.value = false;
      }
    };

    const generateMealPlan = async () => {
      isGenerating.value = true
      try {
        const response = await fetch(`${baseUrl}/users/${userId}/meal-plan`, {
          method: 'POST'
        })
        if (response.ok) {
          const data = await response.json()
          mealPlans.value = data.meal_plan
          showAlert('success', 'Nouveau plan de repas généré')
        } else {
          showAlert('error', 'Erreur lors de la génération du plan')
        }
      } catch (error) {
        showAlert('error', 'Erreur de connexion')
      } finally {
        isGenerating.value = false
      }
    }

    const previousWeek = () => {
      selectedDate.value = subWeeks(selectedDate.value, 1)
    }

    const nextWeek = () => {
      selectedDate.value = addWeeks(selectedDate.value, 1)
    }

    const setSelectedDate = (date) => {
      selectedDate.value = date
    }

    const isSelectedDay = (date) => {
      return format(date, 'yyyy-MM-dd') === format(selectedDate.value, 'yyyy-MM-dd')
    }

    const showAlert = (type, message) => {
      alert.value = {
        show: true,
        type,
        message
      }
    }

    const getImageUrl = (imageName) => {
      try {
        return new URL(`../assets/images/${imageName}`, import.meta.url).href
      } catch (error) {
        console.error('Error loading image:', error)
        return new URL('../assets/images/default-recipe.jpg', import.meta.url).href
      }
    }

    const truncateIngredients = (ingredients) => {
      if (typeof ingredients === 'string') {
        ingredients = JSON.parse(ingredients);
      }
      const ingredientsList = ingredients
        .map(ing => ing.item)
        .slice(0, 2)
        .join(', ');
      return ingredientsList + (ingredients.length > 2 ? '...' : '');
    };

    // Lifecycle hooks
    onMounted(() => {
      fetchMealPlan()
    })

    watch(() => format(selectedDate.value, 'yyyy-ww'), () => {
      fetchMealPlan()
    })

    return {
      selectedDate,
      mealPlans,
      isLoading,
      isGenerating,
      alert,
      viewMode,
      formattedDateRange,
      weekDays,
      selectedDayMeals,
      generateMealPlan,
      previousWeek,
      nextWeek,
      setSelectedDate,
      isSelectedDay,
      formatDay,
      formatDate,
      formatFullDate,
      showAlert,
      showRecipeDetails,
      recipeDialog,
      getImageUrl,
      truncateIngredients,
      invalidateDialog,
      invalidateMeal,
      confirmInvalidateMeal
    }
  }
}
</script>

<style scoped>
.v-card {
  border-radius: 8px;
}

.v-list-item {
  min-height: 64px;
}

.flex-nowrap {
  flex-wrap: nowrap !important;
  overflow-x: auto;
}

.cursor-pointer:hover {
  text-decoration: underline;
}

.rounded {
  border-radius: 4px;
}

.meal-plan-card {
  padding: 16px;
}

.meal-item-card {
  border-radius: 12px !important;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s;
  position: relative;
}

.meal-item-card:hover {
  transform: translateY(-2px);
}

.meal-image {
  border-radius: 8px;
  margin: 8px;
  object-fit: cover;
}

.meal-content {
  flex: 1;
  padding: 8px 16px;
}

.meal-type {
  font-size: 0.9rem;
  font-weight: 500;
  color: rgba(0, 0, 0, 0.6);
}

.meal-name {
  font-size: 1.1rem;
  font-weight: 500;
  margin-bottom: 4px;
}

.meal-ingredients {
  color: rgba(0, 0, 0, 0.6);
}

.score-badge {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #b895b3;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 16px;
  font-weight: 500;
}

:deep(.v-img__img) {
  object-fit: cover;
}
</style>
