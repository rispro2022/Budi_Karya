<template>
    <v-app>
      <v-card 
          class="mx-auto text-center mt-10"
          max-width = "1300">
          <br>
          <h2>Daftar Pembelian Perkakas</h2>
          <br>
          <router-link to="/purchaseTools">
              <v-btn color="primary" class="d-flex ml-4 mb-6">
                  Purchase Tools
              </v-btn>
          </router-link>
          <v-data-table 
            :headers = "column"
            :items = "types"
            :items-per-page="5"
            >
            <template #[`item.toolPurchaseId`]="{ item }">
              <div v-if="item.toolPurchaseId === editedItem.toolPurchaseId">
                  <v-text-field disabled v-model="editedItem.toolPurchaseId" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolPurchaseId == editedItem.toolPurchaseId"></v-text-field>
                  <span v-else>{{item.toolPurchaseId}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.toolPurchaseId" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolPurchaseId == editedItem.toolPurchaseId"></v-text-field>
                  <span v-else>{{item.toolPurchaseId}}</span>
              </div>
            </template>
  
            <template v-slot:[`item.orderName`]="{ item }">
            <v-text-field v-model="editedItem.orderName" :hide-details="true" dense single-line v-if="item.toolPurchaseId == editedItem.toolPurchaseId" ></v-text-field>
            <span v-else>{{item.orderName}}</span>
          </template>
  
          <template v-slot:[`item.purchaseDate`]="{ item }">
            <v-text-field v-model="editedItem.purchaseDate" :hide-details="true" dense single-line v-if="item.toolPurchaseId == editedItem.toolPurchaseId" ></v-text-field>
            <span v-else>{{item.purchaseDate}}</span>
          </template>

  
            <template v-slot:[`item.purchaserName`]="{ item }">
              <v-text-field v-model="editedItem.purchaserName" :hide-details="true" dense single-line v-if="item.toolPurchaseId == editedItem.toolPurchaseId" ></v-text-field>
              <span v-else>{{item.purchaserName}}</span>
            </template>
            
            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.toolPurchaseId == editedItem.toolPurchaseId">
                <v-icon color="red" class="mr-3" @click="close">
                  mdi-window-close
                </v-icon>
                <v-icon color="green" @click="updateData()">
                  mdi-content-save
                </v-icon>
              </div>
              <div v-else>
                <router-link :to="{name : 'List Purchase Item By Purchase Tools',params:{id : `${item.toolPurchaseId}`}}">
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
                    <span>List Purchase Item By Purchase Tools</span>
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
              </div>
            </template>
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
          {text : 'ID',               value : 'toolPurchaseId'},
          {text : 'Order Name',       value : 'orderName'},
          {text : 'Purchase Date',    value : 'PurchaseDate'},
          {text : 'Purchaser Name',   value : 'purchaserName'},
          {text : 'Action',           value : 'aksi'}
      ],
      types : [],
      requirmentMaterial : [],
      editedIndex: -1,
      editedItem: {
        id: '',
        nama: '',
        purchaseDate: '',
        purchaserName: '',
      },
      defaultItem: {
        id: '',
        nama: '',
        purchaseDate: '',
        purchaserName: '',
      },
      dueDate: undefined,
      datetime: undefined
    }
  },

  mounted(){
      this.fetchMaterial()
  },

  methods: {
    close () {
      setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem);
          this.editedIndex = -1;
      }, 300)
    },

    editMaterial(types){
      console.log('ID : ' + types.id)
      this.editedIndex = this.types.indexOf(types);
      this.editedItem = Object.assign({},types);
    },

    async fetchMaterial(){
      try{
        const axios = require('axios');
        const res = await axios.get('/tools/show_tool_purchase');
        if (res.data == null){
          alert('Material Kosong')
        }else{
          this.types = res.data
          console.log(res,this.types)
        }
      }
      catch(error){
        alert("Error")
        console.log(error)
      }
    },
    
    deleteMaterial(types){
        console.log('ID : ' + types.id)
        try{
            const axios = require('axios');
            axios.delete(`/material/delete_purchase_material/${types.id}`);
            alert("Delete Purchase Material Success!")
            this.fetchMaterial()
        }
        catch(error){
            console.log(error)
        }
    },

    async updateData(){
      if (this.editedIndex > -1) {
          Object.assign(this.types[this.editedIndex], this.editedItem)
          console.log(this.editedItem)
      }
      this.close()
      try{
          const axios = require('axios')
          const res = await axios.post('/material/update_purchase_material/'+ this.editedItem.id,
          { id     : this.editedItem.id,
            nama     : this.editedItem.nama,
            purchaseDate    : this.editedItem.purchaseDate,
            purchaserName : this.editedItem.purchaserName,
          })
          console.log(res)
      }catch(error){
          console.log(error)
      }
    },
    
    
  }
}


</script>
