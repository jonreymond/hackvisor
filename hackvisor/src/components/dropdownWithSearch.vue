<script setup>
import Multiselect from 'vue-multiselect';
</script>
<template>
    <Multiselect 
        v-model="selected"
        :options="options.map(e => e.name)"
        :multiple="true"
        :close-on-select="true"
        :preserve-search="true" 
        :mulitple="true"
        :allow-empty="true"
        :placeholder="'Search...'"
        @select="validateSelection"
        @search-change="getDropdownValues" 

        />
</template>
<script>
export default {
    props : [
        'options',
        'width'
    ], 
    data() {
        return {
            selected: this.options.map(e => e.name)[0] // Default to the first option,
        }
    },
    methods: {
        validateSelection(selection) {
            this.selected = selection;
            console.log(selection + " has been selected");
        },
      
        getDropdownValues(keyword) {
            console.log("You could refresh options by querying the API with " + keyword);
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
