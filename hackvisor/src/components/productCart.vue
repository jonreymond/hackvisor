<template>
    <div class="pricing-container"  >
        <div class="card free">
            <div class="card-header">$0<span>/ Month</span></div>
            <h2>{{product.name}} {{ importance }}</h2>
            <ul>
                <li>Platform-hosted store</li>
                <li><strong>30</strong> products a month</li>
                <li>5 product images</li>
                <li>Community support</li>
            </ul>
            <button>Choose Plan</button>
        </div>
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