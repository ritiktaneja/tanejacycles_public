<template>
    <v-container fluid class="grey lighten-4 ">
        <div v-if="product || loading">
        <div class="ma-0 pa-0 overline mb-0 pb-0">
              <v-breadcrumbs divider="/" :items="breadcrumbs">
                <template v-slot:divider>
                    <v-icon>mdi-chevron-right</v-icon>
                </template>
            </v-breadcrumbs>
        </div>
        <ProductOverview v-if="product" :product="product"/>
        <ProductDetails v-if="product" :product="product"/>
        <SimilarProducts v-if="product" :product="product"/>
        
        </div>
        <v-card v-else flat height="250" class="d-flex align-center text-center justify-center grey lighten-1">
            <div>
            <v-icon color="yellow" class=" text-center darken-5" x-large>mdi-alert-outline</v-icon> <br>
             <span class="headline "> The link you're trying to access is either temporary unavailable or broken.</span>
             <br>
             <router-link :to="{name:'Home'}"><span class="primary--text"> Click here to return to Homepage </span></router-link>
            </div>
        </v-card>
    </v-container>

</template>
<script>
import ProductOverview from '../components/ProductOverview'
import ProductDetails from '../components/ProductDetails'
import SimilarProducts from '../components/SimilarProducts'

import axios from 'axios'

export default {
    components : {
        ProductOverview,
        ProductDetails,
        SimilarProducts
    },
    data : function(){
        return {
           // product :{id:'7504', images:[require('@/assets/bicycle.jpg'),require('@/assets/bicycle.jpg'),require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['Red with Black Graphics','Green']},
            product:null,
            productid:this.$route.params.id,
            loading:false,
        }
    },
    computed : {
         breadcrumbs() {
             var ref =this
            if(this.product)
            return  [
                        {
                            text:'Home',
                           
                             to : {path:'/'}
                        },
                        {
                            text:'Bicycles',
                            to : {path:'/',name:'Catalog'}
                        },
                        {
                            text:ref.product.brand.name + " "+ref.product.name,
                            disabled:false,
                        }
            ]
            else 
            return [{
                            text:'Homepage',
                           
                             to : {path:'/'}
                        },
                        {
                            text:'Bicycles',
                            to : {path:'/',name:'Catalog'}
                        },
                    ]
        }
    },
    created(){
        this.getProductDetails()
    },
    methods : {
        getProductDetails(){
           this.loading = true
            axios.get(this.$store.state.BACKENDURL+'bicycles/'+this.$route.params.id+'/')
            .then(response=> {
              
                this.product = response.data
            })
            .catch(e=>{
                console.log('Error occured while loading catalog : '+e)
                this.$store.commit('ERROR_OCCURRED',e)
            })
            .finally(()=>{
                this.loading = false
            })
        }
    },
    watch: {
        productid()
        {
            this.getProductDetails()
        }
       
    }
    
}
</script>