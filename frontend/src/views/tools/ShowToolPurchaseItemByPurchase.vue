<template>
<v-app>


    <v-card class="text-center mt-4 ml-3" max-width="1350">

        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>

          <v-autocomplete
          item-text="nama"
          item-value="codes"
          v-model="type"
          :items="tooltype"
          label="Tool Type"
          ></v-autocomplete>

          <v-text-field
          v-model="quantity"
          label="Quantity"
          required
          ></v-text-field>

          <v-autocomplete   
          item-text="nama"
          item-value="id"
          v-model="unit"
          :items="units"
          label="Unit"
          ></v-autocomplete>

          <div class="d-flex">
            <v-menu 
              class="mt-6"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-10" :value="arrivalDatePlan" v-bind="attrs" v-on="on" label="Schedulled Arrival" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker full-width v-model="arrivalDatePlan"></v-date-picker>
          </v-menu>
        </div>
         
          <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="validate()"
          >
            Submit
            </v-btn>

            <v-btn
              color="error"
              class="mr-4"
             @click="reset"
              >
              Reset
            </v-btn>

        </v-form>

        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>
    </v-card>

 



    <v-card
        class="text-center mt-10 ml-3"
        max-width="1000">
        <br>
        <h1>List Tool Purchase Item</h1>
        <br>
        <v-card
            class="mx-auto text-center"
            max-width="1000">
            <v-data-table
                :headers = "column"
                :items = "toolPurchaseItem"
            >
            <template v-slot:[`item.purchaseItemId`]="{ item }">
                <v-text-field v-model="editedItem.purchaseItemId" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.purchaseItemId}}</span>
            </template>

            <template v-slot:[`item.namaToolType`]="{ item }">
                <v-text-field v-model="editedItem.namaToolType" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.namaToolType}}</span>
            </template>

            <template v-slot:[`item.quantity`]="{ item }">
                <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.quantity}}</span>
            </template>

            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>

            
            <template v-slot:[`item.arrivalDatePlan`]="{ item }">
                <v-text-field v-model="editedItem.arrivalDatePlan" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>



            <template v-slot:[`item.aksi`]="{ item }">
            <div v-if="item.id==editedItem.id">
                <v-icon color="red" class="mr-3" @click="close()">
                    mdi-window-close
                </v-icon>
                <v-icon color="green" @click="updateToolBox()">
                    mdi-content-save
                </v-icon>
            </div>
            <div v-else>
                <router-link :to="{name : 'List Tools Stock By Purchase Item', params:{id : `${item.purchaseItemId}`}}">
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
                        <span>List Tool Stock</span>
                    </v-tooltip>
                </router-link>

                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      @click="editToolBox(item)"
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
                      @click="deleteToolBox(item)"
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
    </v-card>

</v-app>
</template>

<script>
export default {
    data(){
        return {
            column : [
                {text : 'ID Purchase Item', value : 'purchaseItemId'},
                {text : 'Nama Tool Type', value : 'namaToolType'},
                {text : 'Quantity', value : 'quantity'},
                {text : 'Satuan', value : 'nama'},
                {text : 'Action',value : 'aksi'}
            ],
            toolPurchaseItem : [],
            tooltype : [],
            units : [],
            unit : '',
            type : '',
            quantity : '',
            arrivalDatePlan : '',
            editedIndex : -1,
            editedItem : {
                id : '',
                nama  : '',
            },
            defaultItem : {
                id : '',
                nama : '',
            },
            snackbar : {
            show : false,
            color : null,
            message : null,
      },
        }
    },

    mounted(){
        this.fetchData(),
        this.fetchUnit(),
        this.fetchToolType()
    },

    methods : {

      validate () {
        if(this.$refs.form.validate()){
          this.addPurchaseItem()
        }
      },

        async fetchData(){
            try{
                const axios = require('axios')
                const res = await axios.get('/tools/show_purchase_item_bypurchase/' + this.$route.params.id)
                if(res.data == null){
                    alert("Data Tool Box kosong")
                }else{
                    this.toolPurchaseItem = res.data
                    console.log(res,this.toolBox)
                }
            }
            catch(error){
                console.log(error)
            }
        },

        async fetchUnit(){
        try{
            const axios = require('axios')
            const res = await axios.get('/unit/get_unit')
            if (res.data == null){
                alert("Material Unit Kosong")
            }else{
                this.units = res.data
                console.log(res,this.units)
            }
        }catch(error){
            alert(error)
            console.log(error)
        } 
      },

      async fetchToolType(){
        try{

            const axios = require('axios')
            const res = await axios.get('/tools/show_tooltype')
            if(res.data == null){
              console.log("type kosong")
            }
            else{
              this.tooltype = res.data
              console.log(res,this.tooltype)
            }

        }catch(error){
           console.log(error)
        }
      },
        
      async addPurchaseItem(){

        try{
          const axios = require('axios')
          const res = await axios.post('/tools/add_toolpurchase_by_purchasetools/' + this.$route.params.id,{
             type : this.type,
             quantity : this.quantity,
             unit : this.unit,
             arrivalDatePlan : this.arrivalDatePlan
          })

          if(res.data.status == 'berhasil'){
            this.snackbar = {
              show : true,
              message : "Purchase Tools Item Berhasil",
              color : "green"
            }

            location.replace('/listPurchaseItemByPurchaseTools/' + this.$route.params.id)

          }else if(res.data.status == 'gagal'){
            this.snackbar = {
              show : true,
              message : "Purchase Tools Item Gagal",
              color : "red"
            }
          }

        }
        catch(error){
          this.snackbar = {
            show : true,
            message : "Purchase Item Tools Error",
            color : "red"
          }
          console.log(error)
        }

      }
       
    }
}
</script>
