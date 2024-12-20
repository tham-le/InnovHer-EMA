import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'

export default defineConfig({
  plugins: [
    vue(),
    vuetify({ autoImport: true }),
  ],
  resolve: {
    alias: {
      '@': '/src',
    },
  },
  optimizeDeps: {
    include: ['vue', 'vuetify']
  },  // Added comma here
  build: {
    rollupOptions: {
      external: ['vue-chartjs', 'chart.js']
    }
  }
})