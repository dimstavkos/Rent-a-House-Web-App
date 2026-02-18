<script setup>
import { inject, reactive, onMounted, computed } from "vue";

import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import TransparentBlogCard from "@/examples/cards/blogCards/TransparentBlogCard.vue";

import post1 from "@/assets/img/examples/testimonial-6-2.jpg";
import { useAppStore } from "@/stores";
import setNavPills from "@/assets/js/nav-pills.js";
import setMaterialInput from "@/assets/js/material-input";

const store = useAppStore();

const axios = inject("axios");

const state = reactive({
  rooms: [],
});

const getRecommendations = () => {
  let id = store.id;
  const api = "http://localhost:8000/property/recommend/" + id;

  axios
    .get(api)
    .then((response) => {
      state.rooms = response.data;
    })
    .catch((e) => {
      alert("Error: " + e.response.data);
    });
};

onMounted(() => {
  getRecommendations();
  setMaterialInput();
  setNavPills();
});
</script>
<template>
  <BaseLayout title="Recommendations" :breadcrumb="[{ label: 'Properties' }, { label: 'Recommended' }]">
    <section class="py-3">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <h5 class="mb-5">Top matches</h5>
          </div>
        </div>
        <div class="row">
          <div v-for="r in state.rooms" v-bind:key="r.id" class="col-lg-3 col-sm-6">
            <TransparentBlogCard :image="r.photos[0].photo" :title="r.location.country + '-' + r.location.city"
              :description="'Property Type: ' +
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
    route: '/host/propertypage/' + r.id,
    color: 'success',
    params: {id:r.id}

  }">
              <h6>{{ r.location.address }}</h6>
            </TransparentBlogCard>
          </div>
        </div>
      </div>
    </section>
  </BaseLayout>
</template>
