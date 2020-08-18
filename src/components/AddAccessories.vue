<template>
<v-container grid-list-xs  fluid class="grey lighten-3 mt-5 pa-5">
   
        <span class="title text-center center">Add Accessories</span>
   
    <v-row>
            <v-col  cols="6" sm="6" md="3" v-for="(item,i) in similarProducts" :key ="i">
                <v-card light  @click="addToCart(item)">
                <v-img v-if="item.images[0]" contain class="black--text " :src="$store.state.BACKENDBASE+item.images[0]">         
                </v-img>
                 <v-img  class="text-center justify-center align-center black" v-else lazy-src="@/assets/bicycle.png">
                <span class="grey lighten-5  "> Picture Unavailable</span>
                </v-img>
                <v-card-subtitle>
                        {{item.brand.name}} {{item.name}}
                </v-card-subtitle>
                <v-card-subtitle>
                  &#8377;  {{item.price}}
                </v-card-subtitle>
                
                </v-card>
            </v-col>
            </v-row>
    </v-container>
</template>

<script>
import axios from 'axios'
export default {
    props : {
       
    },
    data:function(){
        return {
            similarProducts : [
            ]
        }
    },
    mounted (){
        axios.get(this.$store.state.BACKENDURL+'bicycles/?category=access')
        .then(response=>{
         
           
            response.data = response.data.filter((x,index)=>{
                return index<8
            })

            this.similarProducts = response.data
            
        })
    },
    methods :{
        addToCart(product)
        {
            this.$store.commit('ADD_TO_CART',product)
        }
    }

}
</script>