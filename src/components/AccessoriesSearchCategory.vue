<template>
     <v-container class="grey lighten-3">
             
                <v-row>
                    <v-col>
                        <div class="h3 font-weight-bold"> By Brand</div>
                        <v-list dense class="transparent">
                         <v-list-item v-for="(brand,index) in ['Hero', 'Huge','Kross']" :key="index"> 
                              <v-btn text small >  {{brand}} </v-btn>
                          </v-list-item>
                        </v-list>
                    </v-col>
                     <v-col >
                        <div class="h3 font-weight-bold"> By Category</div>
                        <v-list dense class="transparent">
                         <v-list-item v-for="(brand,index) in ['Gel Cover', 'Lock','Mudguards','Odo meter','Lights','Helmets' ]" :key="index"> 
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