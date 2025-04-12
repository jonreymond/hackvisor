import './assets/main.css'
import { createPinia } from 'pinia'
import { createApp } from 'vue'
import App from './App_3bars.vue'

const pinia = createPinia()

const app = createApp(App)

app.use(pinia)



app.mount('#app')
