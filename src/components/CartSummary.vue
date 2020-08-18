<template>
   <v-card flat class="text-center">
        <v-row>
            <v-spacer></v-spacer>
            <v-btn color="primary" :disabled="this.cart.length==0" @click="stepCompleted()" text>Next</v-btn>
        </v-row>
      <span class="mt-0 pt-0 headline  text-center font-weight-light">Cart Summary</span>
       <v-divider width="60%" class="mx-auto my-2"></v-divider>
      <div v-if="!cart.length" class="mt-3 orange pa-5 lighten-4"> <span class="title ">Your Cart is Empty!</span> <br>
       <router-link :to='{name:"Catalog"}'>Click here to browse items </router-link> 
      </div>

        <v-row class="mx-auto" v-for="(product,index) in cart" :key="index">
            <v-col md="4" @click="$router.push({name:'Product',params:{id:product.id}})">
                <v-img v-if="product.images[0]" contain :src='$store.state.BACKENDBASE+product.images[0]'/>
                 <v-img    class="text-center justify-center align-center black" v-else lazy-src="@/assets/bicycle.png">
                <span class="grey lighten-5  "> Picture Unavailable</span>
                </v-img>
            </v-col>
            <v-col>
                <v-row>
                    <span class="overline"> Product Id :{{product.id}}</span>
                </v-row>
                <v-row class="d-flex align-center" >
                        <span class="font-weight-light headline">{{product.brand.name}}</span>
                        <span class="ma-1 font-weight-bold headline">{{product.name}}</span>
                       
                        <span class="ml-auto mr-5 justify-self-end font-weight-light ">Size : {{product.wheel_size}}</span>
                </v-row>
                <v-row class="d-flex align-center">
                        <span class="font-weight-bold headline primary--text"> &#8377; {{product.price}}</span>
                        <span class="ml-3 font-weight-light text-h7 secondary--text">  MRP : &#8377; {{product.mrp}}</span>
                          <span class="ml-auto mr-5 justify-self-end font-weight-light ">Color : {{product.color[0]}}</span>
                </v-row>
                 <v-row class="d-flex align-center">
 
                        <span class="font-italic text-h8 secondary--text">  {{product.desc}}</span>
                          <span class="ml-auto mr-5 justify-self-end font-weight-light "><v-btn @click="removeProduct(product)" text>  <v-icon color="red">mdi-trash-can</v-icon> </v-btn></span>
                </v-row>
            </v-col>
        </v-row>
        <v-row class="mx-auto caption">Note: ALL PICTURES SHOWN ARE FOR ILLUSTRATION PURPOSE ONLY.ACTUAL PRODUCT MAY VARY DUE TO PRODUCT ENHANCEMENT.</v-row>
        <AddAccessories/>
        <v-row>
            <v-spacer></v-spacer>
            <v-btn color="primary" :disabled="this.cart.length==0" @click="stepCompleted()" text>Next</v-btn>
        </v-row>
    </v-card>
</template>

<script>
import AddAccessories from './AddAccessories'
export default {
    components:{
        AddAccessories
    },
    computed : {
        cart(){
            return this.$store.state.cart
        }
    },
    methods : {
        removeProduct(obj){
            this.$store.commit('REMOVE_FROM_CART',obj)
        },
        stepCompleted(){
            this.$emit('stepCompleted')
        }
    }
}
</script>