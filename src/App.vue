<template>
  <v-app fluid>
    

    <NavigationBar/>
    <v-menu-transition>
   <router-view :key="$route.fullPath"/>
    </v-menu-transition>
   <Footer/>
  </v-app>
</template>

<script>

import Footer from '@/components/Footer'
import NavigationBar from '@/components/NavigationBar2.vue'

export default {
  name: 'App',
  components: {
    NavigationBar,
    Footer
  },

  metaInfo(){
    return {
        title : 'Taneja Cycles - Great Brands at Wholesale prices',
        meta : [
          {
            name : 'description',
            content : " Taneja Cycle Works is the leading wholesaler and retailer in the cycling world in Uttrakhand since 1962. We, at Taneja Cycles believe more in building relations with our customers rather than just dealing with them, and 'take pride in their ride'."
          },
          {
            name : 'robots',
            content : 'index, follow'
          },
          {
            property:'og:title',
            content : 'Homepage - Taneja Cycles'
          },
          {
            property:'og:site_name',
            contenr:'Taneja Cycles'
          },
         
          
        ]
    }
  },

  data: () => ({
    //
  }),
  mounted (){
    if(localStorage.cart)
    this.$store.commit('UPDATE_CART_ON_LOAD',JSON.parse(localStorage.cart))
  }
};
</script>
