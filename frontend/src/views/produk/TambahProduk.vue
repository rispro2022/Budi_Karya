<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1000">
    <br>
    <h1>Tambah Produk Baru</h1>
    <v-form
      class="pa-6"
      ref="form"
      @submit.prevent="submitHandler"
      v-model="valid"
      lazy-validation>
      
      <v-text-field
      v-model="id"
      :counter="9"
      :rules="idRules"
      label="ID"
      required
      ></v-text-field>

      <v-autocomplete
      item-text="id"
      item-value="id"
      v-model="rincianProyek"
      :items="items"
      label="Rincian Proyek"
      ></v-autocomplete>

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
    
    <div v-if="snackBar == true">
      <v-snackbar top color="green" v-model="snackBar">
        Insert Produk Sukses!
      </v-snackbar>
    </div>

    <div v-else-if="snackBar == false">
      <v-snackbar top color="red" v-model="snackBar">
        Insert Produk Gagal!
      </v-snackbar>
    </div>

    <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
      {{snackbar.message}}
    </v-snackbar>
  </v-card>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    valid: true,  
    snackbar: {
      show: false,
      message: null,
      color: null
    },
    id: '',
    idRules: [
      v => !!v || 'ID is required',
      v => (v && v.length <= 9 && v.length >= 5) || 'ID must be 5-9 characters',
    ],
    rincianProyek: undefined,
    snackBar : false,
    items: [],
  }),

  mounted(){
    this.fetchRincianProyek()
  },

  methods: {
    validate () {
      if(this.$refs.form.validate()){
        this.InsertProduk()
      }
    },

    async InsertProduk(){
      try{
        const response = await axios.post('/product/add_product',
          { id: this.id,
            rincianProyek: this.rincianProyek
          }
        );
        console.log(response,this.data)
        if(response.data.Status == "Berhasil"){
            this.snackbar = {
            message : "Insert Produk Success",
            color : 'green',
            show : true
        }}
        else if(response.data.Status == "Gagal"){
            this.snackbar = {
            message : "Insert Produk Gagal, ID Sudah Tersedia!",
            color : 'red',
            show : true
        }}
      }
      catch(error){
        this.snackbar = {
          message : "Insert Produk Error",
          color : 'error',
          show : true
        }
        console.log(error)
      }
    },

    async fetchRincianProyek(){
      try{
          const axios = require('axios')
          const res = await axios.get('/rproyek/show_rproyek')
          if (res.data == null){
              alert("Proyek Kosong")
          }else{
              this.items = res.data
              console.log(res,this.items)
          }
      }catch(error){
          alert(error)
          console.log(error)
      }
    },
  }
}
</script>