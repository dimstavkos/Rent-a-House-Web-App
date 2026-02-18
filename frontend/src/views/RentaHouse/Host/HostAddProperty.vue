<script setup>
// import { reactive, inject, onMounted } from "vue";
import { onMounted, reactive, inject } from "vue";

import MaterialSelect from "@/components/MaterialSelect.vue";
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialButton from "@/components/MaterialButton.vue";
import MaterialTextArea from "@/components/MaterialTextArea.vue";
import MaterialSwitch from "@/components/MaterialSwitch.vue";
import MaterialCheckbox from "@/components/MaterialCheckbox.vue";
import setNavPills from "@/assets/js/nav-pills.js";
import setMaterialInput from "@/assets/js/material-input";
import { useAppStore } from "@/stores";

const axios = inject("axios");
const store = useAppStore();

const state = reactive({
  locationData: {
    country: "Greece",
    city: "Athens",
    address: "",
    latitude: "",
    longitude: "",
  },
  indoorSpaceData: {
    bedroom_num: 2,
    bath_num: 1,
    bed_num: 1,
    total_space: 50,
    description: "",
    has_livingroom: true,
    property_type_id: 1,
  },
  propertyData: {
    // ids:
    user_id: store.id,
    indoor_space_id: undefined,
    location_id: undefined,
    // fields:
    has_airconditioning: true,
    has_kitchen: true,
    has_parking: false,
    is_available: true,
    description: "",
    number_of_guests: "3",
    price: 100,
    has_wifi: true,
    has_heat: false,
    has_tv: true,
    has_elevator: false,
    floor: 0,
  },
  propertyRules:{
    party_allowed: true,
    property_id: 1,
    min_night_number: 16,
    smoking_allowed: true,
    pet_allowed: true
  },
  propertyPhoto:{
    photo: "https://picsum.photos/seed/pay/410/225",
    property_id: 9,
    
  },
  property_types: [],
});

const createProperty = async () => {
  const apiLocation = "http://localhost:8000/location/create";
  const apiIndoorSpace = "http://localhost:8000/indoorspace/create";
  const apiProperty = "http://localhost:8000/property/create";
  const apiRuleList = "http://localhost:8000/propertyrulelist/create";
  const apiPhoto = "http://localhost:8000/photo/create";

  let response = undefined;

  response = await axios.post(apiLocation, state.locationData);
  const location_id = response.data.id;

  response = await axios.post(apiIndoorSpace, state.indoorSpaceData);
  const indoor_space_id = response.data.id;

  state.propertyData.location_id = location_id;
  state.propertyData.indoor_space_id = indoor_space_id;

  response = await axios.post(apiProperty, state.propertyData);
  const property_id = response.data.id;

  state.propertyRules.property_id = property_id;

  response = await axios.post(apiRuleList, state.propertyRules);
  const ruleList_id = response.data.id;

  state.propertyPhoto.property_id = property_id;

  response = await axios.post(apiPhoto, state.propertyPhoto);
  const photo_id = response.data.id;


  alert(location_id + "," + indoor_space_id + "," + property_id + "," + ruleList_id + "," + photo_id);
};

const getPropertyTypes = () => {
  const api = "http://localhost:8000/propertytype/list";

  axios
    .get(api)
    .then((response) => {
      state.property_types = response.data;
    })
    .catch((e) => {
      alert("Error: " + e.response.data);
    });
};

onMounted(() => {
  setMaterialInput();
  setNavPills();
  getPropertyTypes();
});
</script>
<template>
  <BaseLayout
    title="Add Property"
    :breadcrumb="[{ label: 'Host' }, { label: 'Add Property' }]"
  >
    <!-- <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <div class="col-12 mx-auto"></div>
        </div>
      </div>
    </section> -->

    <form role="form" id="add-property-form" method="post" autocomplete="off">
      <section>
        <div class="py-3 bg-gray-100">
          <div class="row">
            <div
              class="col-lg-7 mx-auto d-flex justify-content-center flex-column"
            >
              <div class="card-body">
                <div class="row">
                  <h4 class="py-2">Location</h4>
                  <div class="col-md-4">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Country', class: '' }"
                      type="text"
                      v-model="state.locationData.country"
                    />
                  </div>
                  <div class="col-md-4">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'City', class: '' }"
                      type="text"
                      v-model="state.locationData.city"
                    />
                  </div>
                  <div class="col-md-4">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Address', class: '' }"
                      type="text"
                      v-model="state.locationData.address"
                    />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Latitude', class: '' }"
                      type="text"
                      v-model="state.locationData.latitude"
                    />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Longitude', class: '' }"
                      type="text"
                      v-model="state.locationData.longitude"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section>
        <div class="py-3 bg-gray-100">
          <div class="row">
            <div
              class="col-lg-7 mx-auto d-flex justify-content-center flex-column"
            >
              <div class="card-body">
                <div class="row">
                  <h4 class="py-2">Property Indoor Space</h4>
                  <div class="row">
                    <div class="col-md-12">
                      <div class="col-md-12">
                        <label>Property type:</label>
                        <MaterialSelect
                          class="input-group-dynamic mb-4"
                          v-model="state.indoorSpaceData.property_type_id"
                          :validValues="state.property_types"
                          title="property_type_name"
                        />
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Bedrooms', class: '' }"
                      type="text"
                      v-model="state.indoorSpaceData.bedroom_num"
                    />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Bathrooms', class: '' }"
                      type="text"
                      v-model="state.indoorSpaceData.bath_num"
                    />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Beds', class: '' }"
                      type="text"
                      v-model="state.indoorSpaceData.bed_num"
                    />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Total Space', class: '' }"
                      type="text"
                      v-model="state.indoorSpaceData.total_space"
                    />
                  </div>
                  <div class="col-md-12">
                    <MaterialTextArea
                      class="input-group-static mb-4 py-2"
                      id="message"
                      :rows="4"
                      v-model="state.indoorSpaceData.description"
                      >Description
                    </MaterialTextArea>
                  </div>

                  <div class="col-md-12">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      id="flexSwitchCheckDefault"
                      labelClass="ms-3 mb-0"
                      v-model="state.indoorSpaceData.has_livingroom"
                    >
                      Living Room
                    </MaterialSwitch>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section>
        <div class="py-3 bg-gray-100">
          <div class="row">
            <div
              class="col-lg-7 mx-auto d-flex justify-content-center flex-column"
            >
              <div class="card-body">
                <div class="row">
                  <h4 class="py-2">Property General Information</h4>

                  <div class="col-md-4 ps-2">
                    <MaterialInput
                      class="input-group-static"
                      :label="{ text: 'Floor', class: '' }"
                      type="number"
                      v-model="state.propertyData.floor"
                    />
                  </div>
                  <div class="col-md-4">
                    <MaterialInput
                      class="input-group-static"
                      :label="{ text: 'Number of guests', class: '' }"
                      type="number"
                      v-model="state.propertyData.number_of_guests"
                    />
                  </div>
                  <div class="col-md-4">
                    <MaterialInput
                      class="input-group-static"
                      :label="{ text: 'Price per Night', class: '' }"
                      type="number"
                      v-model="state.propertyData.price"
                    />
                  </div>
                  <div class="row">
                    <div class="col-md-12">
                      <MaterialTextArea
                        class="input-group-static mb-4 py-2"
                        id="message"
                        :rows="2"
                        v-model="state.propertyData.description"
                        >Description
                      </MaterialTextArea>
                    </div>
                  </div>

                  <div class="row">
                    <div class="col-md-3">
                      <MaterialSwitch
                        class="mb-4 d-flex align-items-center"
                        id="flexSwitchCheckDefault"
                        labelClass="ms-3 mb-0"
                        v-model="state.propertyData.has_wifi"
                      >
                        Wifi
                      </MaterialSwitch>
                    </div>
                    <div class="col-md-3">
                      <MaterialSwitch
                        class="mb-4 d-flex align-items-center"
                        id="flexSwitchCheckDefault"
                        labelClass="ms-3 mb-0"
                        v-model="state.propertyData.has_airconditioning"
                      >
                        Cooling
                      </MaterialSwitch>
                    </div>
                    <div class="col-md-3">
                      <MaterialSwitch
                        class="mb-4 d-flex align-items-center"
                        id="flexSwitchCheckDefault"
                        labelClass="ms-3 mb-0"
                        v-model="state.propertyData.has_heat"
                      >
                        Heating
                      </MaterialSwitch>
                    </div>
                    <div class="col-md-3">
                      <MaterialSwitch
                        class="mb-4 d-flex align-items-center"
                        id="flexSwitchCheckDefault"
                        labelClass="ms-3 mb-0"
                        v-model="state.propertyData.has_kitchen"
                      >
                        Kitchen
                      </MaterialSwitch>
                    </div>
                    <div class="col-md-3">
                      <MaterialSwitch
                        class="mb-4 d-flex align-items-center"
                        id="flexSwitchCheckDefault"
                        labelClass="ms-3 mb-0"
                        v-model="state.propertyData.has_tv"
                      >
                        Television
                      </MaterialSwitch>
                    </div>
                    <div class="col-md-3">
                      <MaterialSwitch
                        class="mb-4 d-flex align-items-center"
                        id="flexSwitchCheckDefault"
                        labelClass="ms-3 mb-0"
                        v-model="state.propertyData.has_parking"
                      >
                        Parking
                      </MaterialSwitch>
                    </div>
                    <div class="col-md-3">
                      <MaterialSwitch
                        class="mb-4 d-flex align-items-center"
                        id="flexSwitchCheckDefault"
                        labelClass="ms-3 mb-0"
                        v-model="state.propertyData.has_elevator"
                      >
                        Elevator
                      </MaterialSwitch>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      labelClass="ms-3 mb-0"
                      v-model="state.propertyData.is_available"
                    >
                      Initially available
                    </MaterialSwitch>
                  </div>
                </div>
              </div>
              
            </div>
          </div>
        </div>
      </section>

      <section>
        <div class="py-3 bg-gray-100">
          <div class="row">
            <div
              class="col-lg-7 mx-auto d-flex justify-content-center flex-column"
            >
              <div class="card-body">
                <div class="row">
                  <h4 class="py-2">Property Rules</h4>
                  
                  <div class="col-md-4">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      labelClass="ms-3 mb-0"
                      v-model="state.propertyRules.smoking_allowed"
                    >
                      Smoking
                    </MaterialSwitch>
                  </div>
                

                
                  <div class="col-md-4">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      labelClass="ms-3 mb-0"
                      v-model="state.propertyRules.pet_allowed"
                    >
                      Pets
                    </MaterialSwitch>
                  </div>
               

                
                  <div class="col-md-4">
                    <MaterialSwitch
                      class="mb-4 d-flex align-items-center"
                      labelClass="ms-3 mb-0"
                      v-model="state.propertyRules.party_allowed"
                    >
                      Parties
                    </MaterialSwitch>
                  </div>
               

                  <div class="col-md-6 pt-3 px-5">
                    <MaterialInput
                      class="input-group-static mb-4"
                      :label="{ text: 'Minimum Nights', class: '' }"
                      type="number"
                      v-model="state.propertyRules.min_night_number"
                    />
                  </div>
                </div>
              </div>
              <div class="ms-auto col-md-3">
                <MaterialButton
                  type="submit"
                  variant="gradient"
                  color="success"
                  fullWidth
                  @click.prevent="createProperty"
                  >Add property
                </MaterialButton>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- <section>
        <div class="py-3 bg-gray-100">
          <div class="row">
            <div
              class="col-lg-7 mx-auto d-flex justify-content-center flex-column"
            >
              <div class="card-body">
                <div class="row">
                  <h4 class="py-2">Property Dates</h4>

                  <div class="col-md-6 ps-2">
                    <MaterialInput
                      class="input-group-static"
                      :label="{ text: 'Start Date', class: '' }"
                      type="dtext"
                    />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput
                      class="input-group-static"
                      :label="{ text: 'End Date', class: '' }"
                      type="text"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section> -->
    </form>
  </BaseLayout>
</template>
