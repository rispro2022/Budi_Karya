<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1700">
        <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
             DAFTAR STASIUN KERJA
            </v-card-title>
          
        </v-card>
          <br><br>
        <v-card
        class="mx-auto text-center"
        max-width="1700">
            <v-data-table
                :headers = "headers"
                :items = "stasiun">
                <template v-slot:[`item.id`]="{ item }">
                    <div v-if="item.id === editedItem.id">
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

                 <template v-slot:[`item.liniproduksi`]="{ item }">
                   <v-select v-model="editedItem.liniproduksi" item-text="id" item-value="id" :items="lini" v-if="item.id == editedItem.id"></v-select>
                  <span v-else>{{item.liniproduksi}}</span>
                </template>

                <template v-slot:[`item.aksi`]="{ item }">
                    <div v-if="item.id==editedItem.id">
                        <v-icon color="red" class="mr-3" @click="close()">
                            mdi-window-close
                        </v-icon>
                        <v-icon color="green" @click="updateData()">
                            mdi-content-save
                        </v-icon>
                    </div>
                    <div v-else>
                        <v-tooltip top>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn 
                                class="mx-1" 
                                x-small
                                color="green"
                                @click="editStasiunKerja(item)"
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
                                @click="deleteStasiunKerja(item)"
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
  export default {
    data: () => ({
      valid: true,
      headers:[
        {text : 'ID', value : 'id'},
        {text : 'Nama', value : 'nama'},
        {text : 'Dibuat', value : 'dibuat'},
        {text : 'Berlaku', value : 'berlaku'},
        {text : 'Lini Produksi', value : 'liniproduksi'},
        {text : 'Action', value : 'aksi'}     
      ],
      stasiun:[],
      lini : [],
      editedIndex : -1,
      editedItem : {
        id : '',
        nama : '',
        liniproduksi : '',
      },
      defaultItem : {
        id : '',
        nama : '',
        liniproduksi : ''
       
      },
      'id' : '',
      'nama' : '',
      'liniproduksi' : ''
    }),

    mounted(){
        this.fetchData()
        this.fetchLini()
    },

    methods: {
        editStasiunKerja(stasiun){
           console.log('ID : ' + stasiun.id)
           this.editedIndex = this.stasiun.indexOf(stasiun)
           this.editedItem = Object.assign({},stasiun)
        },

        close(){
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },

        deleteStasiunKerja(stasiun){
            console.log('ID : ' + stasiun.id)
            try{
                const axios = require('axios');
                axios.delete(`/stasiun/deleteStasiun/${stasiun.id}`);
                alert("Delete Stasiun Kerja Success!")
                this.fetchData()
            }
            catch(error){
                console.log(error)
            }
        },

        async fetchData(){
            try{
            const axios = require('axios');
            const res = await axios.get(`/stasiun_kerja/show_stasiun_kerja`);
            if(res.data == null){
                alert("Stasiun Kosong")
            }else{
                this.stasiun = res.data;
                console.log(res,this.data)
            }
            } 
            catch(error){
                alert("Error")
                console.log(error)
            }
        },
        
        async fetchLini(){
            try{
                const axios = require('axios')
                const res = await axios.get('/liniproduksi/show_liniproduksi')
                if(res.data == null){
                    console.log("Data lini kosong")
                }else{
                    this.lini = res.data;
                    console.log(res,this.lini)
                }
            }catch(error){
                console.log(error)
            }
        },
        async updateData(){
            if(this.editedIndex > -1){
                Object.assign(this.stasiun[this.editedIndex],this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/stasiun_kerja/update_stasiun_kerja/' + this.editedItem.id,{ 
                    id : this.editedItem.id,
                    nama : this.editedItem.nama,
                    liniproduksi : this.editedItem.liniproduksi
                })

                console.log(res)
                
            }catch(error){
                console.log(error)
            }
        }
    }
  }
</script>