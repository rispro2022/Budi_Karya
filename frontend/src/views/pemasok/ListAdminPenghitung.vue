<template>
    <v-app>


      <v-card 
          class="text-center mt-10 ml-3"
          width = "1500">
        
          <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
              PILIH ADMIN PENGHITUNG
        </v-card-title>

        </v-card>
        <br>
         
          <v-data-table 
            :headers = "column"
            :items = "penghitung"
            :items-per-page="5"
            >
            <template v-slot:[`item.idPenghitung`]="{ item }">
              <div v-if="item.idPenghitung === editedItem.idPenghitung">
                  <v-text-field disabled v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.idPenghitung == editedItem.idPenghitung"></v-text-field>
                  <span v-else>{{item.idPenghtiung}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.idPenghitung" :hide-details="true" dense single-line :autofocus="true" v-if="item.idPenghitung == editedItem.idPenghitung"></v-text-field>
                  <span v-else>{{item.idPenghitung}}</span>
              </div>
            </template>
  
            <template v-slot:[`item.namaPenghitung`]="{ item }">
              <v-text-field v-model="editedItem.namaPenghitung" :hide-details="true" dense single-line v-if="item.idPenghitung == editedItem.idPenghitung" ></v-text-field>
              <span v-else>{{item.namaPenghitung}}</span>
            </template>
  
            <template v-slot:[`item.tglPenghitung`]="{ item }">
              <v-text-field v-model="editedItem.tglPenghitung" :hide-details="true" dense single-line v-if="item.idPenghitung == editedItem.idPenghitung" ></v-text-field>
              <span v-else>{{item.tglPenghitung}}</span>
            </template>
  
            

            <template v-slot:[`item.aksi`]="{ item }">
            
            <div>
              <router-link :to="{name : 'Hasil Matriks Kriteria dan Bobot By Admin',params:{id : `${item.idPenghitung}`}}">
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
                  <span>Hasil Perhitungan Matriks Kriteria</span>
                </v-tooltip>
              </router-link>

              <router-link :to="{name : 'List Hasil Perbandingan Supplier Admin',params:{id : `${item.idPenghitung}`}}">
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                  </template>
                  <span>Hasil Perbandingan Matriks Supplier</span>
                </v-tooltip>
              </router-link>
              
            
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
              {text : 'ID Penghitung',    value : 'idPenghitung'},
              {text : 'Nama Penghitung',             value : 'namaPenghitung'},
              {text : 'Create Date',    value : 'tglPenghitung'},
              {text : 'Action',           value : 'aksi'}
          ],
          penghitung : [],
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
         
        }
      },
    
      mounted(){
          this.fetchData()
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
  
        async fetchData(){
          try{
            const axios = require('axios');
            const res = await axios.get('/supplier/show_admin_penghitung');
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.penghitung = res.data
              console.log(res,this.penghitung)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
        
        
      }
    }
  </script>