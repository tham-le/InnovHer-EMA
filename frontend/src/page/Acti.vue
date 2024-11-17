<template>
  <v-container class="pa-0" fluid>
    <div class="min-h-screen" style="background-color: #FFE4D6;">
      <!-- Header Section -->
      <v-container class="pa-4">
        <v-card class="d-flex align-center mb-4 rounded-pill pa-3">
          <div class="relative mr-4" style="width: 48px; height: 48px;">
            <div class="position-absolute rounded-circle border-4" 
                 style="border-color: #E5B1B1; inset: 0;">
            </div>
            <div class="position-absolute rounded-circle border-4"
                 style="border-color: #E5B1B1 transparent transparent #E5B1B1; inset: 0; transform: rotate(310deg);">
            </div>
            <div class="position-absolute d-flex align-center justify-center font-weight-bold text-lg"
                 style="inset: 0;">
              86
            </div>
          </div>
          <span class="text-lg font-weight-medium">
            Note de la journée
          </span>
        </v-card>

        <div class="d-flex gap-4">
          <v-btn variant="elevated" color="white" class="rounded-pill">
            <v-icon color="#E5B1B1" class="mr-2">mdi-plus</v-icon>
            Ajouter une activité
          </v-btn>
          <v-btn variant="elevated" color="white" class="rounded-pill">
            <v-icon color="#E5B1B1" class="mr-2">mdi-play</v-icon>
            Ajouter une vidéo
          </v-btn>
        </div>
      </v-container>

      <!-- Main Content -->
      <v-container>
        <v-row>
          <v-col v-for="activity in activities" :key="activity.id" cols="12">
            <v-card class="rounded-xl">
              <div class="d-flex p-3">
                <v-avatar color="#E5B1B1" class="mr-4">
                  <v-icon>{{ activity.youtubeUrl ? 'mdi-youtube' : 'mdi-bell' }}</v-icon>
                </v-avatar>
                <div class="flex-grow-1">
                  <div class="d-flex justify-space-between align-center mb-2">
                    <span class="font-weight-bold">{{ activity.title }}</span>
                    <v-chip style="background-color: #FFB4B4">
                      {{ activity.datetime }}
                    </v-chip>
                  </div>
                  <p class="text-body-2 text-grey-darken-1">
                    {{ activity.description }}
                  </p>
                  <div v-if="activity.youtubeUrl" class="mt-2 position-relative">
                    <a :href="activity.youtubeUrl" target="_blank" rel="noopener noreferrer">
                      <v-img
                        :src="activity.thumbnailUrl"
                        height="180"
                        cover
                        class="rounded-lg"
                      >
                        <template v-slot:placeholder>
                          <v-row class="fill-height ma-0" align="center" justify="center">
                            <v-progress-circular indeterminate color="#E5B1B1"></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                      <div class="position-absolute d-flex align-center justify-center" style="inset: 0;">
                        <v-icon size="64" color="white">mdi-play-circle</v-icon>
                      </div>
                    </a>
                  </div>
                </div>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

    </div>
  </v-container>
</template>

<script setup lang="ts">
interface Activity {
  id: number;
  title: string;
  description: string;
  datetime: string;
  youtubeUrl?: string;
  thumbnailUrl?: string;
}

const activities: Activity[] = [
  {
    id: 1,
    title: "Course à pied",
    description: "Séance d'endurance avec intervalles. 5 min échauffement, 20 min course à intensité modérée, 5 min retour au calme.",
    datetime: "Lun - 30 min",
  },
  {
    id: 2,
    title: "Séance de Yoga",
    description: "Yoga flow dynamique pour améliorer la flexibilité et la force. Focus sur les postures de guerrier et les salutations au soleil.",
    datetime: "Mar - 45 min",
    youtubeUrl: "https://www.youtube.com/watch?v=3_rUl32CPbA",
    thumbnailUrl: "https://i3.ytimg.com/vi/3_rUl32CPbA/maxresdefault.jpg"
  },
  {
    id: 3,
    title: "Natation", 
    description: "Entraînement mixte avec 20 longueurs en crawl, 10 longueurs en brasse. Travail technique sur la respiration.",
    datetime: "Mer - 40 min",
  },
  {
    id: 4,
    title: "Musculation",
    description: "Circuit training complet: squats, pompes, développé couché, rowing. 3 séries de 12 répétitions pour chaque exercice.",
    datetime: "Jeu - 50 min",
    youtubeUrl: "https://www.youtube.com/watch?v=tyz0y43a8Cs",
    thumbnailUrl: "https://i3.ytimg.com/vi/tyz0y43a8Cs/maxresdefault.jpg"
  },
  {
    id: 5,
    title: "Vélo statique",
    description: "Séance cardio sur vélo avec variations d'intensité. Programme collines avec pics d'intensité toutes les 5 minutes.",
    datetime: "Ven - 35 min",
  },
]
</script>

<style scoped>
.border-4 {
  border-width: 4px;
  border-style: solid;
}

.position-absolute {
  position: absolute;
}

.relative {
  position: relative;
}

.min-h-screen {
  min-height: 100vh;
}
</style>