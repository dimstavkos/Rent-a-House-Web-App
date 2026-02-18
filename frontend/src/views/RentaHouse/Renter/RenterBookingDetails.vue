<script setup>
// import { reactive, inject, onMounted } from "vue";
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
// import MaterialButton from "@/components/MaterialButton.vue";

// nav-pills
import setNavPills from "@/assets/js/nav-pills.js";

// const axios = inject("axios");

onMounted(() => {
  setNavPills();
});
</script>
<template>
  <BaseLayout
    title="Booking Details"
    :breadcrumb="[{ label: 'Host' }, { label: 'Properties' },{ label: 'Booking' },{ label: 'Booking Details' }]"
  >
    <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-left py-2">
          <div class="col-12 mx-auto">
    
            <h5>Start Date: {{ $route.params.start_date }} </h5>
            <h5>End Date: {{ $route.params.end_date }} </h5>
            <h5>Number of Nights:   {{ $route.params.total_night_num }}</h5>
            
          </div>
        </div>
      </div>
    </section>
  </BaseLayout>
</template>
