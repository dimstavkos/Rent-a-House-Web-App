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
  setNavPills();
  setMaterialInput();
});
</script>
<template>
  <BaseLayout title="Edit Booking" :breadcrumb="[{ label: 'Renter' }, { label: 'Edit Booking' }]">
    <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <form role="form" id="contact-form" method="post" autocomplete="off">
            <div class="card-body">
              <div class="row">
                <h4 class="py-2">Search for New Dates</h4>
                <div class="col-md-6">
                  <MaterialInput class="input-group-dynamic mb-4" :label="{ text: '', class: 'form-label' }"
                    type="date" />
                </div>
                <div class="col-md-6">
                  <MaterialInput class="input-group-dynamic mb-4" :label="{ text: '', class: 'form-label' }"
                    type="date" />
                </div>
                

              </div>
            </div>
            <div class="row">
              <div class="ms-auto col-md-3">
                <MaterialButton type="submit" variant="gradient" color="success" fullWidth>Update
                </MaterialButton>
              </div>
            </div>
          </form>
        </div>
      </div>
    </section>

  </BaseLayout>
</template>
