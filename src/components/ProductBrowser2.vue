<template>
<v-row flat class="mx-auto align-center transparent">
    
    <v-col cols="12" md="5" lg="5" class="d-flex justify-space-around" >
       
        <v-btn
          color="primary"
          class=""
          small
          text
          @click="$router.push({name:'Catalog'})"
        >
         All Bicycles
        </v-btn>
     
       <v-btn
          color="primary"
          class=""
          small
          text
        
          @click="$router.push({name:'Catalog',params:{category:'mountain'}})"
        >
         MTB
        </v-btn>
          <v-btn
          color="primary"
          class=""
          small
          text
          @click="$router.push({name:'Catalog',params:{category:'road'}})"
        >
          Road Bikes
        </v-btn>
           <v-btn
          color="primary"
          class=""
          small
          text
          @click="$router.push({name:'Catalog',params:{category:'kids'}})"
        >
          Kids
        </v-btn>
         <!-- <v-btn
          color="primary"
          class=""
          small
          text
          @click="$router.push({name:'Catalog',params:{category:'electric'}})"
        >
          Electric Bikes
        </v-btn> -->
    </v-col>
     
    <v-col cols="12" md="4" lg="4" class="d-flex blue align-center lighten-5 justify-space-around">

         <v-btn color="primary" small text @click="$router.push({name:'Catalog',query:{brand__name:'hero'}})">
          Hero Cycles
        </v-btn>
          <v-btn color="primary" class="" small text @click="$router.push({name:'Catalog',query:{brand__name:'lectro'}})" >
          Lectro Bikes
        </v-btn>
  
        <!-- <v-btn color="primary" class="" small text @click="$router.push({name:'Catalog',query:{brand__name:'kross'}})" >
          Kross Cycles
        </v-btn>
         -->
  
    
    </v-col>

<v-col cols="12" md="3" lg="3" class="d-flex justify-center  align-center"  >
    <v-btn x-small tile class="mx-2"  color="indigo white--text"  @click="$router.push({name:'Catalog',query:{featured:true}})">New Products</v-btn>
    <v-btn tile x-small  @click="$router.push({name:'Catalog',query:{on_sale:true}})"  class="mx-2 my-1" color="amber">
      <v-icon small>mdi-sale</v-icon>
      Clearance Sale!
      </v-btn>
</v-col>
 
  
        
</v-row>
</template>

<script>
export default {
    components: {
      
    }
}
</script>

<style lang="scss" scoped>

 
</style>
