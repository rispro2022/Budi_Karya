<template>
    <nav>
        <v-app-bar app color="#6f6f6f">
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-btn icon :to="routeHome" class="mr-2">
                <v-icon>mdi-home</v-icon>
            </v-btn>
            <v-img 
                max-height="50"
                max-width="50" 
                src="../assets/itb.png"
                class="mx-2">
            </v-img>
            <v-img 
                max-height="70"
                max-width="70" 
                src="../assets/lpdp.png"
                class="mr-3">
            </v-img>
            <v-img 
                max-height="70"
                max-width="70" 
                src="../assets/inka.png"
                class="mb-1 mr-4">
            </v-img>
            <v-spacer></v-spacer>
            <span class="font-weight-light white--text ">Welcome,</span>
            <span class="white--text mr-6">tools</span>
            <v-btn @click="logout()" color="grey">
                <span>Sign Out</span>
                <v-img src="../assets/logo/arrow-right.png"></v-img>
            </v-btn>
        </v-app-bar>

        <v-navigation-drawer app v-model="drawer" color="#555555" width="22%">
            <v-list>
                <v-list-group
                    v-for="item in items"
                    :key="item.title"
                    v-model="item.active"
                    >
                    <template v-slot:activator>
                    <v-list-item-action>
                        <v-icon class="white--text">{{item.action}}</v-icon>
                    </v-list-item-action>
                    
                    <v-list-item-content>
                        <v-list-item-title class="white--text">{{item.title}}</v-list-item-title>
                    </v-list-item-content>
                    </template>

                    <v-list-item
                    v-for="child in item.items"
                    :key="child.title"
                    :to="child.route"
                    >
                        <v-list-item-action>
                            <v-icon class="white--text ml-6">{{child.icon}}</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title class="white--text">{{child.title}}</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-group>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>
import Login from "../services/Login.js"
export default {
    data(){
        return {
            loginService: new Login(),
            route: "/login",
            routeHome: "/",
            drawer: false,
            items: [
                {
                action: 'mdi-wrench',
                active: false,
                items: [
                    { title: 'Daftar Kotak Perkakas', icon: 'mdi-filter-variant', route: '/showToolBox'},
                    { title: 'Kotak Perkakas', icon: 'mdi-plus', route: '/addToolBox'},
                    { title: 'Jenis Perkakas Consumable', icon: 'mdi-plus', route: '/addToolTypeConsume'},
                    { title: 'Jenis Perkakas Non Consumable', icon: 'mdi-plus', route: '/addToolTypeNonConsume'},
                    { title: 'Pembelian Perkakas', icon: 'mdi-plus', route: '/purchaseTools'},
                    {title : 'Daftar Pembelian Perkakas', icon : 'mdi-filter-variant', route : '/listPurchaseTools'},
                    {title : 'Daftar Stok Perkakas', icon : 'mdi-wrench', route : '/listToolStock'}
                        //{title : 'List Purchase Tool Item',icon : 'mdi-gavel',route : '/listPurchaseToollItem/:id'}
                ],
                title: 'Penambahan Item Perkakas',
                },

                {
                    action: 'mdi-wrench',
                    active: false,
                    items: [
                    { title: 'Pencarian Posisi Perkakas', icon: 'mdi-filter-variant', route: '/searchToolPosition'},
                  
                ],
                    title : "Pencarian Perkakas"
                },

                {
                    action: 'mdi-wrench',
                    active: false,
                    items: [
                    { title: 'Kebutuhan Pengadaan Perkakas', icon: 'mdi-filter-variant', route: '/addPengadaanTools'},
                  
                ],
                    title : "Pengadaan Perkakas"
                },
                
                {
                    action: 'mdi-wrench',
                    active: false,
                    items: [
                    { title: 'Pengiriman Perkakas', icon: 'mdi-filter-variant', route: '/chooseKebutuhanTool'},
                  
                ],

                    title : "Distribusi Perkakas"

                },

               
                {
                    action: 'mdi-wrench',
                    active: false,
                    items: [
                    { title: 'Peminjaman Perkakas', icon: 'mdi-filter-variant', route: '/addPeminjamanTools'},
                    {title : 'Pengembalian Perkakas', icon : 'mdi-filter-variant', route : '/listPengembalian'}
                  
                ],
                    title : "Peminjaman dan Pengembalian Perkakas"
                },

             
                



              

              
           




            ],
        }
    },

    methods: {
        logout() {
            this.route = "/login"
            location.replace("/login")
            this.loginService.removeUserType()
        }
    },
}
</script>

<style>
    .v-navigation-drawer__content::-webkit-scrollbar-track{
        -webkit-box-shadow: inset 0 0 6px #5d5d5d;
        background-color: #5d5d5d;
    }
    .v-navigation-drawer__content::-webkit-scrollbar{
        width: 0px;
    }
    .v-navigation-drawer__content::-webkit-scrollbar-thumb{
        -webkit-box-shadow: inset 0 0 6px #424242;
        background-color: #424242;
    }
    #border{
        border-radius: 50%;
    }
</style>