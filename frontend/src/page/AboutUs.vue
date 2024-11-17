<template>
  <div class="about-container">
    <div class="header">
      <router-link to="/" class="back-button">
        <span class="back-arrow">←</span> Retour
      </router-link>
      <h1 class="title">Notre Histoire</h1>
    </div>

    <div class="story-container">
      <div class="story-section">
        <h2>L'Histoire d'EMA</h2>
        <p class="story-text">
          EMA porte le nom de sa source d'inspiration : Ema, la mère d'Andrea. Pendant 5 ans, mère et fils ont traversé ensemble le parcours difficile de la polyarthrite rhumatoïde. Cette expérience personnelle a inspiré Andrea à créer une solution qui pourrait transformer la vie des patients atteints de maladies rhumatismales.
        </p>
        
        <div class="quote">
          "Durant ces 5 années de combat contre la maladie avec ma mère Ema, j'ai compris qu'un suivi précis et régulier était la clé pour améliorer sa qualité de vie. C'est de cette prise de conscience qu'est née l'application EMA."
          <span class="quote-author">- Andrea</span>
        </div>
      </div>

      <div class="story-section">
        <h2>Une Approche Scientifique</h2>
        <p class="story-text">
          L'application EMA se distingue par son approche basée sur des données scientifiques prouvées :
        </p>
        <ul class="features-list">
          <li>Suivi de santé quotidien personnalisé et continu</li>
          <li>Plans de repas adaptés selon les régimes anti-inflammatoires validés scientifiquement</li>
          <li>Recommandations d'activités physiques adaptées à chaque patient</li>
          <li>Analyses détaillées des facteurs influençant les symptômes</li>
        </ul>
      </div>

      <div class="story-section">
        <h2>Résultats Prouvés</h2>
        <p class="story-text">
          Les résultats de notre application parlent d'eux-mêmes :
        </p>
        <div class="results-grid">
          <div class="result-item">
            <span class="result-title">1er Mois</span>
            <p>Amélioration notable de la gestion des symptômes grâce au suivi quotidien</p>
          </div>
          <div class="result-item">
            <span class="result-title">6 Mois</span>
            <p>Réduction significative des crises grâce à l'identification des facteurs déclencheurs</p>
          </div>
          <div class="result-item">
            <span class="result-title">2 Ans</span>
            <p>Transformation durable de la qualité de vie avec une meilleure maîtrise de la maladie</p>
          </div>
        </div>
      </div>

      <div class="story-section">
        <h2>Notre Engagement</h2>
        <p class="story-text">
          EMA est plus qu'une application de suivi - c'est un compagnon quotidien pour les patients atteints de maladies rhumatismales. Notre approche combine :
        </p>
        <ul class="features-list">
          <li>Des plans alimentaires basés sur la science</li>
          <li>Un accompagnement adapté à chaque patient</li>
          <li>Une analyse continue des progrès</li>
        </ul>
        <p class="story-text highlight">
          Notre engagement : accompagner chaque patient vers une meilleure qualité de vie, dès le premier mois et sur le long terme.
        </p>
      </div>

      <div class="contact-section">
        <h2>Contactez-nous</h2>
        <p class="contact-text">
          Vous souhaitez en savoir plus sur notre approche ou commencer votre parcours avec EMA ?
          <br>
          Email : contact@ema-sante.fr
          <br>
          Téléphone : 01 23 45 67 89
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
// Component logic can be added here if needed
</script>

<style scoped>
.about-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fad5b5;
  min-height: 100vh;
}

.header {
  margin-bottom: 40px;
  position: relative;
}

.back-button {
  position: absolute;
  top: 0;
  left: 0;
  text-decoration: none;
  color: #473463;
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.back-arrow {
  font-size: 20px;
}

.title {
  text-align: center;
  color: #473463;
  font-size: 32px;
  margin: 0;
  padding-top: 20px;
}

.story-section {
  background: white;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #473463;
  margin-bottom: 16px;
  font-size: 24px;
}

.story-text {
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  margin-bottom: 16px;
}

.quote {
  background: #f8f0ea;
  padding: 20px;
  border-left: 4px solid #f29c94;
  margin: 20px 0;
  font-style: italic;
  color: #555;
}

.quote-author {
  display: block;
  margin-top: 8px;
  font-weight: bold;
  color: #473463;
}

.features-list {
  list-style-type: none;
  padding: 0;
}

.features-list li {
  padding: 8px 0;
  padding-left: 24px;
  position: relative;
}

.features-list li::before {
  content: "•";
  color: #f29c94;
  font-weight: bold;
  position: absolute;
  left: 8px;
}

.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.result-item {
  background: #f8f0ea;
  padding: 16px;
  border-radius: 8px;
  text-align: center;
}

.result-title {
  display: block;
  color: #473463;
  font-weight: bold;
  font-size: 18px;
  margin-bottom: 8px;
}

.highlight {
  background: #f8f0ea;
  padding: 16px;
  border-radius: 8px;
  font-weight: 500;
}

.contact-section {
  background: #473463;
  color: white;
  border-radius: 12px;
  padding: 24px;
  text-align: center;
}

.contact-section h2 {
  color: white;
}

.contact-text {
  font-size: 16px;
  line-height: 1.8;
}

@media (max-width: 600px) {
  .about-container {
    padding: 16px;
  }
  
  .story-section {
    padding: 16px;
  }
  
  .title {
    font-size: 24px;
  }
  
  h2 {
    font-size: 20px;
  }
  
  .results-grid {
    grid-template-columns: 1fr;
  }
}
</style>