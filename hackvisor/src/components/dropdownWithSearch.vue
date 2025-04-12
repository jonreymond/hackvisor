<script setup>
import Multiselect from 'vue-multiselect';
</script>
<template>
    <Multiselect v-model="selected" :options="options.sort()" :close-on-select="true" :preserve-search="true"
        :add-label="true" :allow-empty="true" :taggable="true" @tag="addTag" :placeholder="'Search...'"
        @select="validateSelection" />
</template>
<script>
export default {
    props: [
        'options'
    ],
    data() {
        return {
            selected: null // Default to the first option,
        }
    },
    methods: {
        validateSelection(selection) {
            this.selected = selection;
            // Emit the new value to the parent component
            this.$emit('newValue', selection)
        },
        addTag(tag) {
            console.log("You could add a new tag " + tag);
            if (!this.options.includes(tag)) {
                this.options.push(tag);
            }

            this.selected = tag;
            this.validateSelection(tag);

        }
    }
}

</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>
<style scoped>
multiselect {
    background-color: #f0f0f0;
    border-radius: 5px;
    padding: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
