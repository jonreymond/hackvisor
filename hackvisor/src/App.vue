<script setup>
import { ref, nextTick, onMounted, watch } from 'vue'
import { gsap } from 'gsap'
import SummaryComponent from './components/columns/summaryComponent.vue'
import ExtractComponent from './components/columns/userDataComponent.vue'
import TranscriptComponent from './components/columns/tanscriptComponent.vue'
// Component references
const columnRefs = ref([])

const columns = [
    { title: 'User data', component: ExtractComponent },
    { title: 'Transcript', component: TranscriptComponent },
    { title: 'Summary', component: SummaryComponent }
]

const activeIndex = ref(0)

const activate = (index) => {
    if (activeIndex.value !== index) {
        activeIndex.value = index
    }
}

const animateColumns = () => {
    columnRefs.value.forEach((el, index) => {
        if (!el) return
        const isActive = index === activeIndex.value
        gsap.to(el, {
            flex: isActive ? 4 : 1,
            duration: 0.6,
            ease: 'power2.inOut'
        })
    })
}

onMounted(() => {
    nextTick(() => animateColumns())
})

watch(activeIndex, () => {
    nextTick(() => animateColumns())
})
</script>

<template>
    <div class="curtain-container">
        <div v-for="(col, index) in columns" :key="index" class="curtain-column"
            :class="{ active: activeIndex === index }" @mouseenter="activate(index)" ref="columnRefs">
            <div class="curtain-panel">
                <h2>{{ col.title }}</h2>
                <component v-if="activeIndex === index && col.component" :is="col.component" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.curtain-container {
    display: flex;
    height: 100vh;
    overflow: hidden;

    background-image : url('/bkg.png');
    background-size: cover;
}


.curtain-column {
    flex: 1;
    transition: flex 0.3s ease;
    overflow: hidden;
    cursor: pointer;
    position: relative;
    border-right: 3px solid black;
    display: flex;
    align-items: start;
    justify-content: center;

    color: black;
}

.curtain-column:last-child {
    border-right: none;
}

.curtain-panel {
    padding: 2rem;
    text-align: center;
    width: 100%;
}

.curtain-panel h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.curtain-panel div {
    font-size: 1.1rem;
    line-height: 1.5;
}

.active .curtain-panel {

    height: 100%;
    display: flex;
    align-items: start;
    flex-direction: column;
    background-color : rgb(255, 255, 255, 0.8);
    


}
</style>