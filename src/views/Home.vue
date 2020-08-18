<template>
 <v-container class="pa-0" fluid grid-list-xs>
   <v-row class="grey  lighten-2 body-2 text--secondary mx-auto align-center d-flex justify-space-around">
     <v-col> <v-icon color="primary" small >mdi-sale</v-icon>Guaranteed Best Deals! </v-col>
     <v-col> <v-icon  color="primary"  small>mdi-spray-bottle</v-icon>Pre Delivery Sanitization </v-col>
      <v-col> <v-icon  color="primary"  small>mdi-truck-fast-outline</v-icon> Doorstep Delivery </v-col>
     <v-col> <v-icon  color="primary"  small>mdi-shield-check</v-icon>Quality Check  </v-col>
   </v-row>
<HomepageMedia/>

<RecommendedProducts title="Featured Products" urlq="featured=true&in_stock=true" />
<RecommendedProducts title="Products on Sale" urlq="on_sale=&in_stock=true" />

<HomepageBrowser class="mt-5"/>

<WhyUs/>

<CustomerReviews/>
 </v-container>
</template>

<script>
// @ is an alias to /src
import HomepageMedia from '../components/HomepageMedia'
import HomepageBrowser from '../components/HomepageBrowser'
import RecommendedProducts from '../components/RecommendedProducts'
import CustomerReviews from '../components/CustomerReviews'
import WhyUs from '../components/WhyUs'
export default {
  name: 'Home',
  components: {
    HomepageMedia,
    HomepageBrowser,
    WhyUs,
    RecommendedProducts,
    CustomerReviews
  }
}
</script>

