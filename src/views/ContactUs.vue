<template>
    <v-card id="contactus" class="white--text" flat>
        <v-container grid-list-xs fluid>
            <div class="text-center headline font-weight-bold white--text    ">Contact Us</div>
            <div class="     text-capitalize font-weight-light">Are you the customer that needs help? </div> <div class="display-1 text-capitalize font-weight-bold"> That's what our team is here for!</div>

            <v-row>
                <v-col md="4" sm="12" xs="12"> 
                    <v-card min-height="200"  class=" pa-5 white--text  transparent">
                        <span class="text-h5">Registered Office</span>   <br> <br> 
                        <span class="text-h7">1 Turner Road,  Clement Town <br> Dehradun <br> Uttrakhand <br> Pincode-248001</span>
                        
                    </v-card> 
                </v-col>
                 <v-col md="4" sm="12" xs="12"> 
                    <v-card min-height="200" class="white--text pa-5 transparent">
                        <span class="text-h5">Our Social Media Handles</span>  <br> <br>
                        <span> <v-icon large color="white">mdi-facebook</v-icon> <a href="https://fb.me/tanejacycles" class="white--text" style="text-decoration:none;" target="_blank"> Taneja Cycles </a> </span> <br> <br>
                        <span> <v-icon large color="white">mdi-google-my-business</v-icon> <a href="https://g.page/Tanejacycles?we" class="white--text" style="text-decoration:none;" target="_blank"> Taneja Cycle Works </a> </span>
                    </v-card> 
                </v-col>
                 <v-col md="4" sm="12" xs="12"> 
                    <v-card min-height="200" class=" pa-5 white--text  transparent">
                        <span class="text-h5">Email & Phone</span> <br><br>
                        <span> <v-icon large color="white">mdi-gmail</v-icon> <a href="mailto:tanejacycleworks@gmail.com" class="white--text" style="text-decoration:none;" target="_blank"> tanejacycleworks@gmail.com </a> </span> <br>
                        <span> <v-icon large color="white">mdi-whatsapp</v-icon> <a href="https://wa.me/916396843575" class="white--text" style="text-decoration:none;" target="_blank"> 6396 843 575 </a> </span> <br>
                         <span> <v-icon large color="white">mdi-phone</v-icon> <a href="tel:9837478850" class="white--text" style="text-decoration:none;" target="_blank"> 9837 478 850 </a> </span>                        
                    </v-card> 
                </v-col>
            </v-row>
       
        </v-container>
    </v-card>
</template>

<script>
export default {
    
}
</script>
<style scoped>
#contactus{

background: #6190E8 ;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #A7BFE8, #6190E8) ;  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #A7BFE8, #6190E8); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
</style>