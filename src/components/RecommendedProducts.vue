<template>
<v-container v-if="similarProducts.length" grid-list-xs  fluid class="grey lighten-3 mt-5 pa-5">
   
        <span class="title text-center center" ><v-icon large color="orange" v-if="title=='Products On Sale'">mdi-sale</v-icon> {{title}} </span>
   
     <v-row class="mx-auto" v-if="loading" >
            <v-col   v-for='i in 4' :key="i">
              <v-skeleton-loader
                class="mx-auto"
                max-width="375"
                width="375"
                type="card"
                ></v-skeleton-loader>
                </v-col>
        </v-row>
    <v-row class="mx-auto" v-else>
            <v-col  md="3" sm="6" xs="6" v-for="(item,i) in similarProducts" :key ="i"  >
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
                <span class="primary--text font-weight-bold">
                  &#8377;  {{item.price}}
                  </span>
                  <span class="text-decoration-line-through">   
                  &#8377;  {{item.mrp}}
                  </span>    
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
      title : String,
      urlq : {type: String, default : ""} 
    },
    data:function(){
        return {
            similarProducts : [
            ],
            loading:false
        }
    },
    mounted (){
        this.loading=true
        axios.get(this.$store.state.BACKENDURL+'bicycles/?'+this.urlq)
        .then(response=>{
         
            
            response.data = response.data.filter((x,index)=>{
                return index<12
            })
         
            this.similarProducts = response.data
           
        })
        .catch(e=>{
            this.$store.commit('ERROR_OCCURRED',e)
        })
        .finally(()=>{
            this.loading=false
        })
    }

}
</script>