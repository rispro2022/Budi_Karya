<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1800">
    <br>
   
    <br>
    <v-card
      class="mx-auto text-center"
      max-width="1800">

      <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="300"
        >
        <v-card-title class="text-h4">
              DAFTAR PROYEK
            </v-card-title>
        </v-card>
        <br><br>
        <v-data-table
          :headers = "headers"
          :items = "proyek"> 
          <template v-slot:[`item.id`]="{ item }">
            <div v-if="item.id == editedItem.id">
              <v-text-field disabled v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
              <span v-else>{{item.id}}</span>
            </div>
            <div v-else>
              <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
              <span v-else>{{item.id}}</span>
            </div>
          </template>
          <template v-slot:[`item.nama`]="{ item }">
            <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
            <span v-else>{{item.nama}}</span>
          </template>
          <template v-slot:[`item.customerid`]="{ item }">
            <v-select v-model="editedItem.customerid" item-text="id" item-value="id" :items="customer" v-if="item.id == editedItem.id"></v-select>
            <span v-else>{{item.customerid}}</span>
          </template>
          <template v-slot:[`item.aksi`]="{ item }">
          <div v-if="item.id==editedItem.id">
              <v-icon color="red" class="mr-3" @click="close()">
                  mdi-window-close
              </v-icon>
              <v-icon color = "green" class="mr-3" @click="updateData()">
                  mdi-content-save
              </v-icon>
          </div>
          <div v-else>
            <router-link :to="{name : 'List Rincian Proyek by Proyek',params:{id : `${item.id}`}}">
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn 
                    class="mx-1" 
                    x-small
                    color="blue"
                    @click="selectProyek(item)"
                    v-bind="attrs"
                    v-on="on">
                    <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                </template>
                <span>List Rincian Proyek By Proyek</span>
              </v-tooltip>
            </router-link>
            
            <v-tooltip top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn 
                  class="mx-1" 
                  x-small
                  color="green"
                  @click="editProyek(item)"
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
                  @click="deleteProyek(item)"
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
      <br>
      <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="50"
        >
      
        </v-card>

    </v-card>
  </v-card>
</template>

<script>
  import axios from 'axios'
  export default {
    data: () => ({
      valid: true,
      headers:[
        {text : 'ID',               value : 'id'},
        {text : 'Nama',             value : 'nama'},
        {text : 'Tanggal Dibuat',   value : 'tglDibuat'},
        {text : 'Customer ID',      value : 'customerid'},
        {text : 'Action',           value : 'aksi'}        
      ],
      proyek:[],
      customer:[],
      editedIndex : -1,
      editedItem : {
        id : '',
        nama : '',
        customerid : ''
      },

      defaultItem : {
        id : 'New ID',
        nama : 'New Nama',
        customerid : 'New Customer'
       },
       'id' : '',
       'nama' : '',
       'customerid' : ''
    }),

    mounted(){
        this.fetchData(),
        this.fetchCustomer()
    },

    methods: {
      async fetchData(){
        try{
          const res = await axios.get(`/proyek/get_allproyek`);
          if(res.data == null){
              alert("Proyek Kosong")
          }else{
              this.proyek = res.data;
              console.log(res,this.data)
          }
        } 
        catch(error){
            alert("Error")
            console.log(error)
        }
      },

      async fetchCustomer(){
        try{
          const res = await axios.get('/customers/get_customers');
          if (res.data == null){
            alert('Customer Kosong')
          }else{
            this.customer = res.data
            console.log(res,this.customer)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

      async updateData(){
        if(this.editedIndex > -1){
          Object.assign(this.proyek[this.editedIndex],this.editedItem)
          console.log(this.editedItem)
        }
        this.close()
        try{
          const axios = require('axios')
          const res = await axios.post('/proyek/update_proyek/'+ this.editedItem.id,{
            id : this.editedItem.id,
            nama : this.editedItem.nama,
            customerid : this.editedItem.customerid
          })

          console.log(res)

        }catch(error){
          console.log(error)
        }
      },
      
      selectProyek(proyek){ 
        console.log(proyek.id)
        //open(`/listRProyekbyProyek/${proyek.id}`)
      },

      close(){
        setTimeout(()=>{
          this.editedItem = Object.assign({},this.defaultItem)
          this.editedIndex = -1;

        },300)
      },

      updateProyek(proyek){
        console.log(proyek.id)
        this.editedIndex = this.proyek.indexOf(proyek)
        this.editedItem = Object.assign({},proyek)
      },

      deleteProyek(proyek){
        console.log(proyek.id)
      }
    }
  }
</script>