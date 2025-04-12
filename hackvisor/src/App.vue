<script setup>
import { ref, nextTick, onMounted, watch } from 'vue'
import { gsap } from 'gsap'
import SummaryComponent from './components/columns/summaryComponent.vue'
import ExtractComponent from './components/columns/userDataComponent.vue'
import TranscriptComponent from './components/columns/tanscriptComponent.vue'
// Component references
const columnRefs = ref([])

const columns = [
    { title: 'Client data', component: ExtractComponent },
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

    <div class="curtain-header">

        <img src="/logo.png" alt="Logo" />
        <h4>Agentic Advisor Assistant</h4>
        <div class="lan" >
            <div>FR</div>
            <div>IT</div>
        </div>
    </div>

    <div class="curtain-container">
        <div v-for="(col, index) in columns" :key="index" class="curtain-column"
            :class="{ active: activeIndex === index }" @mouseenter="activate(index)" ref="columnRefs">
            <div class="curtain-panel">
                <h4>{{ col.title }}</h4>
                <component v-if="activeIndex === index && col.component" :is="col.component" />
            </div>
        </div>
    </div>
</template>

<style scoped>

.curtain-container {
    display: flex;
    height: 93vh;
    overflow: hidden;

    background-image: url('/bkg.png');
    background-size: cover;

    padding: 25px;
    
}

 h3 {
    width : 480px;
    text-align: left;

    background-color: white !important;
    color: rgb(78, 75, 75);

}

.lan {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    width : 50px ; 
    margin : 0px ; 
    padding : 0px ; 
    margin-right: 10px;
    color : 'darkblue' ;
}

.curtain-header {


    height: 80px;
    width : 100vw; 

    padding : 10px ;
    padding-left : 25px ; 
    background-color: white;

    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

}

.curtain-header h4 {
    width : 480px;
    background-color: white !important;

    color: rgb(124, 122, 122);
    margin-top: 15px;
}

.input-group {
    width : 200px ; 
    margin : 0px ; 
    padding : 0px ; 
}

.input-group-text {
    margin : 0px; 
    color : darkblue ; 
    background-color: transparent;
    text-align: center;
    border : none ; 
    border-right: 1px solid grey;
    transform: scale(0.8);
}

.lan div:last-of-type{
    border-left: 1px solid grey; 
    padding-left : 6px ; 
}
.curtain-column {
    flex: 1;
    transition: flex 0.3s ease;
    overflow: hidden;
    cursor: pointer;
    position: relative;

    border-right: 1px solid black;

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
    border-top: 1px solid black;
    border-bottom: 1px solid black;
    height: 100%; 
    display: flex;
    align-items: start;
    flex-direction: column;
    background-color: rgb(255, 255, 255, 0.8);
}

img {
    height: 30px;
    width: auto;
}
</style>