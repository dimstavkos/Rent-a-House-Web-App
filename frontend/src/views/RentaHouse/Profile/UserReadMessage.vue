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
    title="Message"
    :breadcrumb="[{ label: 'User' }, { label: 'View Message' }]"
  >
    <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <div class="col-12 mx-auto">

            <h5>{{ $route.params.message }} </h5>
          </div>
        </div>
      </div>
    </section>
  </BaseLayout>
</template>
