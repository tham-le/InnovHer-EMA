<template>
  <div class="main-container">
    <span class="ema">EMA</span>
    <div class="group"></div>
    <router-link to="/ME">
    <button class="frame"><span class="andrea">Andrea</span></button>
    </router-link>
    <div class="flex-row-d">
      <div class="group-1"></div>
      <div class="ellipse"></div>
      <div class="vector"></div>
    </div>
    <div class="flex-row">
    <router-link to="/aliments">
    <button class="frame-2">
      <span class="alimentation">Alimentation</span></button>
    </router-link>
    <router-link to="/activities">
    ><button class="frame-3"><span class="activite">Activité</span></button>
    </router-link>
    </div>
    <div class="flex-row-b">
      <div class="group-4"></div>
      <div class="group-5"></div>
    </div>
    <div class="flex-row-a">
      <button class="frame-6"><span class="pathologie">Pathologie</span></button
      ><button class="frame-7">
        <span class="microbiote">Microbiote</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="javascript"></script>

<style src="./landing.css"></style>
