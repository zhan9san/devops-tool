<template>
  <h3>
    Hello <span v-if="username">{{ username }}</span>
  </h3>
</template>
<script>
import { mapState } from "vuex";

export default {
  computed: mapState({
    username: state => state.userModule.name
  })
};
</script>
<style></style>
