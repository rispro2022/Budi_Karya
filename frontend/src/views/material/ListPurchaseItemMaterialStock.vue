<template>
  <v-app>
    <v-card 
        class="mx-auto text-center mt-10"
        width = "1500">
       
        <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
              DAFTAR RINCIAN PEMESAN MATERIAL {{ this.$route.params.id }}
        </v-card-title>

        </v-card>
        <br>

        <router-link :to="{name : 'Tambah Purchase Item By Purchase Material', params : {id : `${this.$route.params.id}`}}">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Purchase Item 
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "prcItembyprcMat"
            :items-per-page="5"
            >
          <template v-slot:[`item.aksi`]="{ item }">
            <router-link :to="{name : 'List Stock Material By Orders',params : {id : `${item.id_item}`}}">
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn 
                    class="mx-1" 
                    x-small
                    color="blue"
                    v-bind="attrs"
                    v-on="on">
                    <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                </template>
                <span>List Stock Material By Purchase Item</span>
              </v-tooltip>
            </router-link>

            <v-tooltip top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn 
                  class="mx-1" 
                  x-small
                  color="green"
                  @click="editMaterial(item)"
                  v-bind="attrs"
                  v-on="on">
                  <v-icon small dark>mdi-pencil</v-icon>
                </v-btn>
              </template>
              <span>Edit</span>
            </v-tooltip>
            
            <v-tooltip top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn 
                  class="mx-1" 
                  x-small
                  color="red"
                  @click="deleteMaterial(item)"
                  v-bind="attrs"
                  v-on="on">
                  <v-icon small dark>mdi-trash-can-outline</v-icon>
                </v-btn>
              </template>
              <span>Delete</span>
            </v-tooltip>
          </template>
        </v-data-table>
    </v-card>
    <v-card
      class="mx-auto text-center mt-12"
      max-width = "750">
     
      <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
              DAFTAR PEMESAN MATERIAL {{ this.$route.params.id }}
        </v-card-title>

        </v-card>
        <br>

      <v-data-table 
          :headers="column2"
          :items="purchasematerial">
        </v-data-table>
    </v-card>
  </v-app>
</template>
   
<script>
  export default {
    data(){
      return {
        valid : true,
        column : [
          {text : 'ID',                 value : 'id_item'},
          {text : 'Material Type Code', value : 'materialTypeCode'},
          {text : 'Purchase ID',        value : 'purchaseId'},
          {text : 'Quantity',           value : 'quantity'},
          {text : 'Schedulled Arrival', value : 'schedulledArrival'},
          {text : 'Supplier',           value : 'supplierCode'},
          {text : 'Unit',               value : 'unit'},
          {text : 'Action',           value : 'aksi'}
        ],
        column2 : [
          {text : 'ID',               value : 'id'},
          {text : 'Nama',             value : 'nama'},
          {text : 'Purchase Date',    value : 'purchaseDate'},
          {text : 'Purchaser Name',   value : 'purchaserName'},
        ],
        prcItembyprcMat : [],
        purchasematerial : []
      }
    },

    mounted(){
      this.fetchPrcItemByPrcMat(),
      this.fetchComparePurchaseMaterialInItem()
    },

    methods: {
      close () {
        setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem);
            this.editedIndex = -1;
        }, 300)
      },

      async fetchPrcItemByPrcMat(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_purchase_item_compare/' + this.$route.params.id);
          if (res.data == null){
            alert('Purchase Item Kosong')
          }else{
            this.prcItembyprcMat = res.data
            console.log(res,this.prcItembyprcMat)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

      async fetchComparePurchaseMaterialInItem(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_purchasematerial_in_purchaseitem/' + this.$route.params.id);
          if (res.data == null){
            alert('Purchase Item Kosong')
          }else{
            this.purchasematerial = res.data
            console.log(res,this.purchasematerial)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      }
    }
  }
</script>