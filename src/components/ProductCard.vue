<template>
<v-hover  v-slot:default="{ hover }"
        open-delay="200">
     
    <v-card 
     
      class="px-3 grey lighten-4  "
      max-width="375"
      :elevation="hover ? 16 : 2"
     
    >
    <v-img
    contain
      @click="$router.push({name:'Product',params:{id:product.id}})"
        v-if="product.images[0]"
       :src="($store.state.BACKENDBASE+product.images[0])"
      height="200px"
      class="justify-center align-center text-center"
    >
     <span v-if="!product.in_stock" class="grey font-weight-bold pa-1 red--text lighten-5  ">OUT OF STOCK</span>
    </v-img>
    <v-img   @click="$router.push({name:'Product',params:{id:product.id}})" height="200px" class="text-center justify-center align-center black" v-else lazy-src="@/assets/bicycle.png">
                <span class="grey lighten-5  "> Picture Unavailable</span>
                </v-img>

   
    
    <v-card-text  style="position:relative;" class="py-5 black--text" :class="{'grey--text':!product.in_stock}">

         <a :href="'whatsapp://send?text=Check out this amazing bicycle available at Taneja Cycle Works! Visit the link : https://tanejacycles.com/product/'+product.id">
         <v-btn  v-if="$vuetify.breakpoint.smAndDown"
                  class="green lighten-1"
                  fab
                  dark
                  small
                  absolute
                  top 
                  right
                >
                 <v-icon>mdi-whatsapp</v-icon>
                </v-btn>
                </a>

        <v-row class="mx-0" align="center"  @click="$router.push({name:'Product',params:{id:product.id}})">
          
        
          <span class="text-h6 font-weight-light ">{{product.brand.name}}</span>
          <span class="text-h6  ml-2 font-weight-bold">{{product.name}}</span>
          
          <v-spacer></v-spacer>

           <!-- <v-rating
          :value="product.rating"
          color="amber"
         small
          dense
          half-increments
          readonly
          size="22"
        ></v-rating> -->
       
        </v-row>
       
        <div class="py-2">
            <span class="text-h5 primary--text font-weight-bold">&#8377; {{product.price}}</span>
            <span class="mx-3 text-decoration-line-through text-h6  "> &#8377; {{product.mrp}}</span> 
        </div>
        <div>
          <v-chip color="warning" small denses class="mr-1" v-for="l in ['Genuine Product']" :key="l">{{l}}</v-chip>
          <v-chip small dense class="mr-1" color = "success" v-if="product.on_sale">On Sale</v-chip>
          <v-chip small dense color = "primary"  v-if="product.featured">Featured</v-chip>
        </div>
      
        <v-divider class="my-2"></v-divider>  
        <div class="text-capitalize">
          <span>Age Group/Wheel Size : {{product.ageGroup || product.wheel_size}}</span> <br>
          <span> Colors Available : {{product.color.join(',')}} </span> <br>
          <span> Speed : {{product.speed}}  </span>
         
        </div>
        
        <div class="my-2">
        <span class="font-italic">  {{product.description}} </span>
      </div>
    </v-card-text>

    <v-snackbar
      v-model="snackbar"
      timeout="500"
      color="primary"
    >
      {{product.brand}} {{product.name}} Added to Cart!
      
    </v-snackbar>

  </v-card>
</v-hover>
</template>

<script>
export default {
props : {
    product : {
        type:Object,
        required:true
    }
},
data : function(){
    return {
        show:false,
        snackbar:false,
    }
},
methods : {
  addToCart()
  {
    this.$store.commit('ADD_TO_CART',this.product)
    this.snackbar=true

  }
}
}
</script>

