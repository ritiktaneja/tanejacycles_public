<template>
<v-card flat class="grey lighten-4" outlined>
    <v-container grid-list-xs>
        
   
      <div class="mb-4 text-center headline font-weight-bold">Order Summary</div>
      <div class="text-h6 d-flex font-weight-regular justify-space-between">
          <span>Total Amount : </span> <span class="font-weight-bold ml-5"> &#8377; {{getMrp}} </span>
      </div>
      <div class="text-h7 mt-3 d-flex font-weight-regular justify-space-between ">
          <span>Discount : </span> <span class="ml-5"> &#8377; {{getDiscount}} </span>
      </div>
       <div class="text-h7 pt-3 d-flex font-weight-regular justify-space-between ">
          <span>Shipping : </span> <span :class='{"success--text font-weight-bold":!getShipping}' class="ml-5">  {{getShipping==0?'FREE' : '&#8377;'+ getShipping }} </span>
      </div>    
        <v-divider class="mt-5"></v-divider>
     <div class="text-h5 pt-3 d-flex primary--text font-weight-bold justify-space-between ">
          <span>Grand Total : </span> <span class="ml-5">  {{getGrandTotal }} </span>
      </div>
       </v-container>
  </v-card>
</template>
<script>
export default {
    computed : {
        cart(){
            return this.$store.state.cart
        },
        getMrp(){
            let amount = 0;
            this.cart.forEach(x=> {
                amount+=parseInt(x.mrp)
            })
            return amount
        },
        getDiscount(){
             let amount = 0;
            this.cart.forEach(x=> {
                amount+= (parseInt(x.mrp)-parseInt(x.price))
            })
            return amount
        },
        getGrandTotal(){
            let amount =  this.getMrp-this.getDiscount+this.getShipping;
            this.$store.commit('UPDATE_GRAND_TOTAL',amount)
            return amount
        },
        getShipping(){
            return 0;
        }
    }
}
</script>