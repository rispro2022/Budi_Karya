<template>
    <v-card 
        class="mx-auto text-center mt-10"
        max-width = "1200">
        <br>
        <h1>List Stok Material On Workstation</h1>
        <br>
        <router-link to="/addStockMaterial">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Stock Material
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "types">
            <template v-slot:[`item.workstationCode`]="{ item }">
                <span>{{item.workstationCode}}</span>
            </template>

            <template v-slot:[`item.id`]="{ item }">
                <span>{{item.id}}</span>
            </template>

            <template v-slot:[`item.login`]="{ item }">
                <span>{{item.login}}</span>
            </template>

            <template v-slot:[`item.logout`]="{ item }">
              <span>{{item.logout}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
              <router-link :to="{name : 'Tambah Material Kosong', params:{id : `${item.id}`}}">
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="blue"
                      @click="selectStock(item)"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                  </template>
                  <span>Tambah Material Kosong</span>
                </v-tooltip>
              </router-link>
            </template>
        </v-data-table>
    </v-card>
</template>

<script>
  export default {
    data(){
      return {
        valid : true,
        column : [
            {text : 'Workstation',          value : 'workstationCode'},
            {text : 'Material Stock',       value : 'id'},        
            {text : 'Login',                value : 'login'},
            {text : 'Logout',               value : 'logout'},
          
        ],
        types : [],
      }
    },
  
    mounted(){
        this.fetchMaterial()
    },

    methods: {
      async fetchMaterial(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material_ws/get_material_onws_by_idstock/' + this.$route.params.id );
          if (res.data == null){
            alert('Stock Kosong')
          }else{
            this.types = res.data
            console.log(res,this.types)
          }
        }
        catch(error){
          console.log(error)
        }
      },
    
      selectStock(types){
          console.log('ID : ' + types.id)
      },
      
    }
  }
</script>