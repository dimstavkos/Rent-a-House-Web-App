<script setup>
// import { reactive, inject, onMounted } from "vue";
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
// import MaterialButton from "@/components/MaterialButton.vue";
import MaterialButton from "@/components/MaterialButton.vue";


// nav-pills
import setNavPills from "@/assets/js/nav-pills.js";

// const axios = inject("axios");

onMounted(() => {
  setNavPills();
});
</script>
<template>
  <BaseLayout
    title="Booking Confirmed"
    :breadcrumb="[{ label: 'User' }, { label: 'Booking Confirmation' }]"
  >
    <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <div class="col-12 mx-auto">
            <h1>Booking Confirmed</h1>
            <h3>Start Date:</h3>
            <h3>End Date: </h3>
            <h3>Total Nights: </h3>
            <h3>Total Price: </h3>
          </div>
          
        </div>
        <!-- <div class="row justify-space-between text-center py-1">
      <div class="col-12 mx-auto text-end">
        <RouterLink :to="{ name: 'search' }">
          <div class="container">
            <MaterialButton
              variant="gradient"
              color="success"
              class="w-auto me-2"
              >Add Property</MaterialButton
            >
          </div>
        </RouterLink>
      </div>
    </div> -->
      </div>
    </section>
  </BaseLayout>
</template>
