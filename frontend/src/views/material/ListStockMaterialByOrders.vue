<template>
    <v-card 
        class="mx-auto text-center mt-10"
        max-width = "1200">
      
        <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
              DAFTAR STOCK MATERIAL RINCIAN PEMBELIAN  {{ this.$route.params.id }}
        </v-card-title>

        </v-card>
        <br>
        <router-link :to="{name : 'Add Material Stock By Purchase Item', params : {id : `${this.$route.params.id}`}}">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
              Add Stock Material 
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "types"
            :items-per-page="5"
            >
            <template v-slot:[`item.id`]="{ item }">
                <span>{{item.id}}</span>
            </template>

            <template v-slot:[`item.purchaseItem`]="{ item }">
                <span>{{item.purchaseItem}}</span>
            </template>

            <template v-slot:[`item.merk`]="{ item }">
                <span>{{item.merk}}</span>
            </template>

            <template v-slot:[`item.quantity`]="{ item }">
              <span>{{item.quantity}}</span>
            </template>

            <template v-slot:[`item.unit`]="{ item }">
              <span>{{item.unit}}</span>
            </template>

            <template v-slot:[`item.arrivalDate`]="{ item }">
              <span>{{item.arrivalDate}}</span>
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
                  <span>Tambah Material</span>
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
            {text : 'ID',                   value : 'id'},
            {text : 'Merk',                 value : 'merk'},        
            {text : 'Quantity',             value : 'quantity'},
            {text : 'Arrival Date',         value : 'arrivalDate'},
            {text : 'Unit',                 value : 'namaUnit'},
            {text : 'Order',                value : 'purchaseItem'},
           
        ],
        types : [],
      }
    },
  
    mounted(){
        this.fetchMaterialByOrder()
   
    },

    methods: {
      async fetchMaterialByOrder(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_materialstock_by_order/' + this.$route.params.id);
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

      async fetchPurchaseItemInStock(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_purchase_item_in_matstock/' + this.$route.params.id);
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