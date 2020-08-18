<template>
    <v-card>
        <v-container grid-list-xs>
            <div class="headline">
              Active Orders  
            </div>
            <v-divider></v-divider>
            <v-simple-table>
              
                    <thead>
                       <th> Customer </th>
                       <th> Order Details </th>
                       <th> Product Details </th>
                       <th> Payment Details </th>
                       <th> Order Status </th>
                    </thead>
                    <tbody>
                        <tr v-for ="(o,index) in orderList" :key="index">
                            <td> 
                                <div> 
                                    {{o.name}} /  {{o.phone}}
                                    <br>
                                    {{o.email}}
                                    <br>
                                    {{o.addr1}} , {{o.addr2}} , {{o.locality}}
                                    <br>
                                    Alternate Number : {{o.phone2}}
                                </div>
                            </td>
                            <td>
                                <span class="font-weight-bold">
                                    Order Id : {{o.id}}
                                    <br>
                                    Order Date : {{new Date(o.datetime)}}
                                </span>
                            </td>
                            <td>
                                <div class="grey lighten-1  mt-2" v-for="(product,i) in o.products" :key="i">
                                   <span class=""> Name :  {{product.brand}} {{product.name}}</span>
                                   <br>
                                    <span class="font-weight-bold"> Details : </span>  {{product.size}} {{product.color}}
                                    ( &#8377; {{product.price}} )
                                </div>
                            </td>

                            <td>
                                <div>
                                    <span class="font-weight-bold">Total Amount : &#8377; {{o.totalAmount}}</span>
                                    <br>
                                    <span class="body-1"> Payment Method : {{o.paymentMethod}}</span> <br>
                                    <span class="body-1" :class="{'success--text':o.paymentStatus == 'confirmed'}" > Payment Status : {{o.paymentStatus}} </span>
                                </div>
                            </td>
                            <td>
                                <div>
                                    <span class="font-weight-bold">Order Status : <br> {{o.orderStatus}} </span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
              
            </v-simple-table>
        </v-container>
    </v-card>
</template>

<script>
import axios from 'axios'
export default {
    data : function(){
        return{
           
            orderList : [
                {
                    name : 'Ritik',
                    phone : '123123',
                    email : 'ritiktaneja10@gmail.com',
                    addr1 : '12 Aashima Vihar',
                    addr2 : 'Turner Road',
                    locality : 'ISBT',
                    phone2 : '0',
                    orderDate : '10 June 2000',
                    orderId : '1',
                    orderStatus : 'Confirmed',
                    paymentMethod : 'COD',
                    totalAmount : '9899',
                    products : [
                        {
                            brand : 'Hero',
                            name :'DTB',
                            price : '4500',
                            amount : '5000',
                            size : '24T',
                            color : 'Red'
                        },
                        {
                            brand : 'Hero',
                            name :'DTB',
                            price : '4500',
                            amount : '5000',
                            size : '24T',
                            color : 'Red'
                        },
                        {
                            brand : 'Hero',
                            name :'DTB',
                            price : '4500',
                            amount : '5000',
                            size : '24T',
                            color : 'Red'
                        }
                    ],
                },
              
            ]
        }
    },
    mounted (){
        this.getOrderList()
    },
    methods : {
        getOrderList()
        {
            axios.get(this.$store.state.BACKENDURL+'orders/')
            .then(response=>{
                console.log(response.data)
                this.orderList = response.data
            })
            .catch(error=>{
                console.log('error , '+error)
                this.$store.commit('ERROR_OCCURED',error)
            })
        }
    }
    
}
</script>