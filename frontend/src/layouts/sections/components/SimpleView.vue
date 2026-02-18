<script setup>
import "prismjs/themes/prism.css"; // import the styles somewhere

defineProps({
  title: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div
    class="position-relative border-radius-xl overflow-hidden shadow-lg mb-7"
  >
    <div class="container border-bottom">
      <div class="row justify-space-between py-2">
        <div class="col-lg-3 me-auto">
          <p class="lead text-dark pt-1 mb-0">{{ title }}</p>
        </div>
        <div class="col-lg-3">
          <div class="nav-wrapper position-relative end-0">
            <!-- <ul class="nav nav-pills nav-fill flex-row p-1" role="tablist">
              <li class="nav-item">
                <a
                  class="nav-link mb-0 px-0 py-1 active"
                  data-bs-toggle="tab"
                  :href="`#preview-${id}`"
                  role="tab"
                  aria-selected="true"
                >
                  <i class="fas fa-desktop text-sm me-2"></i> Preview
                </a>
              </li>
              <li class="nav-item">
                <a
                  class="nav-link mb-0 px-0 py-1"
                  data-bs-toggle="tab"
                  :href="`#code-${id}`"
                  role="tab"
                  aria-selected="false"
                >
                  <i class="fas fa-code text-sm me-2"></i> Code
                </a>
              </li>
            </ul> -->
          </div>
        </div>
      </div>
    </div>
    <div class="tab-content tab-space">
      <div class="tab-pane active p-2">
        <div class="overflow-auto">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.my-editor {
  /* we dont use `language-` classes anymore so thats why we need to add background and text color manually */
  color: black;
  /* you must provide font-family font-size line-height. Example: */
  font-family: Consolas, Fira Mono, Menlo, Courier, monospace;
  font-size: 1em;
  line-height: 1.5;
  padding: 5px;
  tab-size: 4;
}
/* optional class for removing the outline */
.prism-editor__textarea:focus {
  outline: none;
}
</style>
