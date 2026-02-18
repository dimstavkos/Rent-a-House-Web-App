<script setup>
// import { reactive, inject, onMounted } from "vue";
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialButton from "@/components/MaterialButton.vue";
import MaterialTextArea from "@/components/MaterialTextArea.vue";
import MaterialSwitch from "@/components/MaterialSwitch.vue";
import MaterialCheckbox from "@/components/MaterialCheckbox.vue";
import TransparentBlogCard from "@/examples/cards/blogCards/TransparentBlogCard.vue";
import BackgroundBlogCard from "@/examples/cards/blogCards/BackgroundBlogCard.vue";

// nav-pills
import setNavPills from "@/assets/js/nav-pills.js";
import setMaterialInput from "@/assets/js/material-input";

// const axios = inject("axios");

onMounted(() => {
  setMaterialInput();
  setNavPills();
});
</script>
<template>
  <BaseLayout title="Edit Property" :breadcrumb="[{ label: 'Host' }, { label: 'Edit Property' }]">
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
          <div class="col-lg-7 mx-auto d-flex justify-content-center flex-column">
            <form role="form" id="contact-form" method="post" autocomplete="off">
              <div class="card-body">
                <div class="row">
                  <h4 class="py-2">General Information</h4>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic mb-4" :label="{ text: 'Country', class: 'form-label' }"
                      type="text" />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic mb-4" :label="{ text: 'City', class: 'form-label' }"
                      type="text" />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic mb-4" :label="{ text: 'Address', class: 'form-label' }"
                      type="text" />
                  </div>
                  <div class="col-md-6 ps-2">
                    <MaterialInput class="input-group-dynamic" :label="{ text: 'Date', class: 'form-label' }"
                      type="text" />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic" :label="{ text: 'Number of people', class: 'form-label' }"
                      type="number" />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic" :label="{ text: 'Maximum cost', class: 'form-label' }"
                      type="number" />
                  </div>
                </div>
                <div class="row mt-4">
                  <div class="col-md-2">
                    <MaterialCheckbox color="dark">
                      Flat
                    </MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox color="dark">House</MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox color="dark">Villa</MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox color="dark">Cabin</MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox color="dark">Cottage</MaterialCheckbox>
                  </div>
                  <div class="col-md-2">
                    <MaterialCheckbox color="dark">Mansion</MaterialCheckbox>
                  </div>
                </div>
                <div class="row mt-4">
                  <h4 class="py-2">Amenities</h4>
                  <div class="col-md-2">
                    <MaterialSwitch class="mb-4 d-flex align-items-center" id="flexSwitchCheckDefault" checked
                      labelClass="ms-3 mb-0">
                      Wifi
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch class="mb-4 d-flex align-items-center" id="flexSwitchCheckDefault" checked
                      labelClass="ms-3 mb-0">
                      Cooling
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch class="mb-4 d-flex align-items-center" id="flexSwitchCheckDefault" checked
                      labelClass="ms-3 mb-0">
                      Heating
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch class="mb-4 d-flex align-items-center" id="flexSwitchCheckDefault" checked
                      labelClass="ms-3 mb-0">
                      Kitchen
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch class="mb-4 d-flex align-items-center" id="flexSwitchCheckDefault" checked
                      labelClass="ms-3 mb-0">
                      Television
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch class="mb-4 d-flex align-items-center" id="flexSwitchCheckDefault" checked
                      labelClass="ms-3 mb-0">
                      Parking
                    </MaterialSwitch>
                  </div>
                  <div class="col-md-2">
                    <MaterialSwitch class="mb-4 d-flex align-items-center" id="flexSwitchCheckDefault" checked
                      labelClass="ms-3 mb-0">
                      Elevator
                    </MaterialSwitch>
                  </div>

                  <div class="row mt-4">

                    <h4 class="py-2">Rules</h4>
                    <div class="col-md-3">
                      <MaterialCheckbox color="dark">Smoking</MaterialCheckbox>
                    </div>
                    <div class="col-md-3">
                      <MaterialCheckbox color="dark">Pets</MaterialCheckbox>
                    </div>
                    <div class="col-md-3">
                      <MaterialCheckbox color="dark">Parties</MaterialCheckbox>
                    </div>
                  

                  </div>
                  <div class="col-md-6 pt-3">
                      <MaterialInput class="input-group-dynamic mb-4" :label="{ text: 'Minimum Nights', class: 'form-label' }"
                        type="number" />
                    </div>
                  <h4>Indoor Space</h4>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic mb-4" :label="{ text: 'Bedrooms', class: 'form-label' }"
                      type="text" />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic mb-4" :label="{ text: 'Bathrooms', class: 'form-label' }"
                      type="text" />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic mb-4" :label="{ text: 'Beds', class: 'form-label' }"
                      type="text" />
                  </div>
                  <div class="col-md-6">
                    <MaterialInput class="input-group-dynamic mb-4" :label="{ text: 'Total Space', class: 'form-label' }"
                      type="text" />
                    </div>
                    <div class="col-md-12">
                    <MaterialTextArea class="input-group-static mb-4 py-2" id="message" :rows="4">Description
                    </MaterialTextArea>
                  </div>
                  <div class="row">
                    <div class="ms-auto col-md-3">
                      <MaterialButton type="submit" variant="gradient" color="success" fullWidth>Save Changes
                      </MaterialButton>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>


  </BaseLayout>
</template>
