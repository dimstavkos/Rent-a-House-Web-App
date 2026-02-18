<script setup>
import { reactive, inject, onMounted } from "vue";

//Vue Material Kit 2 components
import MaterialAvatar from "@/components/MaterialAvatar.vue";
import MaterialButton from "@/components/MaterialButton.vue";
import MaterialBadge from "@/components/MaterialBadge.vue";

// material-input
import setMaterialInput from "@/assets/js/material-input";

import { useRoute } from "vue-router";

const axios = inject("axios");

const route = useRoute();

const state = reactive({
  user: {},
  loaded: false,
});

const getUser = () => {
  let id = route.params.id;
  const api = "http://localhost:8000/user/id/" + id;

  axios.get(api).then((response) => {
    state.user = response.data;
    state.loaded = true;
  });
};

const activateUser = (u) => {
  const api = "http://localhost:8000/user/patch";

  const json = {
    id: u.id,
    username: u.username,
    password: u.password,
    name: u.name,
    lastname: u.lastname,
    email: u.email,
    phone: u.phone,
    photo: u.photo,
    verified_status: true,
  };

  axios.patch(api, json).then(() => {
    getUser();
  });
};

const deactivateUser = (u) => {
  const api = "http://localhost:8000/user/patch";

  const json = {
    id: u.id,
    username: u.username,
    password: u.password,
    name: u.name,
    lastname: u.lastname,
    email: u.email,
    phone: u.phone,
    photo: u.photo,
    verified_status: false,
  };

  axios.patch(api, json).then(() => {
    getUser();
  });
};

onMounted(() => {
  setMaterialInput();
  getUser();
});
</script>
<template>
  <section class="py-sm-7 py-5 position-relative">
    <div class="container">
      <div class="row">
        <div class="col-12 mx-auto">
          <div class="mt-n8 mt-md-n9 text-center">
            <div class="blur-shadow-avatar">
              <MaterialAvatar
                v-if="state.loaded"
                size="xxl"
                class="shadow-xl position-relative z-index-2"
                :image="state.user.photo"
                alt="loading..."
              />
            </div>
          </div>
          <div class="row py-7">
            <div
              class="col-lg-7 col-md-7 z-index-2 position-relative px-md-2 px-sm-5 mx-auto"
            >
              <div
                class="d-flex justify-content-between align-items-center mb-2"
              >
                <h3 class="mb-0">
                  {{ state.user.lastname }} {{ state.user.name }} (#{{
                    state.user.id
                  }})
                </h3>
                <div class="d-block">
                  <MaterialButton 
                    v-if="state.user.verified_status"
                    @click="deactivateUser(state.user)"
                    class="text-nowrap mb-0"
                    variant="outline"
                    color="danger"
                    size="sm"
                    >Deactivate</MaterialButton
                  >
                  <MaterialButton
                    v-else
                    @click="activateUser(state.user)"
                    class="text-nowrap mb-0"
                    variant="outline"
                    color="success"
                    size="sm"
                    >Activate
                  </MaterialButton>
                </div>
              </div>
              <div class="row mb-4">
                <div class="col-auto">
                  <span class="h6 me-3">Status</span>
                  <MaterialBadge
                    v-if="state.user.verified_status"
                    variant="gradient"
                    color="success"
                  >
                    Verified
                  </MaterialBadge>
                  <MaterialBadge v-else variant="gradient" color="warning">
                    Unverified
                  </MaterialBadge>
                </div>
                <div class="col-auto">
                  <span class="h6 me-3">username</span>
                  <span class="me">{{ state.user.username }}</span>
                </div>
              </div>
              <ul>
                <li>Phone: {{ state.user.phone }}</li>
                <li>Email: {{ state.user.email }}</li>
                <li>Joined: {{ state.user.user_created }}</li>
              </ul>
              <h5>Roles:</h5>
              <ul>
                <li v-for="r in state.user.roles" v-bind:key="r.id">
                  {{ r.role_name }}
                </li>
              </ul>
              <p class="text-lg mb-0">This is an awesome personality!</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
