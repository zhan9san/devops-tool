<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-container>
        <b-navbar-brand @click="$router.push({ name: 'Home' })"
          >Deployment
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right v-if="username">
              <template #button-content>
                <em>{{ username }}</em>
              </template>
              <b-dropdown-item @click="$router.push({ name: 'profile' })"
                >Profile</b-dropdown-item
              >
              <b-dropdown-item @click="logout">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
            <div v-if="!username">
              <b-nav-item
                v-if="$route.name != 'login'"
                @click="$router.push({ name: 'login' })"
                >Login</b-nav-item
              >
            </div>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: mapState({
    username: state => state.userModule.name
  }),
  methods: mapActions("userModule", ["logout"])
};
</script>

<style></style>
