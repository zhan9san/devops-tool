<template>
  <div>
    <b-row>
      <b-col md="8" offset-md="2" lg="6" offset-lg="3">
        <b-card class="mt-5" header="Login">
          <b-form
            @submit.prevent="onSubmit"
            @reset.prevent="onReset"
            v-if="show"
          >
            <b-form-group>
              <b-form-input
                v-model="username"
                type="text"
                placeholder="Enter username"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group>
              <b-form-input
                v-model="password"
                type="password"
                placeholder="Enter password"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-group>
              <b-button type="submit" variant="primary">Login</b-button>
              <b-button type="reset" variant="danger">Reset</b-button>
            </b-form-group>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: "",
      errmsg: "",
      errshow: false,
      show: true
    };
  },
  methods: {
    ...mapActions("userModule", { userLogin: "login" }),
    onSubmit() {
      this.userLogin({
        username: this.username,
        password: this.password
      }).then(() => {
        this.$router.push({ name: "Home" });
      });
    },
    onReset() {
      // Reset our form values
      this.username = "";
      this.password = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
