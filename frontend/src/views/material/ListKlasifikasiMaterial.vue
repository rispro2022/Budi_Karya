<template>
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
               DAFTAR KLASIFIKASI MATERIAL
        </v-card-title>

        </v-card>
        <br>

        <v-data-table 
            :headers = "column"
            :items = "classification">
            <template v-slot:[`item.code`]="{ item }">
              <div v-if="item.id === editedItem.id">
                  <v-text-field disabled v-model="editedItem.code" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                  <span v-else>{{item.code}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.code" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                  <span v-else>{{item.code}}</span>
              </div>
            </template>

            <template v-slot:[`item.descriptions`]="{ item }">
                <v-text-field v-model="editedItem.descriptions" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.descriptions}}</span>
            </template>
           
            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.code == editedItem.code">
                  <v-icon color="red" class="mr-3" @click="close">
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
                      @click="editKlasifikasi(item)"
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
                      @click="deleteKlasifikasi(item)"
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
</template>

<script>
    export default {
        data(){
            return{
                column : [
                    {text : 'Code',         value : 'code'},
                    {text : 'Description',  value : 'descriptions'},
                    {text : 'Action',       value : 'aksi'}
                ],
                classification : [],
                editedIndex: -1,
                editedItem: {
                    code: '',
                    descriptions: '',
                },
                defaultItem: {
                    code: '',
                    descriptions: '',
                }
            }
        },

        mounted(){
            this.fetchClassification()
        },

        methods : {
            close () {
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem);
                    this.editedIndex = -1;
                }, 300)
            },

            editKlasifikasi(classification){
                console.log('ID : ' + classification.code)
                this.editedIndex = this.classification.indexOf(classification);
                this.editedItem = Object.assign({},classification);
            },

            deleteKlasifikasi(classification){
                console.log('Code : ' + classification.code)
                try{
                    const axios = require('axios');
                    axios.delete(`/klasifikasi/deleteKlasifikasiMaterial/${classification.code}`);
                    alert("Delete Klasifikasi Material Success!")
                    this.fetchClassification()
                }
                catch(error){
                    console.log(error)
                }
            },

            async fetchClassification(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/material/show_classification')
                    if(res.data == null){
                        console.log('Data kosong')
                    }else{
                        this.classification = res.data
                        console.log(res,this.classification)
                    }
                }catch(error){
                    alert("Error")
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
                    const res = await axios.post('/klasifikasi/update_klasifikasi/'+ this.editedItem.code,
                    { code         : this.editedItem.code,
                      descriptions : this.editedItem.descriptions,
                    })
                    console.log(res)
                }catch(error){
                    console.log(error)
                }
            } 
        },
    }
</script>