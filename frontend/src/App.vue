<template>
  <v-app class="grey lighten-4">
    <div v-if="idRole == 'Guest'">
      <SidebarGuest />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-if="idRole == 1">
      <SidebarAdmin />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-else-if="idRole == 2">
      <SidebarEngineer />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-else-if="idRole == 3">
      <SidebarMaterial />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-else-if="idRole == 4">
      <SidebarManager />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-else-if="idRole == 5">
      <SidebarUmum />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-else-if="idRole == 6">
      <SidebarDisplay />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-else-if="idRole == 7">
      <SidebarOperator />
    </div>
    <div v-else-if="idRole == 8">
      <SidebarTools />
      <v-main>
        <router-view/>
      </v-main>
    </div>
  </v-app>
</template>

<script>
import SidebarGuest from './components/SidebarGuest.vue'
import SidebarAdmin from './components/SidebarAdmin.vue'
import SidebarManager from './components/SidebarManager.vue'
import SidebarEngineer from './components/SidebarEngineer.vue'
import SidebarMaterial from './components/SidebarMaterial.vue'
import Login from "./services/Login.js"
import SidebarUmum from './components/SidebarUmum.vue'
import SidebarDisplay from './components/SidebarDisplay.vue'
import SidebarOperator from './components/SidebarOperator.vue'
import SidebarTools from './components/SidebarTools.vue'

export default {
  name: 'App',
  components: {
    SidebarGuest,
    SidebarAdmin,
    SidebarManager,
    SidebarEngineer,
    SidebarMaterial,
    SidebarUmum,
    SidebarDisplay,
    SidebarOperator,
    SidebarTools
},

  mounted() {
    this.fetchData();
  },

  data: () => {
    const data = [];
      return {
          idRole: null,
          username : '',
          loginService: new Login(),
          data,
      };
  },

  methods: {
    async fetchData() {
        this.idRole = this.loginService.getCurrentUserType();
        this.username = this.loginService.getCurrentUsername();
        console.log('Usertype: ' + this.idRole)
        console.log('Username: ' + this.username)
    },
  },
};
</script>
