<script setup>
import navbar from './components/navigationBar.vue'
import userComponent from './components/userComponent.vue'
import keywordComponent from './components/keywordComponent.vue'
import productComponent from './components/productComponent.vue'
</script>

<template>
  <main>
    <!-- Main has three components -->

    <!-- 1. That displays the user data -->
    <div id="c1">
      <userComponent />
    </div>
    <!-- 2. That displays the keyword graph -->
    <div id="c2">
      <keywordComponent />
      <!-- 3. That displays the products displayed-->
      <productComponent />
    </div>
  </main>
</template>

<style>


main {
  display: flex;
  flex-direction: row;
  height : 100vh ; 
  width : 100vw; 
}


#c1 {
  height : 100%; 
  width : 100% ; 
}


#c2 {
  height : 50%; 
  width : 100% ; 
}

</style>
