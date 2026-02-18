<script setup>
import { inject, reactive, onMounted, computed } from "vue";

import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialButton from "@/components/MaterialButton.vue";
import MaterialSwitch from "@/components/MaterialSwitch.vue";
import MaterialCheckbox from "@/components/MaterialCheckbox.vue";
import MaterialSelect from "@/components/MaterialSelect.vue";
import TransparentBlogCard from "@/examples/cards/blogCards/TransparentBlogCard.vue";
import setNavPills from "@/assets/js/nav-pills.js";
import setMaterialInput from "@/assets/js/material-input";
import MaterialPagination from "@/components/MaterialPagination.vue";
import MaterialPaginationItem from "@/components/MaterialPaginationItem.vue";

const axios = inject("axios");

const state = reactive({
  formData: {
    country: null,
    city: null,
    location: null,
    number_of_guests: "1",
    max_cost: "1000",
    is_flat: null,
    is_house: null,
    is_villa: null,
    is_cabin: null,
    is_cottage: null,
    is_manson: null,
    has_wifi: null,
    has_airconditioning: null, // cooling
    has_heat: null,
    has_kitchen: null,
    has_tv: null,
    has_parking: null,
    has_elevator: null,
    date_from: null,
    date_to: null,
  },
  countries: [],
  MediaCapabilities: [],
  rooms: [],
  current_page: 0,
  total_pages: 0,
  page_size: 10,
});

const validateForm = computed(() => {
  try {
    if (
      state.formData.date_from != null &&
      state.formData.date_from.length > 0 &&
      state.formData.date_to != null &&
      state.formData.date_to.length > 0 &&
      state.formData.number_of_guests != null &&
      state.formData.number_of_guests.length > 0
    ) {
      return true;
    } else {
      return false;
    }
  } catch (e) {
    return false;
  }
});

function getValue(x) {
  if (x == null || x == "") {
    return null;
  }
  return x;
}

const getCountries = () => {
  const api = "http://localhost:8000/location/countries";

  axios
    .get(api)
    .then((response) => {
      state.countries = response.data;
      state.formData.country = state.countries[0];
    })
    .catch((e) => {
      alert("Error: " + e.response.data);
    });
};

const getCities = () => {
  const api = "http://localhost:8000/location/cities";

  axios
    .get(api)
    .then((response) => {
      state.cities = response.data;
      state.formData.city = state.cities[0];
    })
    .catch((e) => {
      alert("Error: " + e.response.data);
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

const search = () => {
  const api = "http://localhost:8000/property/search";

  let payload = {
    country: state.formData.country,
    city: state.formData.city,
    location: state.formData.location,
    date: state.formData.date,
    number_of_guests: state.formData.number_of_guests,
    max_cost: state.max_cost ?? null,
    is_flat: getValue(state.formData.is_flat),
    is_house: getValue(state.formData.is_house),
    is_villa: getValue(state.formData.is_villa),
    is_cabin: getValue(state.formData.is_cabin),
    is_cottage: getValue(state.formData.is_cottage),
    is_manson: getValue(state.formData.is_manson),
    has_wifi: getValue(state.formData.has_wifi),
    has_airconditioning: getValue(state.formData.has_airconditioning), // cooling
    has_heat: getValue(state.formData.has_heat),
    has_kitchen: getValue(state.formData.has_kitchen),
    has_tv: getValue(state.formData.has_tv),
    has_parking: getValue(state.formData.has_parking),
    has_elevator: getValue(state.formData.has_elevator),
  };

  axios
    .post(api, payload)
    .then((response) => {
      state.rooms = response.data;
      state.total_pages = Math.ceil(state.rooms.length / state.page_size);
    })
    .catch((e) => {
      alert("Error: " + e.response.data);
    });
};

const filteredRooms = computed(() => {
  try {
    return state.rooms.slice(
      state.current_page * state.page_size,
      state.current_page * state.page_size + state.page_size
    );
  } catch (e) {
    return [];
  }
});

onMounted(() => {
  getCountries();
  getCities();
  setMaterialInput();
  setNavPills();

  var currentDate = new Date();
  var currentDateWithFormat = currentDate.toJSON().slice(0, 10);

  state.formData.date_from = currentDateWithFormat;

  var toDate = new Date(currentDate);
  toDate.setDate(toDate.getDate() + 3);

  currentDateWithFormat = toDate.toJSON().slice(0, 10);

  state.formData.date_to = currentDateWithFormat;
});
</script>
<template>
  <BaseLayout
    title="Search for properties"
    :breadcrumb="[{ label: 'Properties' }, { label: 'Search' }]"
  >
    <!-- <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <div class="col-12 mx-auto"></div>
        </div>
      </div>
    </section> -->

    <section>
      <div class="py-3 bg-gray-100">
        <div class="row">
          <div
            class="col-lg-7 mx-auto d-flex justify-content-center flex-column"
          >
            <form role="form" class="text-start" @submit.prevent="search">
              <div class="card-body">
                <div class="row">
                  <div class="col-md-6">
                    <label>Country:</label>
                    <MaterialSelect
                      id="Country"
                      class="input-group-dynamic mb-4"
                      v-model="state.formData.country"
                      :validValues="state.countries"
                    />
                  </div>
                  <div class="col-md-6 ps-2">
                    <label>City:</label>
                    <MaterialSelect
                      id="City"
                      class="input-group-dynamic mb-4"
                      v-model="state.formData.city"
                      :validValues="state.cities"
                    />
                  </div>
                  <div class="col-md-12 ps-2">
                    <MaterialInput
                      id="location"
                      class="input-group-static mb-4"
                      :label="{ text: 'Address', class: '' }"
                      v-model="state.formData.location"
                      type="text"
                      :isRequired="true"
                    />
                  </div>
                  <div class="col-md-6 ps-2 mb-4">
                    <MaterialInput
                      id="date"
                      class="input-group-static"
                      :label="{ text: 'Date from:*', class: '' }"
                      v-model="state.formData.date_from"
                      :isRequired="true"
                    />
                  </div>
                  <div class="col-md-6 ps-2 mb-4">
                    <MaterialInput
                      id="date"
                      class="input-group-static"
                      :label="{ text: 'Date to:*', class: '' }"
                      v-model="state.formData.date_to"
                      :isRequired="true"
                    />
                  </div>
                  <div class="col-md-6 mb-4">
                    <MaterialInput
                      id="number_of_guests"
                      class="input-group-static"
                      :label="{
                        text: 'Number of people *',
                        class: '',
                      }"
                      type="number"
                      v-model="state.formData.number_of_guests"
                      :isRequired="true"
                    />
                  </div>
                  <div class="col-md-6 mb-4">
                    <MaterialInput
                      id="maximum_cost"
                      class="input-group-static"
                      :label="{ text: 'Maximum cost', class: '' }"
                      type="number"
                      v-model="state.formData.max_cost"
                    />
                  </div>
                </div>
                <div class="row mt-4">
                  <div class="col-md-2">
                    <MaterialCheckbox
                      id="flat"
                      color="dark"
                      v-model="state.formData.is_flat"
                    >
                      Flat
                    </MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox
                      id="house"
                      color="dark"
                      v-model="state.formData.is_house"
                    >
                      House
                    </MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox
                      id="villa"
                      color="dark"
                      v-model="state.formData.is_villa"
                    >
                      Villa
                    </MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox
                      id="cabin"
                      color="dark"
                      v-model="state.formData.is_cabin"
                    >
                      Cabin
                    </MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox
                      id="cottage"
                      color="dark"
                      v-model="state.formData.is_cottage"
                    >
                      Cottage
                    </MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox
                      id="manson"
                      color="dark"
                      v-model="state.formData.is_manson"
                    >
                      Mansion
                    </MaterialCheckbox>
                  </div>
                </div>
                <div class="row mt-4">
                  <div class="col-md-2">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      id="wifi"
                      labelClass="ms-3 mb-0"
                      v-model="state.formData.has_wifi"
                    >
                      Wifi
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      id="cooling"
                      labelClass="ms-3 mb-0"
                      v-model="state.formData.has_airconditioning"
                    >
                      Cooling
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      id="heating"
                      labelClass="ms-3 mb-0"
                      v-model="state.formData.has_heat"
                    >
                      Heating
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      id="kitchen"
                      labelClass="ms-3 mb-0"
                      v-model="state.formData.has_kitchen"
                    >
                      Kitchen
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      id="television"
                      labelClass="ms-3 mb-0"
                      v-model="state.formData.has_tv"
                    >
                      Television
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      id="parking"
                      labelClass="ms-3 mb-0"
                      v-model="state.formData.has_parking"
                    >
                      Parking
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      id="flexSwitchCheckDefault"
                      labelClass="ms-3 mb-0"
                      v-model="state.formData.has_elevator"
                    >
                      elevator
                    </MaterialSwitch>
                  </div>
                  <div class="row">
                    <div class="ms-auto col-md-3">
                      <MaterialButton
                        type="submit"
                        variant="gradient"
                        color="success"
                        fullWidth
                        :disabled="!validateForm"
                        >Search</MaterialButton
                      >
                    </div>
                  </div>
                </div>
              </div>
            </form>
            <!-- <pre>
              {{ state.formData }}
            </pre> -->
          </div>
        </div>
      </div>
    </section>
    <section class="py-3">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <h5 class="mb-5">Search results</h5>
          </div>
        </div>
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
        <div class="row">
          <div
            v-for="r in filteredRooms"
            v-bind:key="r.id"
            class="col-lg-3 col-sm-6"
          >
            <TransparentBlogCard
              :image="r.photos[0].photo"
              :title="r.location.country + '-' + r.location.city"
              :description="
                'Property Type: ' +
                r.indoorspace.property_type.property_type_name +
                '<br>' +
                'Cost Per Night: ' +
                r.price +
                '<br>' +
                'Guests: ' +
                r.number_of_guests +
                '<br>' +
                'Beds: ' +
                r.indoorspace.bed_num
              "
              :action="{
                label: 'Read more',
                route: '/host/propertypage/' + r.id + '?from=' + state.formData.date_from + '&to=' + state.formData.date_to,
                color: 'success',
              }"
            >
              <h6>{{ r.location.address }}</h6>
              <div v-for="(r, index) in r.review_score" v-bind:key="index">
                <span v-for="i in r.stars" v-bind:key="i"> ★ </span><br>
                Review Score: {{ r.rating }} ({{ r.total_ratings }} reviews) <br>
              </div>
            </TransparentBlogCard>
          </div>
        </div>
      </div>
    </section>
  </BaseLayout>
</template>
