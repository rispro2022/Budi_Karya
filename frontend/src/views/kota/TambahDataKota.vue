<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Kota Baru</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="kode"
            :counter="3"
            :rules="kodeRules"
            label="Kode"
            required
            ></v-text-field>

            <v-autocomplete
            v-if="items"
            item-text="nama"
            item-value="code"
            v-model="negara"
            v-bind:items="items"
            :rules="[v => !!v || 'Negara is required']"
            label="Negara"
            required
            ></v-autocomplete>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

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
    
</template>

<script>
  export default {
    data: () => ({
      valid: true,
     
      nama: '',
      kode: '',
      kodeRules: [
        v => !!v || 'Kode is required',
        v => (v && v.length <= 3 && v.length >= 3) || 'Kode must be 3 characters',
      ],
      negara: undefined,
      items: [],
      snackbar: {
        show: false,
        message: null,
        color: null
      },
    }),

    mounted(){
      this.fetchData()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertKota()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.kode)
        console.log(this.nama)
        console.log(this.negara)
      },

      async fetchData(){
        try{
            const axios = require('axios');
            const res = await axios.get(`/countries/get_allcountries`);
            console.log(res)
            if(res.data == null){
                alert("Negara Kosong")
            }else{
                this.items = res.data
                console.log(this.items)
            }
        } 
        catch(error){
            alert("Error")
            console.log(error)
        }
      },

      async InsertKota(){
        try{
          const axios = require('axios');
          const response = await axios.post('/city/add_city',
            { code: this.kode,
              nama: this.nama,
              country: this.negara
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
             this.snackbar = {
              message : "Insert Kota Success",
              color : 'green',
              show : true
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Kota Gagal, Kode sudah tersedia",
              color : 'red',
              show : true
          }}
          
        }
        catch(error){
          alert("Insert Kota Failed")
          console.log(error)
          this.snackbar = {
              show : true,
              color : "red",
              message : "Insert kota error"}
        }
      },
    },
  }
</script>