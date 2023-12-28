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
      sortedItems: []
    };
  },
  mounted() {
    this.fetchData();
  },
  watch: {
    selectedOrder: 'sortItems'
  },
  methods: {
    fetchData() {
      axios.get('https://api.brockdev.it/communia')
        .then(response => {
          this.sortedItems = response.data;

          this.sortItems();
        })
        .catch(error => {
          console.error(error);
        });
    },
    sortItems() {
      const itemsCopy = [...this.sortedItems];

      // array order
      if (this.selectedOrder === 'author') {
        itemsCopy.sort((a, b) => (a.author < b.author ? -1 : 1));
      } else if (this.selectedOrder === 'star') {
        itemsCopy.sort((a, b) => (a.stars > b.stars ? -1 : 1));
      } else if (this.selectedOrder === 'recent') {
        itemsCopy.sort((a, b) => (a.created > b.created ? -1 : 1));
      } else if (this.selectedOrder === 'updated') {
        itemsCopy.sort((a, b) => (a.updated > b.updated ? -1 : 1));
      }

      this.sortedItems = itemsCopy;
    }
  }
};
</script>
