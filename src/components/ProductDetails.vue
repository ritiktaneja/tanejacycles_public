<template>
    <v-card >
        <v-tabs
            v-model="tab"
            fixed-tabs
           
            class="transparent"
            slider-color="primary"
        >
            <v-tab>About {{product.brand.name}} Cycles </v-tab>
            <v-tab>Specifications</v-tab>
            <!-- <v-tab>Why US? </v-tab>       -->
        </v-tabs>

        <v-tabs-items
        show-arrows
        show-arrows-on-hover
        v-model='tab'>
            <v-tab-item>
              <BrandDetails :product="product"/>
            </v-tab-item>
            <v-tab-item>
                <ProductSpecifications :product="product"/>
            </v-tab-item>
            <v-tab-item>
                Comming Soon!
            </v-tab-item>

        </v-tabs-items>

    </v-card>
</template>

<script>
import BrandDetails from './BrandDetails'
import ProductSpecifications from './ProductSpecifications'

export default {
    components:{
        BrandDetails,
        ProductSpecifications,
       
    },
    props : {
        product : {
            type : Object,
            required:true
        }
    },
    data : function(){
        return {
            tab:0,
           
        }
    }
}
</script>

