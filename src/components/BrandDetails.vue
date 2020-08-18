<template>
  <v-card>
        <v-container grid-list-xs>
            <v-row>  
                <v-col md="4" >
                   
                    <v-img v-if="brand.logo" fluid contain :src="($store.state.BACKENDBASE+brand.logo)"> </v-img>   
                </v-col>
                <v-col sm="12" md="8">   
                    {{brand.desc}}
                </v-col>
            </v-row>
        </v-container>
    </v-card>

</template>


<script>
export default {
    props : {
        product:{
            type:Object,
        },
        
    },
    computed:{
        brand()
        {
            return this.product.brand
        }
    }
    
}
</script>