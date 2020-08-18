<template>
     <v-container class="grey lighten-3">
             
                <v-row>
                    <v-col md="4">
                        <div class="h3 font-weight-bold"> By Brand</div>
                        <v-list dense class="transparent">
                         <v-list-item v-for="(brand,index) in ['Hero', 'Huge','Kross']" :key="index"> 
                              <v-btn text small >  {{brand}} </v-btn>
                          </v-list-item>
                        </v-list>
                    </v-col>
                     <v-col md="4">
                        <div class="h3 font-weight-bold"> By Category</div>
                        <v-list dense class="transparent">
                         <v-list-item v-for="(brand,index) in ['City', 'Mtb','Hybrid','Electric','Kids']" :key="index"> 
                              <v-btn text small >  {{brand}} </v-btn>
                          </v-list-item>
                        </v-list>
                    </v-col>
                    <v-col md="4">
                        <div class="h3 font-weight-bold"> By Wheel Size</div>
                        <v-list dense class="transparent">
                         <v-list-item v-for="(brand,index) in ['12T', '14T','16T','18T','24T','26T','27.5T','29T']" :key="index"> 
                              <v-btn text small >  {{brand}} </v-btn>
                          </v-list-item>
                        </v-list>
                    </v-col>
                    
                    
                </v-row>
            </v-container>
</template>
<script>
export default {
    
}
</script>