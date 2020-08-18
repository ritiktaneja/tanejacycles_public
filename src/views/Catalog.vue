<template>
<div class=" d-flex grey lighten-5">

    <FilterProductDrawer  :filterDrawer="filterDrawer" v-on:filterData="filter"  v-on:closeDrawer="filterDrawer=false" />
   
    
    <v-container id="products" class=" ma-0 pa-0">
        
        <v-btn color="blue lighten-4" 
        fixed
        right
        v-if="$vuetify.breakpoint.mdAndDown"
        @click="filterDrawer=!filterDrawer"
        bottom
        fab
        >
        <v-icon>mdi-tune</v-icon>
        </v-btn>   
        <v-row class="mx-auto" v-if="this.loading" >
            <v-col   v-for='i in 4' :key="i">
              <v-skeleton-loader
             
                class="mx-auto"
                max-width="375"
                width="375"
                type="card"
                ></v-skeleton-loader>
                </v-col>
        </v-row>
        <v-row class="mx-auto d-flex align-baseline justify-center" v-if="!this.products.length">
           <v-container grid-list-xs>
                <v-card flat class="text-center pa-5">
                   There are no products to match your search! <br>
                   <router-link  class="red--text" :to="{name:'Catalog'}"><span class="text-h6 ">Click here to search more products</span></router-link>
                   <br>
                   Please change the filters or refresh this page in your browser <br>
                   Or <router-link :to="{name:'ContactUs'}" > Contact Us to enquire about products not available on our website. </router-link>

                </v-card>
             </v-container>
        </v-row>
        <v-row v-else class="mx-auto">
            
         <v-col cols="12" md="4" lg="4" xl="3" v-for="(product,index) in products" :key="index" >
           
 
            <ProductCard  class="" :product="product" />
         </v-col>
        </v-row>
    </v-container>
</div>
    
</template>

<script>
import FilterProductDrawer from '../components/FilterProductDrawer'
import axios from 'axios'
import ProductCard from '../components/ProductCard'
export default {
    components :{
        ProductCard,
        FilterProductDrawer
    },
    data : function(){
        return{
             products:[//{id:'7504', images:[require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['red','green']},
            // {id:'7504', images:[require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['red','green']},
            // {id:'7504', images:[require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['red','green']},
            // {id:'7504', images:[require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['red','green']},
            // {id:'7504', images:[require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['red','green']},
            // {id:'7504', images:[require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['red','green']},
            // {id:'7504', images:[require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['red','green']},
            // {id:'7504', images:[require('@/assets/bicycle.jpg')], name:'DTB',mrp:'5000', category:'Mountain Bike', price:'4499',rating:3.5, labels:['Best Seller','On Sale'], desc:'Most loved economical Mountain Bike',brand:'Hero',reviews:[{},{},{},{}],size:'24T',ageGroup:'12-18',colors:['red','green']},
           ],
            filterDrawer:false,
            loading:false,
            params : "",
        }
    },
    mounted (){
        this.getProducts()

        if(this.$vuetify.breakpoint.lgAndUp)
        this.filterDrawer=true
    },
    methods : {
        getProducts()
        {
            
            this.loading=true

            if(this.$route.params.category)
                this.params += 'category='+this.$route.params.category +'&'
            let q = this.$route.query;
           
            Object.keys(q).map(key=>{
                this.params+= key+'='+q[key]+'&';
            })
            let ref2 = this;
         
           axios.get(this.$store.state.BACKENDURL+'bicycles/?'+this.params)
            .then(response=>{
               
                this.products=response.data
                console.log('Products List',this.products.length,this.params)
            })
            .catch(e=>{
                console.log('Error occured while loading catalog : '+e)
                this.$store.commit('ERROR_OCCURRED',ref2.$route.path,e)
            })
            .finally(()=>{
                this.loading=false
            })
            
        },
        filter(url){
            if(this.$vuetify.breakpoint.mdAndDown){this.filterDrawer=false}
            this.params = url
            console.log(this.params)
            this.getProducts()
        }
    }
}
</script>

<style lang="scss" scoped>

#products {
   
  display: flex !important;
  flex-flow: row wrap !important;

}

</style>