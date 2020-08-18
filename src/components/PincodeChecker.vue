<template>
 <v-form @submit.prevent="" ref="form">
            
    <v-row class="my-5 justify-center mx-auto d-flex align-center">
       
        
        <v-text-field
            name="pincode"
            label="Pincode"
            :success-messages="successMessage"
            id="pincode"
            disabled
            value="Currently Delivering in Uttrakhand Only"
            :rules='[v=>!!v || "Please Enter your pincode" ]'
          
        ></v-text-field>
        <v-btn small disabled outlined class="mx-3 black--text" color="black" dark @click="verify()" >Check Delivery</v-btn>
    </v-row>
    </v-form>
</template>
<script>
export default {
    data : function(){
       return {
        pincode : "",
        successMessage:"",
       }
        
    },
    methods : {
        verify(){
            if(this.$refs.form.validate())
            {
                this.successMessage="Free Delivery Applicable!"
            }
        }
    }
    
}
</script>