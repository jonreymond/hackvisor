<template>
    <a :class="(selected == title)? 'selected' : ''">{{ title }}</a>
</template>
<script>

export default {
    props : [
        'title',
        'selected'
    ],
}
</script>
<style scoped>

a.selected {
    color : var(--c1) !important;
    font-weight: bold;

}

a {
    text-decoration: none !important;
    color : black ;
}
</style>