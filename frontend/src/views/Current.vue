<template>
  <div>
    <TableComponent :items="items" :fields="fields" />
  </div>
</template>

<script>
// @ is an alias to /src
import TableComponent from "@/components/Table.vue";

export default {
  name: "Current",
  components: {
    TableComponent
  },
  data() {
    return {
      items: [],
      fields: []
    };
  }
};
</script>
