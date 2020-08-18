<template>
<v-card class="grey lighten-5" flat>
   
     
        <v-row >
             <v-col order-md="last" class="col-12 col-md-4" > 
                <OrderSummary/>
            </v-col>
            <v-col class="col-lg-8 col-md-12 col-12">
                  <CheckoutStepper/>
            </v-col>
           

        </v-row>
   
</v-card>
</template>

<script>
import CheckoutStepper from '../components/CheckoutStepper'
import OrderSummary from '../components/OrderSummary'
export default {
    components:{
        CheckoutStepper,
        OrderSummary
    }
    
}
</script>