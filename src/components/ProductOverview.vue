<template>
    <v-container class="pt-0" grid-list-xs>
        <span class="overline"></span>
        <v-row>
            <v-col md="7" class="">
                
                <v-card class="transparent pb-2" flat>
                    <div class="headline py-0 "><span>{{product.brand.name}}</span> <span class="font-weight-bold">{{product.name}}</span></div>
                    <div class="font-weight-light caption">{{product.brand.name}} | Wheel Size  {{product.wheel_size}} |  {{product.speed}}</div>
                    
                </v-card>
                 <v-carousel
                  ref="carousel"
                 
                 :height="$vuetify.breakpoint.xs?'285px':''"
                 >

                    <v-carousel-item
                    v-for="(item,i) in product.images"
                    :key="i"
                    >
                    .
                     <v-img max-height="550" :loading="true" :key="item" lazy-src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/82614c38823695.5770ea557a3a8.gif" contain  :src="$store.state.BACKENDBASE+item"/>
                     

                       
                    </v-carousel-item>
                </v-carousel>
                
            </v-col>
            <v-col class="">
         
            <div class="overline d-flex justify-space-between">Product Id: {{product.id}}
            </div>
                <div class="my-3 d-flex justify-space-between align-center">
                   <div class="d-flex align-center">
                    <span :class="{'text-h5':$vuetify.breakpoint.smAndDown}" class="primary--text text-h4 font-weight-bold"> &#8377; {{product.price}}</span>
                    <span :class="{'text-h9':$vuetify.breakpoint.smAndDown}" class="ml-3 secondary--text text-h8 font-weight-bold text-decoration-line-though"> MRP  : &#8377; {{product.mrp}}</span>
                 
                   </div>
                       <a style="text-decoration:none;" :href="'whatsapp://send?text=Check out this amazing bicycle available at Taneja Cycle Works! Visit the link : https://tanejacycles.com/product/'+product.id">
                <v-btn  
                class="green lighten-1"
                 v-if ="$vuetify.breakpoint.mdAndDown"  
                fab
                small
                dark
                right
                  
                >
                 <v-icon>mdi-whatsapp</v-icon>
                 
                 
                </v-btn>
                </a>
                   <div class="">
                         <!-- <v-rating
                            :value="product.rating"
                            color="amber"
                            class="ml-auto "
                            dense
                            half-increments
                            readonly
                            size="18"
                            ></v-rating> -->
                            <!-- <v-btn small color="primary" text>View All Reviews!</v-btn> -->
                   </div>
                </div>
                <v-divider class="my-2"></v-divider>
                    <div>
                        <div class="body-1 font-italic py-5">{{product.description}}</div>
                        <div class="body-1 d-flex justify-space-between">
                            <div>
                            Age Group :<span class="font-weight-bold"> {{riderDetails.riderAge}} </span> <br>
                            Suitable Height :<span class="font-weight-bold"> {{riderDetails.riderHeight}} </span>
                            </div>
                            <div class="body-2 primary--text">
                                <SizeChart/>
                              
                            </div>
                        </div>
                         <div v-for="(o,index) in offers" :key="index"> 
                             <span class=" body-2 ma-0 pa-0"> {{o}}</span>
                        </div>
                    </div>
                    
                    <!-- <v-select class="mt-5"
                        :items="product.colors"
                        v-model="selectedColor"
                        label="Select Color"
                    ></v-select> -->

                     <!-- <ProductVariables  v-on:colorSelected="(value)=>{selectedColor=value}"  :product="product"/>  -->


                    
                    <v-form class="mt-5" ref='form' @submit.prevent=""> 
                        <v-row class="mx-auto">
                        
                            <v-select
                            v-if="typeof product.color =='object'"
                                :items="product.color"
                                v-model="selectedColor"
                                outlined
                                dense
                                :rules="[v=>!!v||'Please select a color']"
                                label="Select Color"
                            ></v-select>

                            
                        </v-row>
                    </v-form>




                    <div v-if="product.in_stock" class="my-3   d-flex justify-space-around">
                        <v-btn tile color="amber" @click="addToCart(true)"> <v-icon>mdi-cart-outline</v-icon> Buy Now!</v-btn>
                        <v-btn color="primary" v-if="!addedToCart" @click="addToCart(false)" outlined tile> <v-icon>mdi-cart</v-icon> Add To Cart</v-btn>
                        <v-btn color="success" v-else @click="$router.push({name:'Checkout'})"  tile> <v-icon>mdi-cart</v-icon> Checkout</v-btn>
                    </div>
                    <div v-else class="d-flex justify-center ">
                        <div>
                            <v-btn class="center" color="secondary" text> Currently Unavailable</v-btn>
                            <br>
                            <span class="mx-auto">
                                <a style="text-decoration:none;" :href="'https://api.whatsapp.com/send?phone=916396843575&text=When can  '+product.brand.name+' '+product.name+' be available? Found it at https://tanejacycles.com/products/'+product.id"> <span class="body-1 justify-center"><v-icon color="success">mdi-whatsapp</v-icon> Enquire about this product</span></a>
                            </span>
                        </div>
                    </div>
                    
                    <PincodeChecker class="mx-auto"/>


                   
                    <div class="text-center" >
                       <a :href="'https://api.whatsapp.com/send?phone=916396843575&text=I am looking to buy '+product.brand.name+' '+product.name+' available at https://tanejacycles.com/product/'+product.id"> <span class="title">Have Doubts ? <br><v-icon color="success">mdi-whatsapp</v-icon> We are just a text away!</span></a>
                    </div> 

            </v-col>
        </v-row>
        <v-snackbar
            v-model="snackbar"
            timeout="500"
            color="primary"
             class="center"
        >
             {{product.brand.name}} {{product.name}} Added to Cart!
          
        </v-snackbar>
    </v-container>    
</template>

<script>
//import ProductVariables from '../components/ProductVariables'
import PincodeChecker from '../components/PincodeChecker'
import SizeChart from '../components/SizeChart'
export default {
    props : {
        product : {type: Object, required:true},
        
    },
    components:{
        //ProductVariables,
        PincodeChecker,
        SizeChart
    },
    data: function() {
        return {
            selectedColor : "",
            offers : [  'Fully Fitted, Ready to Ride - delivered to your doorstep. No assembly required',
                        'Pre delivery Quality Check by Experts.',
                        'Free Shipping*',
                        '1 Free Accessories worth ₹150 View Offers',
                       ],
             snackbar:false,
             addedToCart:false,
             riderDetails : ""
       }
    
    },
    methods : {
        addToCart(goToCheckout){
            if(!this.$refs.form.validate())
            return false
           
            var p = {...this.product}
            p.color = [this.selectedColor]
            this.$store.commit('ADD_TO_CART',p)
            this.snackbar=true
            this.addedToCart = true
            if(goToCheckout)
            this.$router.push({name:'Checkout'})
        },
       
    },
   mounted () {
       this.riderDetails = this.$store.state.SizeChart(this.product.wheel_size)
    }
    
}
</script>

