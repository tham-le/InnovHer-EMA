<template>
  <div class="min-h-screen bg-gradient-to-b from-[#FFE4D6] to-[#ffd6c3] relative">
    <!-- Header Section -->
    <div class="sticky top-0 z-50 bg-transparent backdrop-blur-sm pt-4 px-4 pb-2">
      <div class="flex gap-2 bg-white/80 p-1.5 rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300">
        <h1 class="text-2xl font-bold text-[#473463]">Microbiote Intestinal</h1>
      </div>
    </div>

    <!-- Main Content -->
    <div class="p-4">
      <!-- Introduction Card -->
      <div class="bg-white/90 backdrop-blur rounded-3xl shadow-lg p-6 mb-4 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
        <h2 class="text-xl font-bold text-[#473463] mb-3">Le Microbiote Intestinal Humain</h2>
        <p class="text-gray-700 leading-relaxed">
          Du grec mikrós « petit », et biôtós, « vivre », le microbiote intestinal représente l'ensemble des microorganismes présents dans notre système digestif.
        </p>
      </div>

      <!-- Key Facts Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-6">
        <div class="bg-white/90 backdrop-blur rounded-3xl shadow-lg p-6 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 border border-[#F29C94]/10">
          <h3 class="text-lg font-bold text-[#473463] mb-3 flex items-center">
            <span class="w-2 h-2 bg-[#F29C94] rounded-full mr-2"></span>
            Composition
          </h3>
          <ul class="space-y-3">
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Archées
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Bactéries
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Levures
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Virus associés
            </li>
          </ul>
        </div>

        <div class="bg-white/90 backdrop-blur rounded-3xl shadow-lg p-6 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 border border-[#F29C94]/10">
          <h3 class="text-lg font-bold text-[#473463] mb-3 flex items-center">
            <span class="w-2 h-2 bg-[#F29C94] rounded-full mr-2"></span>
            Fonctions Principales
          </h3>
          <ul class="space-y-3">
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Digestion des fibres
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Synthèse de vitamines
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Maturation immunitaire
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Régulation métabolique
            </li>
          </ul>
        </div>

        <div class="bg-white/90 backdrop-blur rounded-3xl shadow-lg p-6 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 border border-[#F29C94]/10">
          <h3 class="text-lg font-bold text-[#473463] mb-3 flex items-center">
            <span class="w-2 h-2 bg-[#F29C94] rounded-full mr-2"></span>
            Impact sur la Santé
          </h3>
          <ul class="space-y-3">
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Système immunitaire
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Métabolisme
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Digestion
            </li>
            <li class="flex items-center gap-3 text-gray-700 hover:text-[#473463] transition-colors">
              <span class="text-[#F29C94] text-lg">•</span>
              Santé mentale
            </li>
          </ul>
        </div>
      </div>

      <!-- Research Section -->
      <div class="bg-white/90 backdrop-blur rounded-3xl shadow-lg p-6 mb-20 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 border border-[#F29C94]/10">
        <h3 class="text-lg font-bold text-[#473463] mb-3 flex items-center">
          <span class="w-2 h-2 bg-[#F29C94] rounded-full mr-2"></span>
          Recherches Récentes
        </h3>
        <p class="text-gray-700 leading-relaxed">
          Les avancées scientifiques depuis les années 2000 ont permis de mieux comprendre le rôle du microbiote dans notre santé, notamment grâce aux techniques de séquençage haut débit.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
// Component logic can be added here if needed
</script>