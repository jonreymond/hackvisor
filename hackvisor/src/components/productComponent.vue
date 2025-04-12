<script setup>
import dropdownWithSearch from './blocks/dropdownWithSearch.vue';

import { useProductStore } from '../store';
import productCart from './productCart.vue';

const store = useProductStore();

</script>
<template>
    <div id="product-component" class="windows">
        <h3>Recommanended products</h3>

        <div class="product-dropdown">
            Choose to check product :
            <!-- TODO avoid multiselect from jumping -->
            <dropdownWithSearch :options="store.getProducts.map(e => e.name)" width="100%" />
        </div>

        <div class="product-cards">
            <productCart v-for="(product, index) in store.getFirstProducts(3)" :key="index" :product="product" :importance="product.importance"/>
        </div>
    </div>
</template>
<script>


</script>
<style scoped>
#product-component {
    position: relative;
}

.product-cards {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 10px;
}

.product-dropdown {
    position: absolute;
    top: 11%;
    right: 0;
    margin: 10px;
}




</style>