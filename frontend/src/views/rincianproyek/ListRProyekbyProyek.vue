<template>
    <v-app>
        <div class="d-flex ml-14">
            <v-card class="ml-8 text-center mt-6" width="600">
                <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
                PROYEK {{this.$route.params.id}}
            </v-card-title>
          </v-card>
                <v-data-table
                    :headers = "headers2"
                    :items = "proyekinrincian"
                    :items-per-page="5"
                >
                </v-data-table>
            </v-card>
      
            <v-card class="ml-15 text-center mt-6" width = "500">
                
                <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
                PELANGGAN {{this.idcustomer}}
            </v-card-title>
          </v-card>

                <v-data-table
                    :headers = "headers3"
                    :items = "customer"
                    :items-per-page="5"
                >
                </v-data-table>
            </v-card>
        </div>
        <v-card class="mx-auto text-center mt-6" width="1500">
            <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
              RINCIAN PROYEK {{this.$route.params.id}}
            </v-card-title>
          </v-card>
            <br>
            <br>
            <router-link :to="{name : 'Tambah Rincian Proyek by Proyek',params : {id : `${this.$route.params.id}`}}">
                <v-btn color="primary" class="d-flex ml-4 mb-6">
                    Add Rincian Proyek
                </v-btn>
            </router-link>
            <v-card class="mx-auto text-center" max-width="1500">
                <v-data-table
                    :headers = "headers"
                    :items = "rincianbyproyek"
                    :items-per-page="5"
                    >
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
                    <template v-slot:[`item.jumlah`]="{ item }">
                        <v-text-field v-model="editedItem.jumlah" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.jumlah}}</span>
                    </template>

                    <template v-slot:[`item.dueDate`]="{ item }">
                        <div v-if="item.id === editedItem.id">
                            <v-text-field disabled v-model="editedItem.dueDate" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                            <span v-else>{{item.dueDate}}</span>
                        </div>
                        <div v-else>
                            <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                            <span v-else>{{item.dueDate}}</span>
                        </div>
                    </template>

                    <template v-slot:[`item.proyek`]="{ item }">
                        <v-text-field v-model="editedItem.proyek" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.proyek}}</span>
                    </template>

                    <template v-slot:[`item.jenisProduk`]="{ item }">
                        <v-text-field v-model="editedItem.jenisProduk" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.jenisProduk}}</span>
                    </template>
                    <template v-slot:[`item.aksi`]="{ item }">
                        <div v-if="item.id == editedItem.id">
                            <v-icon color="red" class="mr-3" @click="close()">
                                mdi-window-close
                            </v-icon>
                            <v-icon color="green" class="mr-3" @click="updateData()">
                                mdi-content-save
                            </v-icon>
                        </div>
                        <div v-else>
                            <router-link :to="{name:'List Produk by Rincian Proyek',params:{'id': `${item.id}`}}">
                                <v-tooltip top>
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-btn 
                                        class="mx-1" 
                                        x-small
                                        color="blue"
                                        @click="selectRProyektoProduct(item)"
                                        v-bind="attrs"
                                        v-on="on">
                                        <v-icon small dark>mdi-check</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>List Produk By Rincian Proyek</span>
                                </v-tooltip>
                            </router-link>
    
                            <v-tooltip top>
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn 
                                    class="mx-1" 
                                    x-small
                                    color="green"
                                    @click="editRProyek(item)"
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
                                    @click="deleteRProyek(item)"
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
    </v-app>
</template>

<script>
export default {
    data(){
        return{
            headers : [
                {text : 'ID Rincian Proyek',value : 'id'},
                {text : 'Jenis Produk',value : 'nama'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Due Date',value : 'dueDate'},
                {text : 'Proyek',value : 'proyek'},
                {text : 'Action', value : 'aksi'}
            ],
            headers2 : [
               
                {text : 'ID Proyek', value : 'IdProyek'},
                {text : 'Nama Proyek', value : 'NamaProyek'}
            ],
            headers3 : [
                {text : 'ID Customer', value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'NamaCustomer'},
            ],
            customer : [],
            rincianbyproyek : [],
            proyekinrincian : [],
            editedIndex : -1,
            editedItem : {
                id : '',
                jumlah : '',
                dueDate : '',
                proyek : '',
                jenisProduk : ''
            },
            defaultItem : {
                id : 'New ID',
                jumlah : 'New Jumlah',
                dueDate : 'New Due Date',
                proyek : 'New Proyek',
                jenisProduk : 'New Jenis Produk'
            },
            idcustomer : ''
        }
    },

    mounted(){
        this.fetchRProyekbyProyek(),
        this.fetchProyekInRProyek()
    },
    
    methods : {
        async fetchRProyekbyProyek(){
            try{
                const axios = require('axios')
                const res = await axios.get('/rproyek/show_rproyek_by_proyek/' + this.$route.params.id)
                if (res == null){
                    alert("Rincian Proyek Kosong")  
                }
                else{
                    this.rincianbyproyek = res.data
                    console.log(res,this.rincianbyproyek)
                }
            }
            catch(error){
                alert("Error")
                console.log(error)
            }
        },

        async fetchProyekInRProyek(){
            try{
                
                const axios = require('axios')
                const res = await axios.get('/rproyek/show_proyek_inrproyek/' + this.$route.params.id)
                if(res == null){
                    console.log("Data kosong")
                }else{
                    this.proyekinrincian = res.data
                    this.customer = res.data
                    this.idcustomer = this.customer[0].IdCustomer
                    console.log(res,this.proyekinrincian)
                }

            }catch(error){
                alert("Error")
                console.log(error)
            }
        },

        async updateData(){
            if(this.editedIndex > -1){
                Object.assign(this.rincianbyproyek[this.editedIndex],this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/rproyek/update_rproyek/' + this.editedItem.id,{ 
                    id : this.editedItem.id,
                    jumlah : this.editedItem.jumlah,
                    dueDate : this.editedItem.dueDate,
                    proyek : this.editedItem.proyek,
                    jenisProduk : this.editedItem.jenisProduk
                })
                console.log(res)                    
            }catch(error){
                console.log(error)
            }
        },

        selectRProyektoProduct(rincianbyproyek){
            console.log(rincianbyproyek.id)
        },

        selectRProyektoJProduct(rincianbyproyek){
             console.log(rincianbyproyek.id)
        },

        editRProyek(rincianbyproyek){
            this.editedIndex = this.rincianbyproyek.indexOf(rincianbyproyek)
            this.editedItem = Object.assign({},rincianbyproyek)
        },

        close(){
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },
    }
}
</script>