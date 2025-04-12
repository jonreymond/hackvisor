<script setup>

import { useUserStore } from '../store';

const userStore = useUserStore();

</script>

<template>
    <div>
        hi 
        <table class="table">
            <thead>
                <tr>
                    <th v-for="(key, index) in userStore.userKeys" :key="index">{{ key }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(value, index) in userStore.user" :key="index">
                    <td v-for="(val, i) in value" :key="i">{{ val }}</td>
                </tr>
            </tbody>
       
        </table>
    </div>
</template>

<script>
export default {
    name: "SummaryComponent",
};
</script>

<style scoped>
/* Add styles here if needed */
</style>