<template>
  <div class="home">
    <!-- <TableComponent :items="items" :fields="fields" /> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import TableComponent from "@/components/Table.vue";

export default {
  name: "Home",
  props: ["user"],
  components: {
    // TableComponent
  },
  data() {
    return {
      items: [
        {
          isActive: true,
          age: 40,
          name: { first: "Aickerson", last: "Macdonald" }
        },
        { isActive: false, age: 21, name: { first: "Larsen", last: "Shaw" } },
        {
          isActive: false,
          age: 9,
          name: { first: "Mini", last: "Navarro" }
        },
        { isActive: false, age: 89, name: { first: "Geneva", last: "Wilson" } },
        { isActive: true, age: 38, name: { first: "Jami", last: "Carney" } },
        { isActive: false, age: 27, name: { first: "Essie", last: "Dunlap" } },
        { isActive: true, age: 40, name: { first: "Thor", last: "Macdonald" } },
        {
          isActive: true,
          age: 87,
          name: { first: "Larsen", last: "Shaw" }
        },
        { isActive: false, age: 26, name: { first: "Mitzi", last: "Navarro" } },
        {
          isActive: false,
          age: 22,
          name: { first: "Genevieve", last: "Wilson" }
        },
        { isActive: true, age: 38, name: { first: "John", last: "Carney" } },
        { isActive: false, age: 29, name: { first: "Dick", last: "Dunlap" } }
      ],
      fields: [
        {
          key: "name",
          label: "Person full name",
          sortable: true,
          sortDirection: "desc"
        },
        {
          key: "age",
          label: "Person age",
          sortable: true,
          class: "text-center"
        },
        {
          key: "isActive",
          label: "Is Active",
          formatter: value => {
            return value ? "Yes" : "No";
          },
          sortable: true,
          sortByFormatted: true,
          filterByFormatted: true
        },
        { key: "actions", label: "Actions" }
      ]
    };
  },
  created() {
    document.title = "Dashboard";
  }
};
</script>
