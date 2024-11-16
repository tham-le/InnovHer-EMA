import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/api';

export function getDietRecommendations() {
  return axios.get(`${API_BASE_URL}/diet`);
}

export function getExerciseRecommendations() {
  return axios.get(`${API_BASE_URL}/exercise`);
}

export function getMentalHealthTips() {
  return axios.get(`${API_BASE_URL}/mental-health`);
}
