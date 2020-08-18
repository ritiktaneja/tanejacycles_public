<template>
<v-row flat class="d-flex justify-space-around align-center transparent">
    
    <v-col offset-md="1">
     <v-menu :nudge-width="500" open-on-hover offset-y bottom >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          class=""
          small
          text
          v-bind="attrs"
          v-on="on"
          @click="$router.push({name:'Catalog'})"
        >
          Bicycles
        </v-btn>
        
      </template>
       
           <BicycleSearchCategory/>
        
    </v-menu>
  
     <v-menu :nudge-width="500" open-on-hover offset-y bottom >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          class=""
          small
          text
          v-bind="attrs"
          v-on="on"
        >
          Accessories
        </v-btn>
        
      </template>
       
           <AccessoriesSearchCategory/>
        
    </v-menu>
    </v-col>

<v-col>
    <v-btn small tile class="mx-2"  color="indigo white--text"  @click="$router.push({name:'Catalog'})">New Products</v-btn>


    <v-btn tile small  class="mx-2 my-1" color="amber">
      <v-icon>mdi-sale</v-icon>
      Clearance Sale!
      </v-btn>
</v-col>
 
  
        
</v-row>
</template>

<script>
import BicycleSearchCategory from '../components/BicycleSearchCategory'
import AccessoriesSearchCategory from '../components/AccessoriesSearchCategory'
export default {
    components: {
        BicycleSearchCategory,
        AccessoriesSearchCategory
    }
}
</script>

<style lang="scss" scoped>

 
</style>
