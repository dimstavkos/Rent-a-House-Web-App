<script setup>
import { reactive, inject, onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import MaterialButton from "@/components/MaterialButton.vue";

// nav-pills
import setNavPills from "@/assets/js/nav-pills.js";

const axios = inject("axios");

const exportUsersAsJSON = () => {
  const api = "http://localhost:8000/export/users";

  axios.get(api, { responseType: "blob" }).then((response) => {
    const blob = new Blob([response.data]);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "users.json";
    link.click();
  });
};

const exportUsersAsXML = () => {
  const api = "http://localhost:8000/export/users";

  const config = {
    headers: {
      Accept: "application/xml",
    },
    responseType: "blob",
  };

  axios.get(api, config).then((response) => {
    const blob = new Blob([response.data]);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "users.xml";
    link.click();
  });
};

const exportLocationsAsJSON = () => {
  const api = "http://localhost:8000/export/locations";

  axios.get(api, { responseType: "blob" }).then((response) => {
    const blob = new Blob([response.data]);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "locations.json";
    link.click();
  });
};

const exportLocationsAsXML = () => {
  const api = "http://localhost:8000/export/locations";

  const config = {
    headers: {
      Accept: "application/xml",
    },
    responseType: "blob",
  };

  axios.get(api, config).then((response) => {
    const blob = new Blob([response.data]);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "locations.xml";
    link.click();
  });
};


const exportPropertiesAsJSON = () => {
  const api = "http://localhost:8000/export/locations";

  axios.get(api, { responseType: "blob" }).then((response) => {
    const blob = new Blob([response.data]);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "properties.json";
    link.click();
  });
};

const exportPropertiesAsXML = () => {
  const api = "http://localhost:8000/export/locations";

  const config = {
    headers: {
      Accept: "application/xml",
    },
    responseType: "blob",
  };

  axios.get(api, config).then((response) => {
    const blob = new Blob([response.data]);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "properties.xml";
    link.click();
  });
};


const exportBookingsAsJSON = () => {
  const api = "http://localhost:8000/export/bookings";

  axios.get(api, { responseType: "blob" }).then((response) => {
    const blob = new Blob([response.data]);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "bookings.json";
    link.click();
  });
};

const exportBookingsAsXML = () => {
  const api = "http://localhost:8000/export/bookings";

  const config = {
    headers: {
      Accept: "application/xml",
    },
    responseType: "blob",
  };

  axios.get(api, config).then((response) => {
    const blob = new Blob([response.data]);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "bookings.xml";
    link.click();
  });
};


onMounted(() => {
  setNavPills();
});
</script>
<template>
  <BaseLayout
    title="Export dataset"
    :breadcrumb="[{ label: 'Administrator' }, { label: 'Export dataset' }]"
  >
    <section class="py-7 mt-3 bg-gray-100">
      <div class="container">
        <div class="row justify-space-between text-center py-2">
          <div class="col-12 mx-auto">
            <MaterialButton
              variant="gradient"
              color="secondary"
              class="w-auto me-2"
              @click="exportUsersAsJSON"
              >Export users as JSON</MaterialButton
            >
            <MaterialButton
              variant="gradient"
              color="primary"
              class="w-auto me-2"
              @click="exportUsersAsXML"
              >Export users as XML</MaterialButton
            >
          </div>
          <div class="col-12 mx-auto">
            <MaterialButton
              @click="exportLocationsAsJSON"
              variant="gradient"
              color="info"
              class="w-auto me-2"
              >Export locations as JSON</MaterialButton
            >
            <MaterialButton
              @click="exportLocationsAsXML"
              variant="gradient"
              color="success"
              class="w-auto me-2"
              >Export locations as XML</MaterialButton
            >
          </div>
          <div class="col-12 mx-auto">
            <MaterialButton
              @click="exportPropertiesAsJSON"
              variant="gradient"
              color="warning"
              class="w-auto me-2"
              >Export properties as JSON</MaterialButton
            >
            <MaterialButton
              @click="exportPropertiesAsXML"
              variant="gradient"
              color="danger"
              class="w-auto me-2"
              >Export properties as XML</MaterialButton
            >
          </div>
          <div class="col-12 mx-auto">
            <MaterialButton
              @click="exportBookingsAsJSON"
              variant="gradient"
              color="warning"
              class="w-auto me-2"
              >Export bookings as JSON</MaterialButton
            >
            <MaterialButton
              @click="exportBookingsAsXML"
              variant="gradient"
              color="danger"
              class="w-auto me-2"
              >Export bookings as XML</MaterialButton
            >
          </div>
        </div>
      </div>
    </section>
  </BaseLayout>
</template>
