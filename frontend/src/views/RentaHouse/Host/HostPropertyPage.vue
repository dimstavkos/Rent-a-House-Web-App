<script setup>
// import { reactive, inject, onMounted } from "vue";
import { onMounted, inject, reactive } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import DefaultInfoCard from "@/examples/cards/infoCards/DefaultInfoCard.vue";
import CenteredBlogCard from "@/examples/cards/blogCards/CenteredBlogCard.vue";
import DefaultReviewCard from "@/examples/cards/reviewCards/DefaultReviewCard.vue";
import MaterialTextArea from "@/components/MaterialTextArea.vue";
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialButton from "@/components/MaterialButton.vue";
import team2 from "@/assets/img/team-2.jpg";
import bgContact from "@/assets/img/examples/blog2.jpg";
import { useAppStore } from "@/stores";

// import MaterialButton from "@/components/MaterialButton.vue";

// nav-pills
import setNavPills from "@/assets/js/nav-pills.js";
import { useRoute } from "vue-router";
import { Button } from "bootstrap";

const store = useAppStore();
const axios = inject("axios");
const route = useRoute();

const state = reactive({
  dataset: {
    location: {
      address: "",
      country: "",
      city: "",
      id: undefined,
    },
    indoorspace: {
      bed_num: undefined,
      bath_num: undefined,
      has_livingroom: undefined,
      description: undefined,
      id: undefined,
      bedroom_num: undefined,
      total_space: undefined,
      property_type_id: undefined,
      property_type: {
        id: undefined,
        property_type_name: "",
      },
    },
    photos: [
      {
        photo: "",
        property_id: undefined,
        id: undefined,
      },
    ],
    rules: [
      {
        pet_allowed: undefined,
        min_night_number: undefined,
        smoking_allowed: undefined,
        party_allowed: undefined,
        id: undefined,
        property_id: undefined,
      },
    ],
    availableDates: [],
    booking: [
      {
        total_night_num: undefined,
        id: undefined,
        user_id: undefined,
        review_id: undefined,
        booking_updated: undefined,
        booking_verified: undefined,
        end_date: undefined,
        start_date: undefined,
        total_price: undefined,
        property_id: undefined,
        booking_created: undefined,
        booking_completed: undefined,
        review: {
          rating: 0,
          id: undefined,
          comment: "",
        },
      },
    ],
    owner: {
      id: undefined,
      username: "",
      lastname: "",
      phone: "",
      name: "",
      email: "",
      user_created: undefined,
      roles: [],
    },
  },
  message: {
    user_id: store.id,
    send_to_id: undefined,
    text: "",
  },
  booking: {
    property_id: route.params.id,
    user_id: store.id,
    start_date: route.query.from,
    end_date: route.query.to,
  },
});

const sendMessage = () => {
  const api = "http://localhost:8000/usermessage/create";

  axios
    .post(api, state.message)
    .then(() => {
      alert("Message sent successfully");
    })
    .catch((e) => {
      alert("Error: " + e.response.data.detail);
    });
};

const commitBooking = () => {
  const api = "http://localhost:8000/booking/create";

  axios
    .post(api, state.booking)
    .then(() => {
      alert("Booking submitted successfully");
    })
    .catch((e) => {
      alert("Error: " + e.response.data.detail);
    });
};

const getProperties = () => {
  let id = route.params.id;

  const api = "http://localhost:8000/property/id/" + id;

  axios.get(api).then((response) => {
    state.dataset = response.data;
    state.message.send_to_id = state.dataset.owner.id;
  });
};

const userState = reactive({
  dataset: {},
});

// const getUser = async (id) => {
//   const api = "http://localhost:8000/user/id/" + id;

//   return await axios.get(api).then((response) => {
//     return response.dataset.username;
//   });
// };

onMounted(() => {
  setNavPills();
  getProperties();
  // getUser();
});
</script>
<template>
  <BaseLayout
    title="Property Page"
    :breadcrumb="[{ label: 'Host' }, { label: 'Property' }]"
  >
    <section class="py-2 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <div v-if="state.dataset.photos[0]"
            class="page-header min-vh-100"
            :style="{
              backgroundImage: 'url(' + state.dataset.photos[0].photo + ')',
            }"
            loading="lazy"
          >
            <span class="mask bg-gradient-dark opacity-5"></span>
            <div class="container">
              <div class="row">
                <div
                  class="col-lg-6 col-md-7 d-flex justify-content-center flex-column"
                >
                  <!-- <h1 class="text-white mb-4">Material Kit</h1> -->
                  <div>
                    <h3 class="text-white opacity-8">Property Description</h3>
                    <h5 v-if="state.dataset.location" class="text-white opacity-8">{{ state.dataset.location.country }} - {{ state.dataset.location.city }}</h5>
                    <p class="text-white opacity-8 lead me-5">
                      {{ state.dataset.description }}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-12 mx-auto"></div>
        </div>
        <hr />
        <h3 class="py-3">Amenities</h3>

        <div class="container">
          <div class="row align-items-center">
            <div class="col-lg-6">
              <div class="row justify-content-start">
                <DefaultInfoCard
                  v-if="state.dataset.has_wifi"
                  color="info"
                  icon="wifi"
                  title="Wifi"
                  description="Wifi available in  property"
                />
                <DefaultInfoCard
                  v-if="state.dataset.has_airconditioning"
                  color="info"
                  icon="ac_unit"
                  title="Airconditioning"
                  description="Aiconditioning available in  property"
                />
              </div>
              <div class="row justify-content-start mt-4">
                <DefaultInfoCard
                  v-if="state.dataset.has_heat"
                  color="info"
                  icon="fireplace"
                  title="Heat"
                  description="Heat available in  property"
                />
                <DefaultInfoCard
                  v-if="state.dataset.has_kitchen"
                  color="info"
                  icon="kitchen"
                  title="Kitchen"
                  description="Kitchen available in  property"
                />
              </div>
              <div class="row justify-content-start mt-4">
                <DefaultInfoCard
                  v-if="state.dataset.has_tv"
                  color="info"
                  icon="tv"
                  title="TV"
                  description="Television available in  property"
                />
                <DefaultInfoCard
                  v-if="state.dataset.has_parking"
                  color="info"
                  icon="local_parking"
                  title="Parking"
                  description="Parking available in  property"
                />
                <DefaultInfoCard
                  v-if="state.dataset.has_elevator"
                  color="info"
                  icon="elevator"
                  title="Elevator"
                  description="Elevator available in  property"
                />
              </div>
            </div>
            <div
              v-if="state.booking.start_date && state.booking.end_date"
              class="col-lg-4 ms-auto mt-lg-0 mt-6"
            >
              <CenteredBlogCard
                image="https://images.unsplash.com/photo-1544717302-de2939b7ef71?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80"
                title="Confirm Booking"
                @click.prevent="commitBooking"
                :description="'Price/Night :' + state.dataset.price"
                :action="{
                  label: 'Submit',
                  route: '',
                  color: 'btn-success',
                }"
              />
            </div>
            <div v-else class="col-lg-4 ms-auto mt-lg-0 mt-6">
              <CenteredBlogCard
                image="https://images.unsplash.com/photo-1544717302-de2939b7ef71?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80"
                title="You can book for this property using the search menu"
                :description="'Price/Night :' + state.dataset.price"
                :action="{
                  label: 'Search',
                  route: '/search',
                  color: 'btn-success',
                }"
              />
            </div>

            <hr class="bg-success" />
            <h3 class="py-2">Indoor Space Spacifications / Rules</h3>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.indoorspace"
                color="info"
                icon="bed"
                :title="'Number of Beds: ' + state.dataset.indoorspace.bed_num"
                description="Property specifications on number of number of beds"
              />
            </div>

            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.indoorspace"
                color="info"
                icon="bathroom"
                :title="
                  'Number of Bathrooms: ' + state.dataset.indoorspace.bath_num
                "
                description="Property specifications on number of bathrooms"
              />
            </div>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.indoorspace"
                color="info"
                icon="house"
                :title="
                  'Property Type: ' +
                  state.dataset.indoorspace.property_type.property_type_name
                "
                description="Property specifications on property type"
              />
            </div>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.indoorspace"
                color="info"
                icon="bedrooms"
                :title="
                  'Number of Bedrooms: ' + state.dataset.indoorspace.bedroom_num
                "
                description="Property specifications on number of bedrooms"
              />
            </div>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.indoorspace"
                color="info"
                icon="chair"
                :title="'Living Room: Yes'"
                description="Property specifications on livingroom"
              />
              <DefaultInfoCard
                v-else
                color="info"
                icon="chair"
                :title="'Living Room: No'"
                description="Property specifications on livingroom"
              />
            </div>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.indoorspace"
                color="info"
                icon="meeting_room"
                :title="
                  'Space: ' + state.dataset.indoorspace.total_space + ' ㎡'
                "
                description="Total Space of property"
              />
            </div>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.rules[0].pet_allowed == true"
                color="info"
                icon="pets"
                :title="'Pets Allowed: Yes'"
                description="Property pet policy"
              />
              <DefaultInfoCard
                v-else
                color="info"
                icon="pets"
                :title="'Pets Allowed: No'"
                description="Property pet policy"
              />
            </div>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.rules[0].smoking_allowed == true"
                color="info"
                icon="smoking_rooms"
                :title="'Smoking Allowed: Yes'"
                description="Property smoking policy"
              />
              <DefaultInfoCard
                v-else
                color="info"
                icon="smoking_rooms"
                :title="'Smoking Allowed: No'"
                description="Property smoking policy"
              />
            </div>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.rules[0].party_allowed == true"
                color="info"
                icon="celebration"
                :title="'Parties Allowed: Yes'"
                description="Property party policy"
              />
              <DefaultInfoCard
                v-else
                color="info"
                icon="celebration"
                :title="'Parties Allowed: No'"
                description="Property party policy"
              />
            </div>
            <div class="row justify-content-start mt-4 col-lg-6">
              <DefaultInfoCard
                v-if="state.dataset.rules[0]"
                color="info"
                icon="bedtime"
                :title="
                  'Minimum Nights: ' + state.dataset.rules[0].min_night_number
                "
                description="Property minimum night policy"
              />
            </div>
          </div>
        </div>
        <hr class="bg-success" />
        <h3 class="py-2">Reviews</h3>
        <div class="row justify-content-start mt-4">
          <div
            v-for="(item, i) in state.dataset.booking"
            v-bind:key="i"
            class="col-lg-6 py-2"
          >
            <DefaultReviewCard
              v-if="item.review"
              color="bg-gradient-success"
              :image="team2"
              name="John doe"
              date="2010-10-10"
              :review="item.review.comment"
              :rating="item.review.rating"
            />
          </div>
        </div>

        <hr class="bg-success" />
        <div class="container py-6">
          <div class="row">
            <div class="col">
              <div class="card box-shadow-xl overflow-hidden mb-5">
                <div class="row">
                  <div
                    class="col-lg-5 position-relative bg-cover px-0"
                    :style="{ backgroundImage: `url(${bgContact})` }"
                    loading="lazy"
                  >
                    <div
                      class="z-index-2 text-center d-flex h-100 w-100 d-flex m-auto justify-content-center"
                    >
                      <div class="mask bg-gradient-dark opacity-8"></div>
                      <div
                        class="p-5 ps-sm-8 position-relative text-start my-auto z-index-2"
                      >
                        <h3 class="text-white">Contact Information</h3>
                        <p class="text-white opacity-8 mb-4">
                          Fill up the form and our Team will get back to you
                          within 24 hours.
                        </p>
                        <div class="d-flex p-2 text-white">
                          <div>
                            <i class="fas fa-user text-sm"></i>
                          </div>
                          <div class="ps-3">
                            <span class="text-sm opacity-8"
                              >{{ state.dataset.owner.name }}
                              {{ state.dataset.owner.lastname }}</span
                            >
                          </div>
                        </div>
                        <div class="d-flex p-2 text-white">
                          <div>
                            <i class="fas fa-phone text-sm"></i>
                          </div>
                          <div class="ps-3">
                            <span class="text-sm opacity-8">{{
                              state.dataset.owner.phone
                            }}</span>
                          </div>
                        </div>
                        <div class="d-flex p-2 text-white">
                          <div>
                            <i class="fas fa-envelope text-sm"></i>
                          </div>
                          <div class="ps-3">
                            <span class="text-sm opacity-8">{{
                              state.dataset.owner.email
                            }}</span>
                          </div>
                        </div>
                        <div class="d-flex p-2 text-white">
                          <div>
                            <i class="fas fa-map-marker-alt text-sm"></i>
                          </div>
                          <div class="ps-3">
                            <span class="text-sm opacity-8">{{
                              state.dataset.location.address
                            }}</span>
                          </div>
                        </div>
                        <div class="mt-4">
                          <MaterialButton
                            color="none"
                            size="lg"
                            class="btn-icon-only btn-link text-white mb-0"
                            data-toggle="tooltip"
                            data-placement="bottom"
                            data-original-title="Log in with Facebook"
                          >
                            <i class="fab fa-facebook"></i>
                          </MaterialButton>
                          <MaterialButton
                            color="none"
                            size="lg"
                            class="btn-icon-only btn-link text-white mb-0"
                            data-toggle="tooltip"
                            data-placement="bottom"
                            data-original-title="Log in with Twitter"
                          >
                            <i class="fab fa-twitter"></i>
                          </MaterialButton>
                          <MaterialButton
                            color="none"
                            size="lg"
                            class="btn-icon-only btn-link text-white mb-0"
                            data-toggle="tooltip"
                            data-placement="bottom"
                            data-original-title="Log in with Dribbble"
                          >
                            <i class="fab fa-dribbble"></i>
                          </MaterialButton>
                          <MaterialButton
                            color="none"
                            size="lg"
                            class="btn-icon-only btn-link text-white mb-0"
                            data-toggle="tooltip"
                            data-placement="bottom"
                            data-original-title="Log in with Instagram"
                          >
                            <i class="fab fa-instagram"></i>
                          </MaterialButton>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-7">
                    <form class="p-3" id="contact-form" method="post">
                      <div class="card-header px-4 py-sm-5 py-3">
                        <h2>Say Hi!</h2>
                        <p class="lead">We'd like to talk with you.</p>
                      </div>
                      <div class="card-body pt-1">
                        <div class="row">
                          <div class="col-md-12 pe-2 mb-3">
                            <MaterialInput
                              class="input-group-static mb-4"
                              label="Send a message to owner of this property:"
                              type="text"
                              v-model="state.dataset.owner.name"
                              placeholder="Full Name"
                              :isDisabled="true"
                            />
                          </div>
                          <div class="col-md-12 pe-2 mb-3">
                            <MaterialTextArea
                              class="input-group-static mb-4"
                              placeholder="I want to say that..."
                              :rows="6"
                              v-model="state.message.text"
                            ></MaterialTextArea>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-md-6 text-end ms-auto">
                            <MaterialButton
                              variant="gradient"
                              color="success"
                              type="submit"
                              class="mb-0"
                              @click.prevent="sendMessage"
                            >
                              Send Message</MaterialButton
                            >
                          </div>
                        </div>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </BaseLayout>
</template>
