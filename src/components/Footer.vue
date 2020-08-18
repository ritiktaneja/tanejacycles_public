<template>
    <v-card class="grey center lighten-3 ma-0 pa-0" outlined flat>
        <v-container class="" fluid grid-list-xs>
          
              
            <CompanyLogo/>
               
                <v-row>
               <v-col class="" md="4" xs="12" sm="12" >
                <div class="ma-3"> <router-link :to='{name:"ContactUs"}'> ContactUs </router-link> </div>
                <div  class="ma-3"><router-link  :to='{name:"PrivacyPolicy"}'> Privacy Policy </router-link> </div>
                <div class="ma-3"> <router-link :to='{name:"TermsAndConditions"}'>  Terms And Conditions </router-link> </div>
                <div class="ma-3"> <router-link :to='{name:"ReturnPolicy"}'>  Return Policy </router-link> </div>
                <div class="ma-3"> <router-link :to='{name:"AboutUs"}'> About Us </router-link> </div>
             
           
               </v-col>
               <v-col>

            <div md="4" class=" text-right mr-3" xs="12" sm="12">
                <span class="font-weight-bold">Registered Office:</span>
                <br>
                <span> 1 Turner Road </span>      
                <br>             
                <span> Clement Town, Dehradun  </span>
                <br>
                <span>(Uttrakhand) <br> Pincode - 248001</span> 
            </div>
               </v-col>
           </v-row>
           
        </v-container>
        <v-container class="font-weight-light text-center" grid-list-xs>
            Copyright 2020.
        </v-container>
    </v-card>
</template>

<script>
import CompanyLogo from './CompanyLogo'
export default {
    components:{
        CompanyLogo
    }
}
</script>

<style scoped>
    .router-link {
        text-decoration: none !important;
    }
</style>