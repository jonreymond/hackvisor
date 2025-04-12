<template>
    <div class="pricing-container" :class="(product.importance == 1)? 'important' : 'smaller'">

        <div class="card free">
            <div class="card-header">$0<span>/ Month</span></div>
            <h2>{{ product.name }}</h2>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2880 320">
                <path fill="#E82025" fill-opacity="1"
                    d="M0,288L37,288C74,288,148,288,222,282.7C295,277,369,267,443,240C516,213,590,171,664,165.3C738,160,811,192,885,208C959,224,1032,224,1106,186.7C1179,149,1253,75,1327,90.7C1401,107,1474,213,1548,245.3C1622,277,1695,235,1769,197.3C1843,160,1916,128,1990,128C2064,128,2137,160,2211,176C2285,192,2358,192,2432,181.3C2506,171,2579,149,2653,144C2727,139,2800,149,2837,154.7L2880,160L2880,0L2837,0C2800,0,2727,0,2653,0C2579,0,2506,0,2432,0C2358,0,2285,0,2211,0C2137,0,2064,0,1990,0C1916,0,1843,0,1769,0C1695,0,1622,0,1548,0C1474,0,1401,0,1327,0C1253,0,1179,0,1106,0C1032,0,959,0,885,0C811,0,738,0,664,0C590,0,516,0,443,0C369,0,295,0,222,0C148,0,74,0,37,0L0,0Z">
                </path>
            </svg>

            <ul>
                <li>Platform-hosted store</li>
                <li><strong>30</strong> products a month</li>
                <li>5 product images</li>
                <li>Community support</li>
            </ul>
            <button>Choose Plan</button>
        </div>

        <div class="curve"></div>
    </div>

</template>
<script>

export default {
    name: 'ProductCart',
    props: ['product'],
    data() {
        return {

        };
    },
    methods: {
        selectKeyword(keyword) {
            this.$emit('keyword-selected', keyword);
        }
    }
};

</script>
<style scoped>
.card-header {
    background-color: var(--r_primary);
    border: none;
}

h2 {
    margin-bottom: 0px;
}

.important {
    transform : calc(1.2) !important;
}

.smaller {
    transform : calc(0.8) !important
}
</style>