<script setup>
import { useUserStore } from '../store';

const userStore = useUserStore();
const userData = userStore.getUser;
const userDataKeys = Object.keys(userData);
</script>
<template>
    <div id="user-component" class="windows">
        <h3>Products</h3>

        <div>
            <div>
                <transition-group name="fade" tag="div">
                    <p v-for="(line, index) in conversation" :key="index" class="fade-item">
                        <span v-if="line.speaker === 'Person A'"><strong>Person A:</strong> {{ line.text }}</span>
                        <span v-else><strong>Person B:</strong> {{ line.text }}</span>
                    </p>
                </transition-group>
            </div>

        </div>


    </div>
</template>
<script>
export default {
    data() {
        return {
            conversation: [
                { speaker: 'Person A', text: 'Hello, how can I help you today?' },
                { speaker: 'Person B', text: 'I have a question about my account.' },
                { speaker: 'Person A', text: 'Sure, what would you like to know?' },
                { speaker: 'Person B', text: 'Can you tell me my balance?' },
            ],
        };
    },
    mounted() {
        // Fetch user data from the store

    },
};
</script>
<style scoped>
body {
  font-family: 'Segoe UI', sans-serif;
  background: linear-gradient(to right, #dfe9f3, #ffffff);
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  margin: 0;
}

.pricing-container {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
  justify-content: center;
  padding: 2rem;
}

.card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  width: 300px;
  text-align: center;
  overflow: hidden;
  position: relative;
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
}

.card-header {
  padding: 2rem 1rem 1rem;
  color: #fff;
  font-size: 2rem;
  font-weight: bold;
  position: relative;
}

.card-header span {
  display: block;
  font-size: 0.9rem;
  font-weight: normal;
}

.card h2 {
  margin: 0;
  font-size: 1.4rem;
  color: #fff;
  margin-bottom: 1rem;
}

.card ul {
  background: #fff;
  margin: 0;
  padding: 1.5rem;
  list-style: none;
  color: #444;
  text-align: left;
}

.card ul li {
  margin: 0.5rem 0;
}

button {
  background: #ccc;
  border: none;
  padding: 0.8rem 2rem;
  margin-bottom: 1.5rem;
  border-radius: 25px;
  cursor: pointer;
  font-weight: bold;
}

.highlighted {
  background: #5e00a2;
  color: white;
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 130px;
  border-bottom-left-radius: 100% 30%;
  border-bottom-right-radius: 100% 30%;
  z-index: -1;
}

.card.free::before {
  background: linear-gradient(to right, #ff0066, #ff4da6);
}

.card.merchant::before {
  background: linear-gradient(to right, #7f00ff, #e100ff);
}

.card.enterprise::before {
  background: linear-gradient(to right, #00b09b, #96c93d);
}

.card.free h2,
.card.merchant h2,
.card.enterprise h2 {
  color: #fff;
}

.card.featured {
  transform: scale(1.05);
  z-index: 2;
}


</style>