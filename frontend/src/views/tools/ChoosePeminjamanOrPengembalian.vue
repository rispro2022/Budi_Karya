<template>
    <v-card
      class="mx-auto text-center mt-10 mb-10"
      max-width="1150"
      height = "400">
      <h1>Peminjaman dan Pengembalian Perkakas</h1>
      <div class="d-flex"> 

          <div class="mx-auto text-center">
  <router-link to="/chooseWorkstation">
    <v-btn
    class="text-center ma-2  mt-15 mb-5"
    color="secondary"
    width = "250"
    height = "100"
  
  >
    Pengembalian Perkakas
  </v-btn>

  </router-link>      
  

  <v-btn
    color="blue-grey"
    class="text-center ma-2 mt-15 mb-5 white--text"
    width = "250"
    height = "100"
  
  >
    Peminjaman Perkakas

  </v-btn>

      </div>
      </div>
             
      </v-card>

</template>