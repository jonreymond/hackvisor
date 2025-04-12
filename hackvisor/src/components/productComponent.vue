<script setup>
import dropdownWithSearch from './dropdownWithSearch.vue';

import { useProductStore } from '../store';


const store = useProductStore();
</script>
<template>
    <div id="product-component" class="windows">
        <h3>Product Component</h3>
        >
        <div class="product-dropdown">
            Choose to check product :
            <!-- TODO avoid multiselect from jumping -->
            <dropdownWithSearch :options=store.getProducts width="100%" />
        </div>
    </div>
</template>
<script>
</script>
<style scoped>
#product-component {
    position: relative;
}

.product-dropdown {
    position: absolute;
    top: 11%;
    right: 0;
    margin: 10px;
}
</style>