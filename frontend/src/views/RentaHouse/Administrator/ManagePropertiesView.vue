<script setup>
import { reactive, inject, onMounted, computed } from "vue";

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

const headers = ["ID", "Description", "Price", "is_available", "Action"];

const state = reactive({
  dataset: [],
  current_page: 0,
  total_pages: 0,
  page_size: 15,
});

const getProperties = () => {
  const api = "http://localhost:8000/property/list";

  axios.get(api).then((response) => {
    state.dataset = response.data;
    state.total_pages = Math.ceil(state.dataset.length / state.page_size);
  });
};

const filteredDataset = computed(() => {
  try {
    return state.dataset.slice(
      state.current_page * state.page_size,
      state.current_page * state.page_size + state.page_size
    );
  } catch (e) {
    return [];
  }
});

const nextPage = () => {
  if (state.current_page < state.total_pages - 1) {
    state.current_page++;
  }
};

const previousPage = () => {
  if (state.current_page > 0) {
    state.current_page--;
  }
};

const gotoPage = (x) => {
  if (x >= 0 && x < state.total_pages) {
    state.current_page = x;
  }
};

// hook
onMounted(() => {
  setNavPills();
  getProperties();
});
</script>
<template>
  <BaseLayout
    title="Manage properties"
    :breadcrumb="[{ label: 'Administrator' }, { label: 'Manage properties' }]"
  >
    <View title="Properties" :code="header1Code" id="header-1">
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

      <table class="table align-items-center text-center mb-0">
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
          <tr v-for="u in filteredDataset" :key="u.id">
            <td>
              <p class="text-center text-xs font-weight-bold">
                {{ u.id }}
              </p>
            </td>
            <td>
              <p v-if="u.description.length > 120" class="text-xs font-weight-bold">
                {{ u.description.substr(0,100) }} ...
              </p>
              <p v-else="u.description.length > 120" class="text-xs font-weight-bold">
                {{ u.description }}
              </p>
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.price }}
              </p>
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.is_available }}
              </p>
            </td>
            <td class="align-middle text-center">
              <RouterLink :to="{ name: 'host-propertypage', params: { id: u.id } }" rel="tooltip" title="View Profile"
                data-placement="bottom">
                <i class="material-icons me-2 cursor-pointer" aria-hidden="true">details</i>
              </RouterLink>
            </td>
          </tr>
        </tbody>
      </table>
    </View>
  </BaseLayout>
</template>
