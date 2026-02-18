import { defineStore } from "pinia";
import { ref } from "vue";
import bootstrap from "bootstrap/dist/js/bootstrap.min.js";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAppStore = defineStore("storeId", {
  state: () => {
    const initial_id = localStorage.getItem("id") || "";
    const id = ref(initial_id);

    const initial_username = localStorage.getItem("username") || "";
    const username = ref(initial_username);

    const initial_token = localStorage.getItem("token") || "";
    const token = ref(initial_token);

    const initial_is_admin = localStorage.getItem("is_admin") || "false";
    const is_admin = ref(initial_is_admin);

    const initial_is_guest = localStorage.getItem("is_guest") || "true";
    const is_guest = ref(initial_is_guest);

    const initial_is_host = localStorage.getItem("is_host") || "false";
    const is_host = ref(initial_is_host);

    const initial_is_renter = localStorage.getItem("is_renter") || "false";
    const is_renter = ref(initial_is_renter);

    const router = useRouter();

    return {
      bootstrap,
      router,
      id,
      username,
      token,
      is_admin,
      is_guest,
      is_host,
      is_renter,
    };
  },

  actions: {
    async signIn(username, password) {
      const api = "http://localhost:8000/auth/login";
      const payload = {
        username: username,
        password: password,
      };

      let response = await axios.post(api, payload);

      if (response.status === 200) {
        let data = response.data;
        this.id = data.id;
        this.username = data.username;
        this.token = data.token;
        this.is_admin = "false";
        this.is_guest = "false";
        this.is_host = "false";
        this.is_renter = "false";

        // console.log(data.roles);

        for (let key in data.roles) {
          const role = data.roles[key];

          if (role.id == 1) {
            this.is_admin = "true";
            this.is_guest = "false";
            this.is_host = "true";
            this.is_renter = "true";
            break;
          }
          if (role.id == 2) {
            this.is_host = "true";
            this.is_renter = "true";
          }
          if (role.id == 3) {
            this.is_renter = "true";
          }
        }

        console.log(this.is_guest);

        localStorage.setItem("id", this.id);
        localStorage.setItem("username", this.username);
        localStorage.setItem("token", this.token);
        localStorage.setItem("is_guest", this.is_guest);
        localStorage.setItem("is_admin", this.is_admin);
        localStorage.setItem("is_host", this.is_host);
        localStorage.setItem("is_renter", this.is_renter);

        if (this.is_admin === "true") {
          this.router.push({ name: "manage-users" });
        } else if (this.is_host === "true") {
          this.router.push({ name: "host-properties" });
        } else {
          this.router.push({ name: "renter-properties" });
        }
      } else {
        // alert("Login failed");
      }
    },
    async signOut() {
      this.id = "";
      this.username = "";
      this.token = "";
      this.is_guest = "true";
      this.is_admin = "false";
      this.is_host = "false";
      this.is_renter = "false";

      localStorage.setItem("id", this.id);
      localStorage.setItem("username", this.username);
      localStorage.setItem("token", this.token);
      localStorage.setItem("is_guest", this.is_guest);
      localStorage.setItem("is_admin", this.is_admin);
      localStorage.setItem("is_host", this.is_host);
      localStorage.setItem("is_renter", this.is_renter);

      this.router.push({ name: "signin-basic" });
    },
  },
});
