<template>
  <main class="container">

    <Navbar />
    <Presentation class="navbar-gap"></Presentation>

    <hr>

    <div class="parent">
  <div class="div1">
    Le repository possono essere ordinate alfabeticamente per autore, per numero di stelle 
    ricevute su GitHub, o per data.
  </div>
  <div class="div2">
    <select v-model="selectedOrder">
          <option value="author" selected>autore</option>
          <option value="star">stelle</option>
          <option value="recent">più recenti</option>
          <option value="updated">più aggiornate</option>
    </select>
  </div>
  </div> 


    <FilteredList :selectedOrder="selectedOrder"/>

    <Footer />
  </main>
</template>

<script>
import FilteredList from './components/FilteredList.vue';
import Navbar from './components/Navbar.vue';
import Presentation from './components/Presentation.vue';
import Footer from './components/Footer.vue';

export default {
  components: {
    FilteredList,
    Navbar,
    Presentation,
    Footer
  },
  data() {
    return {
      selectedOrder: 'author'
    };
  }
};
</script>
