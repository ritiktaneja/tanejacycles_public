<template>
   
    <!-- <div @click="$router.push({name:'Checkout'})">
        <v-badge right :dot="cart.length==0" :content="cart.length" color="primary">
              <v-icon color="primary">{{cartIcon}}</v-icon>
        </v-badge>
    </div> -->
     <v-menu open-on-hover close-on-click fixed :offset-y="true"   transition="slide-x-transition">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
        text
          color="primary"
          class="ma-2"
          v-bind="attrs"
          v-on="on"
        >
        <v-badge right :dot="cart.length==0" :content="cart.length" color="primary">
              <v-icon color="primary">{{cartIcon}}</v-icon>
        </v-badge>
        </v-btn>
      </template>

    <v-card
    class="mx-auto"
    max-width="344"
    outlined
    v-for="(product,index) in cart" :key="index"
   
  >
    <v-list-item class="text-capitalize" three-line>
      <v-list-item-content  @click="$router.push({name:'Product',params:{id:product.id}})">
        <div class="overline">{{product.id}}</div>
        <v-list-item-title class="pa-0 ma-0 h6">{{product.brand.name}} {{product.name}}</v-list-item-title>
        <v-list-item-subtitle class="ma-0 pa-0">{{product.wheel_size}} | {{product.color[0]}} </v-list-item-subtitle>
        </v-list-item-content>

      <v-list-item-avatar
        tile
        size="80"
      >
        <v-img    v-if="product.images[0]"  contain class="black--text " :src="($store.state.BACKENDBASE+product.images[0])">         
        </v-img>
        <v-img   height="200px" class="text-center justify-center align-center black" v-else lazy-src="@/assets/bicycle.png">
        <span class="grey lighten-5  "> Picture Unavailable</span>
        </v-img>
      </v-list-item-avatar>
    </v-list-item>

    <v-card-actions class="my-0 py-0">
    <span class="" style="text-decoration:line-through;"> &#8377; {{product.mrp}}</span>
    <span class="font-weight-bold mx-2"> &#8377; {{product.price}}</span>
        <v-spacer></v-spacer>
    <v-btn text small @click="removeProduct(product)" color="transparent"> <v-icon color="red">mdi-delete</v-icon> </v-btn>
    </v-card-actions>
  </v-card>
  <v-card max-width="344" width="344" flat dense class="pa-2">
    <div v-if="cart.length" class="text-center">
        <v-btn small :to='{name:"Checkout"}' color="primary" tile>Proceed to Checkout <v-icon small>mdi-arrow-right</v-icon></v-btn>
    </div>
    <div v-else class="title  ma-5 text-center font-italic ">
      <v-icon color="red" large>mdi-emoticon-sad-outline</v-icon>
      Your cart is empty!
    </div>
  </v-card>
    </v-menu>
    
</template>

<script>
export default {
    props : {
       
    },
    data : function(){
        return{
             cartIcon : "mdi-cart",
            
        }
    },
    computed : {
         cart : function()  {return  this.$store.state.cart }
    },
    methods : {
        removeProduct(product)
        {
            this.$store.commit('REMOVE_FROM_CART',product)   
        },
       
    },
    watch : {
      
    }
    
}
</script>

<style lang="scss" scoped>

</style>