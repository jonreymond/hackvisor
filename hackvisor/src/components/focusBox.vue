<template> 
    <div id="focus-box">
        <button @click="focus(1)"></button>
        <button @click="focus(2)"></button>
        <button @click="focus(3)"></button>
    </div>
</template>
<script>

export default {
    name: 'FocusBox',
    data() {
        return {
            currentFocus: 1
        }
    },
    methods: {
        focus(component) {
            this.currentFocus = component;
            this.$emit('focus', component);
        }
    },
    mounted() {
        this.$emit('focus', this.currentFocus);
    }
}


</script>
<style scoped>
#focus-box {
    position: absolute;
    top: 10px;
    right: 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}



</style>