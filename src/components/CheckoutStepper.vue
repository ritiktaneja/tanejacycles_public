<template>
    <v-stepper v-model="e1">
        <v-stepper-header>
            <v-stepper-step step="1"  :editable="true" :complete="e1>1">Cart Summary</v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="2" :editable="this.$store.state.cart.length>0" :complete="e1>2">Shipping Details</v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="3" :complete="e1>2">Payment Method</v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
            <v-stepper-content step="1">
                <CartSummary v-on:stepCompleted="e1=2"/>
            </v-stepper-content>
            
             <v-stepper-content step="2">
               <ShippingDetails v-on:stepCompleted="e1=3" v-on:goBack="e1=1"/>
            </v-stepper-content>
            <v-stepper-content step="3">
             
                <PaymentMethod />
            </v-stepper-content>
        </v-stepper-items>
    </v-stepper>
</template>

<script>
import CartSummary from './CartSummary'
import ShippingDetails from './ShippingDetails'
import PaymentMethod from './PaymentMethod'
export default {
    data: function(){
        return {
            e1:1
        }
    },
    components:{
        CartSummary,
        ShippingDetails,
        PaymentMethod
    }
}
</script>