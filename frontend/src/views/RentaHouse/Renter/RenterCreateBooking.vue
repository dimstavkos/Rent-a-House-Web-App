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
    
    id: store.id,
    total_night_num: "",
    user_id: "",
    review_id: "",
    booking_updated: "",
    booking_verified: false,
    end_date: "" ,
    start_date: "",
    total_price: "",
    property_id: "" ,
    booking_created: "",
    booking_completed: false,
},
  
  
});

const validateForm = computed(() => {
  try {
    if (
      state.formData.start_date.length > 0 ||
      state.formData.end_date.length > 0
    ) {
      return true;
    } else {
      return false;
    }
  } catch (e) {
    return false;
  }
});

const createBooking = () => {
  const api = "http://localhost:8000/booking/create";

  const json = {
    
    "id": state.formData.id,
    "total_night_num":state.formData.total_night_num ,
    "user_id": state.formData.user_id,
    "review_id": state.formData.review_id,
    "booking_updated": state.formData.booking_updated,
    "booking_verified": state.formData.booking_verified,
    "end_date": state.formData.end_date,
    "start_date": state.formData.start_date,
    "total_price": state.formData.total_price,
    "property_id": state.formData.property_id,
    "booking_created": state.formData.booking_created,
    "booking_completed": state.formData.booking_completed,

  };

  axios
    .patch(api, json)
    .then(() => {
      alert("Booking Created Successfully");
    })
    .catch((e) => {
      alert("Error: " + e.response.data.detail);
    });
};





// const getProperty = () => {
//   let id = ""
//   const api = "http://localhost:8000/property/id/" + id;

//   axios.get(api).then((response) => {
//     state.formData = response.data;
//     state.loaded = true;
  
//   });
// };

onMounted(() => {
  setMaterialInput();
  setNavPills();
  getUser();
});
</script>
<template>
  <BaseLayout
    
    :breadcrumb="[{ label: 'Renter' }, { label: 'Create Booking' }]"
  >
    
    <h3>Confirm Booking Details:</h3>
    <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <form role="form" @submit.prevent="createBooking">
            <div class="card-body">
              <div class="row">
                <div class="col-md-6">
                  <MaterialInput
                    class="input-group-static mb-4"
                    :label="{
                      text: 'Start Date',
                      class: '',
                    }"
                    type="date"
                    v-model="state.start_date"
                  />
                </div>
                <div class="col-md-6 ps-2">
                  <MaterialInput
                    class="input-group-static"
                    :label="{
                      text: 'End Date',
                      class: '',
                    }"
                    type="date"
                    v-model="state.end_date"
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
                
                >Confirm
              </MaterialButton>
            </div>
          </form>
        </div>
      </div>
    </section>
  </BaseLayout>
</template>
