<template>
  <footer class="block py-4">
    <div class="container mx-auto px-4">
      <hr class="mb-4 border-b-1 border-gray-300"/>
      <div class="flex flex-wrap items-center md:justify-between justify-center">
        <div class="w-full md:w-4/12 px-4">
          <div class="text-sm text-gray-600 font-semibold py-1">
            The report generated with <a
            href="https://github.com/annidy/ObjCSameCodeFinder"
            class="text-gray-600 hover:text-gray-800 text-sm font-semibold py-1"
          >
            SameCodeFinder
          </a>
          </div>
        </div>
        <div class="w-full md:w-8/12 px-4">
          <ul class="flex flex-wrap list-none md:justify-end  justify-center">
            <li>
              creator
            </li>
            <li>
              <a
                href="mailto:fengxing2@bytedance.com"
                class="text-gray-700 hover:text-gray-900 text-sm font-semibold block py-1 px-3"
              >
                fengxing2
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
import UserDropdownComponent from "./UserDropdown.vue";

export default {
  components: {
    UserDropdownComponent
  }
};
</script>
