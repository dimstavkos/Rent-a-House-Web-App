<script setup>
import { reactive, inject, onMounted, computed } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import View from "@/layouts/sections/components/SimpleView.vue";
import MaterialPagination from "@/components/MaterialPagination.vue";
import MaterialPaginationItem from "@/components/MaterialPaginationItem.vue";

// Headers page components codes
import { header1Code } from "@/layouts/sections/page-sections/page-headers/components/codes";
import { useAppStore } from "@/stores";


// nav-pills
import setNavPills from "@/assets/js/nav-pills.js";

const axios = inject("axios");
const store = useAppStore();


const headers = ["ID", "Sent To", "Date", "Text", "Action"];

const state = reactive({
  dataset: [],
  current_page: 0,
  total_pages: 0,
  page_size: 15,
});

const getMessages = () => {
  let id = store.id;
  const api = "http://localhost:8000/usermessage/outbox/" + id;

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
  getMessages();
});
</script>
<template>
  <BaseLayout
    title="Outbox"
    :breadcrumb="[{ label: 'User' }, { label: 'Outbox' }]"
  >
    <View title="Messages" :code="header1Code" id="header-1">
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
              <p  class="text-xs font-weight-bold">
                {{ u.send_to_id}} 
              </p>
              
             
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.message_created }}
              </p>
            </td>
            <td>
              <p class="text-xs font-weight-bold">
                {{ u.text }}
              </p>
            </td>
            <td class="align-middle text-center">
              <RouterLink :to="{ name: 'user-readmessage', params: { id: u.id , message: u.text} }" rel="tooltip" title="Read Message"
                data-placement="bottom">
                <i class="material-icons me-2 cursor-pointer" aria-hidden="true">message</i>
              </RouterLink>

              

              
            </td>
          </tr>
        </tbody>
      </table>
    </View>
  </BaseLayout>
</template>
