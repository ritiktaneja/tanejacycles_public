<template>
    <v-card>
        <v-container fluid class="text-center grey lighten-5" v-if="status" grid-list-xs>
            <div v-if="status == 'success'" class="headline font-weight-bold"><span class="success--text ">Congratulations!</span > <span class="primary--text"> Your Order Has Been Placed with Order Id : {{orderId}} </span></div>
            <div v-if="status =='pending'" class="headline font-weight-bold "> We are processing your Order and will reach to you soon! <br> Your Order Id is <span class="red--text"> {{orderId}} </span> </div>
             <div v-if="status =='failure'" class=" secondary--text font-weight-bold "> <span class=""> Your Transaction couldn't be completed. </span> <br>
            <router-link :to='{name:"Checkout"}' >  <span class="body-1">Click here to checkout again!</span> </router-link></div>
            <div> You can track your Order and Payment Status using the form below</div>
        </v-container>

        <v-container>
            <v-row class="mx-auto headline">Track Your Order</v-row>
            <v-form @submit.prevent="" ref="form">
                <v-row class=''>
                    <v-col cols="12" md="4" lg="4">
            <v-text-field
                name="orderId"
                label="Order ID"
                id="orderid"
                :rules ='[v=>!!v || "Please Enter Your Order ID" ]'
                v-model = "orderId"
            ></v-text-field>
                    </v-col>
                    <v-col cols="12" md="4" lg="4">
            <v-text-field
                name="phone"
                label="Phone Number"
                id="phone"
                v-model="phone"
                :rules='[v=>!!v || "Please Enter your contact number"]'
            ></v-text-field>
                    </v-col>
                    <v-col cols="12" md="4" lg="4">
                <v-btn color="primary" @click="getStatus()" class="mx-auto" outlined>Track Order</v-btn>
                    </v-col>
                </v-row>
            </v-form>
        </v-container>

        

        <v-container grid-list-xs>
          
            <v-simple-table  v-if="order.name">
             
                    <thead>
                        <th>Customer Name </th>
                        <th>Order Id </th>
                        <th>Total Amount </th>
                        <th>Order Status </th>
                        <th>Payment Method</th>
                        <th>Payment Status </th>
                    </thead>


                    <tbody>
                        <tr>
                            <td>{{order.name}}</td>
                            <td>{{order.id}}<td>
                            <td>{{order.amount}} </td>
                            <td>{{order.orderStatus}}</td>
                            <td>{{order.paymentMethod}}</td>
                            <td>{{order.paymentStatus}}</td>
                        </tr>
                    </tbody>
                   
            </v-simple-table>
           
                <v-card v-if="order.exists === false" class="red lighten-4 pa-3 text-center">
                   Order with the mentioned details does not exist with us. <br> Please recheck the details or reach our support team is you think this is a mistake.
                </v-card>
    
                <div class="text-center subtitle-1 mt-5">Have some issues? You can reach our support team <router-link :to="{name:'ContactUs'}"> here!</router-link></div>
        </v-container>
    </v-card>
</template>

<script>
import axios from 'axios'
export default {
    data : function(){
        return {
            orderId: "",
            status : "12",
            phone : "",
            order : "1",
        }
    },
    mounted (){
        if(this.$route.params.id)
            this.orderId = this.$route.params.id
        if(this.$route.params.status)
            this.status = this.$route.params.status
        
        if(this.status == 'success' || this.status == 'failure')
            localStorage.cart = []
    },
    methods: {

        getStatus(){
            if(this.$refs.form.validate())
            axios.get(this.$store.state.BACKENDURL+'order-status/?id='+this.orderId+'&phone='+this.phone)
            .then(response=> {
                console.log(response.data)
                this.order = response.data
            })
            .catch((e)=>{
                this.$store.commit('ERROR_OCCURED',e)
            })
        }
    }
    
}
</script>