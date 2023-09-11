<template>
  <div class="tablelist">

    <table role="grid">
        <thead>
          <tr>
            <th scope="col"><i class="bi bi-github"></i> Repository</th>
            <th scope="col"><i class="bi bi-star-fill"></i> Stelle</th>
            <th scope="col"><i class="bi bi-calendar-fill"></i> Attività</th>
          </tr>
        </thead>
        <tbody>
          <Repository v-for="item in sortedItems" :key="item.url" :item="item"/>
        </tbody>
      </table>
  </div>
</template>

<script>
import axios from 'axios';
import Repository from './Repository.vue';

export default {
  components: {
    Repository
  },
  props: {
    selectedOrder: String,
    items: Array
  },
  data() {
    return {
      sortedItems: [] // Inizializziamo l'array vuoto
    };
  },
  mounted() {
    this.fetchData();
  },
  watch: {
    // Osserva la prop selectedOrder
    selectedOrder: 'sortItems'
  },
  methods: {
    fetchData() {
      // Esegui la richiesta GET quando il componente è montato
      axios.get('http://localhost:8000')
        .then(response => {
          // Assegna i dati ottenuti dalla risposta a sortedItems
          this.sortedItems = response.data;

          // Ordina gli elementi in base all'opzione selezionata
          this.sortItems();
        })
        .catch(error => {
          console.error(error);
        });
    },
    sortItems() {
      // Crea una copia degli elementi per non alterare l'array originale
      const itemsCopy = [...this.sortedItems];

      // Ordina l'array in base all'opzione selezionata
      if (this.selectedOrder === 'author') {
        itemsCopy.sort((a, b) => (a.author < b.author ? -1 : 1));
      } else if (this.selectedOrder === 'star') {
        itemsCopy.sort((a, b) => (a.stars > b.stars ? -1 : 1));
      }


      this.sortedItems = itemsCopy;
    }
  }
};
</script>
