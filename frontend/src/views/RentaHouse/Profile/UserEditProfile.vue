<script setup>
import { inject, reactive, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import DefaultNavbar from "@/examples/navbars/NavbarDefault.vue";
import Header from "@/examples/Header.vue";
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import { useAppStore } from "@/stores";
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialCheckbox from "@/components/MaterialCheckbox.vue";
import MaterialButton from "@/components/MaterialButton.vue";
import setMaterialInput from "@/assets/js/material-input";
import setNavPills from "@/assets/js/nav-pills.js";

const store = useAppStore();
const axios = inject("axios");

const state = reactive({
  formData: {
    username: "",
    password: "",
    name: "",
    lastname: "",
    email: "",
    phone: "",
    verified_status: false,
    id: 1,
    photo: "",
  },
  password: "",
  confirm_password: "",
});

const validateForm = computed(() => {
  try {
    if (
      state.formData.username.length > 0 ||
      state.formData.name.length > 0 ||
      state.formData.lastname.length > 0 ||
      state.formData.email.length > 0 ||
      state.formData.phone.length > 0
    ) {
      return true;
    } else {
      return false;
    }
  } catch (e) {
    return false;
  }
});

const saveChanges = () => {
  const api = "http://localhost:8000/user/patch";

  const json = {
    "id" : state.formData.id,
    "username": state.formData.username,
    "name": state.formData.name,
    "lastname": state.formData.lastname,
    "email": state.formData.email,
    "phone": state.formData.phone,
    "photo": state.formData.photo
  };

  axios
    .patch(api, json)
    .then(() => {
      alert("Changes saved successfully");
    })
    .catch((e) => {
      alert("Error: " + e.response.data.detail);
    });
};

const updatePassword = () => {
  const api = "http://localhost:8000/user/patch";

  const json = {
    "id" : state.formData.id,
    "password" : state.password,
  };

  axios
    .patch(api, json)
    .then(() => {
      alert("Password updated successfully");
    })
    .catch((e) => {
      alert("Error: " + e.response.data.detail);
    });
};

const getUser = () => {
  let id = store.id;
  const api = "http://localhost:8000/user/id/" + id;

  axios.get(api).then((response) => {
    state.formData = response.data;
    state.loaded = true;
    state.password = state.formData.password;
  });
};

onMounted(() => {
  setMaterialInput();
  setNavPills();
  getUser();
});
</script>
<template>
  <BaseLayout
    title="Edit Profile"
    :breadcrumb="[{ label: 'User' }, { label: 'Edit Profile' }]"
  >
    <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <form role="form" @submit.prevent="saveChanges">
            <div class="card-body">
              <div class="row">
                <div class="col-md-6">
                  <MaterialInput
                    class="input-group-static mb-4"
                    :label="{
                      text: 'Username',
                      class: '',
                    }"
                    :isRequired="true"
                    v-model="state.formData.username"
                    type="text"
                  />
                </div>
                <div class="col-md-6 ps-2">
                  <MaterialInput
                    class="input-group-static"
                    :label="{
                      text: 'Email Address',
                      class: '',
                    }"
                    v-model="state.formData.email"
                    type="email"
                  />
                </div>
              </div>

              <div class="row">
                <div class="col-md-6">
                  <MaterialInput
                    class="input-group-static mb-4"
                    :label="{
                      text: 'First Name',
                      class: '',
                    }"
                    type="text"
                    v-model="state.formData.name"
                  />
                </div>
                <div class="col-md-6 ps-2">
                  <MaterialInput
                    class="input-group-static"
                    :label="{
                      text: 'Last Name',
                      class: '',
                    }"
                    type="text"
                    v-model="state.formData.lastname"
                  />
                </div>
              </div>

              <div class="row">
                <div class="col-md-6">
                  <MaterialInput
                    class="input-group-static"
                    :label="{
                      text: 'Phone',
                      class: '',
                    }"
                    type="text"
                    v-model="state.formData.phone"
                  />
                </div>
                <div class="col-md-6">
                  <MaterialInput
                    class="input-group-static"
                    :label="{
                      text: 'Photo',
                      class: '',
                    }"
                    type="text"
                    v-model="state.formData.photo"
                  />
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
                >Save Changes
              </MaterialButton>
            </div>
          </form>
        </div>
      </div>
    </section>

    <h3>Change your password:</h3>
    <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <form role="form" @submit.prevent="updatePassword">
            <div class="card-body">
              <div class="row">
                <div class="col-md-6">
                  <MaterialInput
                    class="input-group-static mb-4"
                    :label="{
                      text: 'Password',
                      class: '',
                    }"
                    type="password"
                    v-model="state.password"
                  />
                </div>
                <div class="col-md-6 ps-2">
                  <MaterialInput
                    class="input-group-static"
                    :label="{
                      text: 'Confirm password',
                      class: '',
                    }"
                    type="password"
                    v-model="state.confirm_password"
                  />
                </div>
              </div>
            </div>
            <div class="text-center">
              <MaterialButton
                class="my-4 mb-2"
                variant="gradient"
                color="success"
                fullWidth
                :disabled="state.password != state.confirm_password"
                >Change password
              </MaterialButton>
            </div>
          </form>
        </div>
      </div>
    </section>
  </BaseLayout>
</template>
