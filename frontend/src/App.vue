<template>
  <main class="container">

    <Navbar />
    <Presentation />

    <br>

    <div class="grid">
      <div class="centered">
        Ordina repository per: 
      </div>
      <div class="centered">
        <select v-model="selectedOrder">
          <option value="author" selected>autore</option>
          <option value="star">stelle</option>
        </select>
      </div>
    </div>


    <FilteredList :selectedOrder="selectedOrder"/>
  </main>
</template>

<script>
import FilteredList from './components/FilteredList.vue';
import Navbar from './components/Navbar.vue';
import Presentation from './components/Presentation.vue';
export default {
  components: {
    FilteredList,
    Navbar,
    Presentation
  },
  data() {
    return {
      selectedOrder: 'author'
    };
  }
};
</script>
