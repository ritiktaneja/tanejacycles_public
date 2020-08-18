<template>
<v-card flat class="overflow-hidden grey lighten-5">
    <v-app-bar
    color="transparent"
     dense
     flat>
     <v-row fluid  class="">    
       
        <CompanyLogo/>
        <v-spacer></v-spacer>

       <div class="mt-1 pt-0 d-flex align-self-center ml-auto  overline">
         <v-btn small text>  <span class="mx-2"><v-icon class="mr-1" small>mdi-shopping</v-icon>Track Order</span></v-btn>
         <v-btn @click="$router.push({name:'ContactUs'})" small text>   <span><v-icon class="mr-1">mdi-face-agent</v-icon>Support</span></v-btn>
       </div>

     </v-row>
     
    </v-app-bar>

    <v-row class="mx-auto py-1 d-flex align-center">
      
        <ProductBrowser/>
            <ProductSearchBar/>
         <v-spacer></v-spacer>
         <CartIcon/> 
      
     </v-row>
  
</v-card>
</template>
<script>
import CompanyLogo from '../components/CompanyLogo'
  import CartIcon from '@/components/CartIcon'
import ProductBrowser from '../components/ProductBrowser'
import ProductSearchBar from '../components/ProductSearchBar'
export default {
    components :{
        CompanyLogo,
        CartIcon,
        ProductBrowser,
        ProductSearchBar
    }
}
</script>
<style lang="scss" scoped>

</style>