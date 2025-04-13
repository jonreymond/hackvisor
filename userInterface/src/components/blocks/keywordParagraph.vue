<template>
    <a :class=returnsClasses>{{ title }}</a>
</template>
<script>

export default {
    props : [
        'title',
        'selected'
    ],
    computed:{
        returnsClasses(){
            var classList = []
            if(this.selected.word == this.title){
                classList.push('selected')
            } 

            if (this.selected.related && this.selected.related.includes(this.title)) {
                classList.push('related')
            }

            return classList

        }

        },
    }

</script>
<style scoped>

a.selected {
    color : var(--c1) !important;
    font-weight: bold;
    
}

a.related {
    color : var(--c1) !important;
}

a {
    text-decoration: none !important;
    color : black ;
}
</style>