<script setup>
import { reactive, inject, onMounted, computed } from "vue";
import { RouterLink } from "vue-router";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import View from "@/layouts/sections/components/SimpleView.vue";
import MaterialPagination from "@/components/MaterialPagination.vue";
import MaterialPaginationItem from "@/components/MaterialPaginationItem.vue";

// Headers page components codes
import { header1Code } from "@/layouts/sections/page-sections/page-headers/components/codes";

// nav-pills
import setNavPills from "@/assets/js/nav-pills.js";

const axios = inject("axios");

const headers = [
  "ID",
  "Username",
  "Lastname",
  "Name",
  "Email",
  "Verified status",
  "Created At",
  "Action",
];

const state = reactive({
  users: [],
  current_page: 0,
  total_pages: 0,
  page_size: 15,
});

const getUsers = () => {
  const api = "http://localhost:8000/user/list";

  axios.get(api).then((response) => {
    state.users = response.data;
    state.total_pages = Math.ceil(state.users.length / state.page_size);
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
    getUsers();
  });
};

const filteredUsers = computed(() => {
  try {
    return state.users.slice(
      state.current_page * state.page_size,
      state.current_page * state.page_size + state.page_size
    );
  } catch (e) {
    return [];
  }
});

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
    getUsers();
  });
};

const nextPage = () => {
  if (state.current_page < state.total_pages - 1) {
    state.current_page++;
    console.log(
      "current page is: " +
        state.current_page +
        " if total pages: " +
        state.total_pages
    );
  }
};

const previousPage = () => {
  if (state.current_page > 0) {
    state.current_page--;
  }
  console.log(
    "current page is: " +
      state.current_page +
      " if total pages: " +
      state.total_pages
  );
};

const gotoPage = (x) => {
  if (x >= 0 && x < state.total_pages) {
    state.current_page = x;
  }
  console.log(
    "current page is: " +
      state.current_page +
      " if total pages: " +
      state.total_pages
  );
};

// hook
onMounted(() => {
  setNavPills();
  getUsers();
});
</script>
<template>
  <BaseLayout
    title="Manage users"
    :breadcrumb="[{ label: 'Administrator' }, { label: 'Manage users' }]"
  >
    <View title="Users" :code="header1Code" id="header-1">
      <div class="row">
        <div class="col-lg-4 mx-auto">
          <MaterialPagination :style="{ marginLeft: '80px' }">
            <MaterialPaginationItem
              v-if="state.total_pages > 1"
              @click="previousPage"
              prev
            />
            <MaterialPaginationItem
              v-for="i in state.total_pages"
              v-bind:key="i"
              :label="String(i)"
              @click="gotoPage(i - 1)"
              :active="state.current_page == i - 1"
            />
            <MaterialPaginationItem
              v-if="state.total_pages > 1"
              @click="nextPage"
              next
            />
          </MaterialPagination>
        </div>
      </div>

      <table class="table align-items-center mb-0">
        <thead>
          <tr>
            <th
              v-for="(header, index) in headers"
              :key="header"
              class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
              :class="{
                'ps-2': index == 1,
                'text-center': index > 1,
              }"
            >
              {{ header }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="u in filteredUsers" :key="u.id">
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.id }}
              </p>
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.username }}
              </p>
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.lastname }}
              </p>
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.name }}
              </p>
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.email }}
              </p>
            </td>
            <td class="align-middle text-center text-sm">
              {{ u.verified_status }}
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.user_created }}
              </p>
            </td>

            <td class="align-middle text-center">
              <RouterLink
                :to="{ name: 'manage-userprofile', params: { id: u.id } }"
                rel="tooltip"
                title="Details"
                data-placement="bottom"
              >
                <i class="material-icons me-2 cursor-pointer" aria-hidden="true"
                  >details</i
                >
              </RouterLink>

              <i
                v-if="!u.verified_status"
                @click="activateUser(u)"
                class="material-icons me-2 cursor-pointer"
                aria-hidden="true"
                >bolt</i
              >

              <i
                v-if="u.verified_status"
                @click="deactivateUser(u)"
                class="material-icons me-2 cursor-pointer"
                aria-hidden="true"
                >flash_off</i
              >
            </td>
          </tr>
        </tbody>
      </table>
    </View>
  </BaseLayout>
</template>
