<script setup>
import { inject, reactive, onMounted, computed } from "vue";
import { useRouter } from "vue-router";

// example coimport { useRouter, useRoute } from 'vue-router'mponents
import DefaultNavbar from "@/examples/navbars/NavbarDefault.vue";
import Header from "@/examples/Header.vue";

//Vue Material Kit 2 components
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialCheckbox from "@/components/MaterialCheckbox.vue";
import MaterialButton from "@/components/MaterialButton.vue";

import setMaterialInput from "@/assets/js/material-input";

const axios = inject("axios");
const router = useRouter();

const state = reactive({
  formData: {
    username: "",
    password: "",
    name: "",
    lastname: "",
    email: "",
    phone: "",
    photo: "",
    host: false,
    renter: true,
  },
  confirm_password: "",
});

const validateForm = computed(() => {
  try {
    if (
      state.formData.username.length > 0 &&
      state.formData.password.length > 0 &&
      state.formData.name.length > 0 &&
      state.formData.lastname.length > 0 &&
      state.formData.email.length > 0 &&
      state.formData.phone.length > 0 && 
      state.formData.password == state.confirm_password
    ) {
      return true;
    } else {
      return false;
    }
  } catch (e) {
    return false;
  }
});

const register = () => {
  const api = "http://localhost:8000/auth/register";

  axios
    .post(api, state.formData)
    .then(() => {
      if (state.formData.host) {
        alert(
          "Account has breen created successfully. You will be notified once your account has been approved"
        );
      } else {
        alert(
          "Account has breen created successfully. Click here to go to login page"
        );
        router.push({ name: "signin-basic" });
      }
    })
    .catch((e) => {
      alert("Error: " + e.response.data.detail);
    });
};

onMounted(() => {
  setMaterialInput();
});
</script>
<template>
  <DefaultNavbar transparent />
  <Header>
    <div
      class="page-header align-items-start min-vh-100"
      :style="{
        backgroundImage:
          'url(https://images.unsplash.com/photo-1497294815431-9365093b7331?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80)',
      }"
      loading="lazy"
    >
      <span class="mask bg-gradient-dark opacity-6"></span>
      <div class="container my-auto">
        <div class="row">
          <div class="col-lg-6 col-md-8 col-12 mx-auto">
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div
                class="card-header p-0 position-relative mt-n4 mx-3 z-index-2"
              >
                <div
                  class="bg-gradient-success shadow-success border-radius-lg py-3 pe-1"
                >
                  <h4
                    class="text-white font-weight-bolder text-center mt-2 mb-0"
                  >
                    Sign up username:
                  </h4>
                </div>
              </div>
              <div class="card-body">
                <div class="container">
                  <div class="row">
                    <div
                      class="mx-auto d-flex justify-content-center flex-column"
                    >
                      <form role="form" @submit.prevent="register">
                        <div class="card-body">
                          <div class="row">
                            <div class="col-md-6">
                              <MaterialInput
                                class="input-group-dynamic mb-4"
                                :label="{
                                  text: 'Username',
                                  class: 'form-label',
                                }"
                                :isRequired="true"
                                v-model="state.formData.username"
                                type="text"
                              />
                            </div>
                            <div class="col-md-6 ps-2">
                              <MaterialInput
                                class="input-group-dynamic"
                                :label="{
                                  text: 'Email Address',
                                  class: 'form-label',
                                }"
                                v-model="state.formData.email"
                                type="email"
                              />
                            </div>
                          </div>

                          <div class="row">
                            <div class="col-md-6">
                              <MaterialInput
                                class="input-group-dynamic mb-4"
                                :label="{
                                  text: 'Password',
                                  class: 'form-label',
                                }"
                                type="password"
                                v-model="state.formData.password"
                              />
                            </div>
                            <div class="col-md-6 ps-2">
                              <MaterialInput
                                class="input-group-dynamic"
                                :label="{
                                  text: 'Confirm password',
                                  class: 'form-label',
                                }"
                                type="password"
                                v-model="state.confirm_password"
                              />
                            </div>
                          </div>

                          <div class="row">
                            <div class="col-md-6">
                              <MaterialInput
                                class="input-group-dynamic mb-4"
                                :label="{
                                  text: 'First Name',
                                  class: 'form-label',
                                }"
                                type="text"
                                v-model="state.formData.name"
                              />
                            </div>
                            <div class="col-md-6 ps-2">
                              <MaterialInput
                                class="input-group-dynamic"
                                :label="{
                                  text: 'Last Name',
                                  class: 'form-label',
                                }"
                                type="text"
                                v-model="state.formData.lastname"
                              />
                            </div>
                          </div>

                          <div class="row">
                            <div class="col-md-6">
                              <MaterialInput
                                class="input-group-dynamic"
                                :label="{
                                  text: 'Phone',
                                  class: 'form-label',
                                }"
                                type="text"
                                v-model="state.formData.phone"
                              />
                            </div>
                            <div class="col-md-6">
                              <MaterialInput
                                class="input-group-dynamic"
                                :label="{
                                  text: 'Photo URI',
                                  class: 'form-label',
                                }"
                                type="text"
                                v-model="state.formData.photo"
                              />
                            </div>
                          </div>

                          <div class="row pt-4 pb-2">
                            <h6>Select desired roles:</h6>
                          </div>

                          <div class="row">
                            <div class="col-md-6">
                              <MaterialCheckbox
                                id="host_checkbox"
                                color="dark"
                                v-model="state.formData.host"
                              >
                                Host
                              </MaterialCheckbox>
                            </div>
                            <div class="col-md-6 ps-2">
                              <MaterialCheckbox
                                id="renter_checkbox"
                                color="dark"
                                v-model="state.formData.renter"
                              >
                                Renter
                              </MaterialCheckbox>
                            </div>
                          </div>
                        </div>
                        <div class="text-center">
                          <MaterialButton
                            class="my-4 mb-2"
                            variant="gradient"
                            color="success"
                            fullWidth
                            :disabled="!validateForm"
                            >Sign up</MaterialButton
                          >
                        </div>
                        <p class="mt-4 text-sm text-center">
                          Have have an account?

                          <RouterLink
                            :to="{ name: 'signin-basic' }"
                            class="text-success text-gradient font-weight-bold"
                          >
                            <span>Sign In</span>
                          </RouterLink>
                        </p>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <footer class="footer position-absolute bottom-2 py-2 w-100">
        <div class="container">
          <div class="row align-items-center justify-content-lg-between">
            <div class="col-12 col-md-6 my-auto">
              <div
                class="copyright text-center text-sm text-white text-lg-start"
              >
                © {{ new Date().getFullYear() }}, made with
                <i class="fa fa-heart" aria-hidden="true"></i> by
                <a
                  href="https://www.creative-tim.com"
                  class="font-weight-bold text-white"
                  target="_blank"
                  >Creative Tim</a
                >
                for a better web.
              </div>
            </div>
            <div class="col-12 col-md-6">
              <ul
                class="nav nav-footer justify-content-center justify-content-lg-end"
              >
                <li class="nav-item">
                  <a
                    href="https://www.creative-tim.com"
                    class="nav-link text-white"
                    target="_blank"
                    >Creative Tim</a
                  >
                </li>
                <li class="nav-item">
                  <a
                    href="https://www.creative-tim.com/presentation"
                    class="nav-link text-white"
                    target="_blank"
                    >About Us</a
                  >
                </li>
                <li class="nav-item">
                  <a
                    href="https://www.creative-tim.com/blog"
                    class="nav-link text-white"
                    target="_blank"
                    >Blog</a
                  >
                </li>
                <li class="nav-item">
                  <a
                    href="https://www.creative-tim.com/license"
                    class="nav-link pe-0 text-white"
                    target="_blank"
                    >License</a
                  >
                </li>
              </ul>
            </div>
          </div>
        </div>
      </footer>
    </div>
  </Header>
</template>
