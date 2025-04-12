<template>
    <div class="curtain-container">
        <div v-for="(col, index) in columns" :key="index" class="curtain-column"
            :class="{ active: activeIndex === index }" @mouseenter="activate(index)" ref="columnRefs">
            <div class="curtain-panel">
                <h2>{{ col.title }}</h2>
                <p v-if="activeIndex === index">{{ col.content }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, nextTick, watch } from 'vue'
import { gsap } from 'gsap'

export default {
    name: 'CurtainTabs',
    data() {
        return {
            columns: [
                { title: 'Transcript', content: 'Welcome to the home section.' },
                { title: 'Summary', content: 'This is the about section.' },
                { title: 'Extract', content: 'Get in touch with us here.' }
            ],
            activeIndex: 0,
        }
    },
    mounted() {
        this.$nextTick(() => {
            this.animateColumns()
        })
    },
    watch: {
        activeIndex() {
            this.$nextTick(() => {
                this.animateColumns()
            })
        }
    },
    methods: {
        activate(index) {
            if (this.activeIndex !== index) {
                this.activeIndex = index;
            }
        },

        animateColumns() {
            const columnRefs = this.columnRefs
            columnRefs.forEach((el, index) => {
                if (!el) return
                const isActive = index === this.activeIndex
                gsap.to(el, {
                    flex: isActive ? 4 : 1,
                    duration: 0.6,
                    ease: 'power2.inOut',
                })
            })
        }
    },
    setup() {
        const columnRefs = ref([])
        return { columnRefs }
    }
}

</script>
<style scoped>


.curtain-container {
    display: flex;
    height: 100vh;
    overflow: hidden;
    background: white
    ;
}

.curtain-column {
    flex: 1;
    transition: flex 0.3s ease;
    overflow: hidden;
    cursor: pointer;
    position: relative;
    border-right: 3px solid black;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
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

.curtain-panel p {
    font-size: 1.1rem;
    line-height: 1.5;
}

.active .curtain-panel {
    background: #4c6ef5;
}
</style>