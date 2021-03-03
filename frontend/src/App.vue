<template>
  <div id="app">
    <navbar />
    <b-container>
      <router-view />
    </b-container>
  </div>
</template>
<script>
import Navbar from "@/views/Navbar.vue";
export default {
  name: "App",
  components: { Navbar }
};
</script>

<style></style>
