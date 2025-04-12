<script setup>
import tanscriptComponent from './components/tanscriptComponent.vue';
</script>
<template>
    <h3>Rafeissen - Processing </h3>
    <div class="circle_container">
        <div v-for="circle in circles" :key="circle" class="circle" @click="handleClick(circle)"
            :style="{ marginTop: `${(circle.id - 1) * 15}vh` }">
            {{ circle.name }}
        </div>
    </div>

    <div class="overlay" v-show="currentFocus !== null" @click="currentFocus = null"></div>
    <div class="popup" v-show="currentFocus == 1"> 

        <tanscriptComponent  />

    </div>
</template>
<script>

export default {
    name: 'App3Stages',
    data() {
        return {
            currentFocus: 1,
            circles: [
                { id: 1, name: 'Transcript', componentName: 'TranscriptComponent' },
                { id: 2, name: 'Summary', componentName: 'SummaryComponent' },
                { id: 3, name: 'Extract', componentName: 'ExtractComponent' },
            ],

        }
    },
    methods: {
        handleClick(circle) {
            console.log("clicked", circle);
            this.currentFocus = circle.id;
        }
    },
    mounted() {
        this.$emit('focus', this.currentFocus);
    }
}
</script>
<style scoped>
.circle {
    width: 20vw;
    height: 20vw;
    border-radius: 50%;
    background-color: var(--r_primary);

    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;

}

div.circle:hover {
    transform: scale(1.2);
    transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out;
    opacity: 1;
}

div.circle {
    transform: scale(0.8)
}

.circle_container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    gap: 1vw;

    height: 60vh;
    width: 100vw;

}

.popup {
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    position: fixed;
    width: 80vw;
    height: 80vh;
    margin : auto ;

    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
    border-radius : 4px; 
}

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 5;
}
.overlay:hover {
    background-color: rgba(0, 0, 0, 0.7);
    transition: background-color 0.5s ease-in-out;
}
</style>