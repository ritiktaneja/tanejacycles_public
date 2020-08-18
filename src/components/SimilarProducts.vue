<template>
<v-container grid-list-xs v-if="similarProducts.length"  fluid class="grey lighten-3 mt-5 pa-5">
   
        <span class="title text-center center">Similar Products</span>
   
    <v-row>
            <v-col md="3" sm="6" xs="6" v-for="(item,i) in similarProducts" :key ="i">
                <v-card light  @click="$router.push({name:'Product',params:{id:item.id}})">
                <v-img   height="200px" v-if="item.images[0]"  contain class="black--text " :src="($store.state.BACKENDBASE+item.images[0])">         
                </v-img>
                <v-img   height="200px" class="text-center justify-center align-center black" v-else lazy-src="@/assets/bicycle.png">
                <span class="grey lighten-5  "> Picture Unavailable</span>
                </v-img>
                <v-card-title>
                        {{item.brand.name}} {{item.name}}
                </v-card-title>
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
        product : {
            type : Object,
            required : true,
        }
    },
    data:function(){
        return {
            similarProducts : [
            ]
        }
    },
    mounted (){
        axios.get(this.$store.state.BACKENDURL+'bicycles/?in_stock=true&wheel_size='+this.$store.state.SizeEnums[this.product.wheel_size])
        .then(response=>{
         
           
            response.data = response.data.filter((x,index)=>{

                return x.id!=this.product.id && index<8
            })

            this.similarProducts = response.data
            
        })
        .catch((e)=>{
            this.$store.commit('ERROR_OCCURED',e)
        })
    }

}
</script>