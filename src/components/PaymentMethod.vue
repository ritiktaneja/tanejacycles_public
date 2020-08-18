<template>
    <v-card height="250" flat class="text-center">
         <span class="headline font-weight-light">Select Payment Method</span>
          <v-divider width="60%" class="mx-auto my-2"></v-divider>
            
        <v-container  grid-list-xs>

          
        <v-btn color="primary" :loading="this.loading" @click="initiateOrder()">Pay Using Paytm Gateway</v-btn>
        
          <v-form v-show="false" ref="form"  method="post" target="_blank" action="https://securegw.paytm.in/order/process" name="paytm">
       
               <v-text-field type="hidden" name="MID" v-model="paytm_params['MID']"/>
                <v-text-field type="hidden" name="CHECKSUMHASH" v-model="paytm_params['CHECKSUMHASH']"/>
               <v-text-field type="hidden" name="WEBSITE" v-model="paytm_params['WEBSITE']"/>
               <v-text-field type="hidden" name="ORDER_ID" v-model="paytm_params['ORDER_ID']"/>
               <v-text-field type="hidden" name="CUST_ID" v-model="paytm_params['CUST_ID']"/>
               <v-text-field type="hidden" name="INDUSTRY_TYPE_ID" v-model="paytm_params['INDUSTRY_TYPE_ID']"/>
               <v-text-field type="hidden" name="CHANNEL_ID" v-model="paytm_params['CHANNEL_ID']"/>
               <v-text-field type="hidden" name="TXN_AMOUNT" v-model="paytm_params['TXN_AMOUNT']"/>
               <v-text-field type="hidden" name="CALLBACK_URL" v-model="paytm_params['CALLBACK_URL']"/>
              
               <v-btn type="submit" label="submit" value="submit">Submit </v-btn>
           
         </v-form>
        </v-container>
        
    </v-card>
</template>






<script>
import axios from 'axios'


export default {
    data:function(){
        return {
            
            paytm_params : {
                WEBSITE:"",
                ORDER_ID:"",
                CUST_ID:"",
                MOBILE_NO:"",
                EMAIL:"",
                INDUSTRY_TYPE_ID:"",
                TXN_AMOUNT:"",
                CHANNEL_ID:"",
                CALLBACK_URL:"",
                CHECKSUMHASH:"",

                loading:false,
            }
        }
    },
    mounted (){
           
    },
    
    methods : {
       async initiateOrder()
        {
            this.loading = true
            let cart = this.$store.state.cart
            let user = this.$store.state.user
            let bicycle = []
            
            cart.forEach((x)=>{
                bicycle.push(x)
            })
           
            var csrftoken =  this.getCookie('csrftoken');
            
            var data = {...user,bicycle:bicycle,paymentMethod:'PAYTM'}
            console.log(csrftoken)
            axios.defaults.headers.post['X-CSRFTOKEN']=csrftoken;
            console.log(axios.defaults.headers.post)
            axios({
                method:'post',
                url : this.$store.state.BACKENDURL+'orders/',
                data :data,          
            })
            .then(response=>{
              if(response.data)   
                {   
                   console.log(response.data)
                    this.paytm_params = response.data

                   
                }
                else
                    console.log(response.data)

            })
            .catch(e=> {
                console.log('error Occured :'+e)
                this.$store.commit('ERROR_OCCURED',e)
            })
            .finally(()=>{
                if(this.paytm_params.MID)
                this.makePayment()
                this.loading = false;
            })
        },
        makePayment()
        {  
            this.loading = true;
            console.log(this.paytm_params)
            this.$refs.form.$el.submit()
            this.$router.push({name:'Home'})
        },
         getCookie(name) {
             
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        
      
    }
}
</script>