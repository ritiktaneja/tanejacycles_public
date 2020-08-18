<template>
    <v-card flat class="grey pb-5  lighten-3">
        <v-container  class="text-center pt-5 pb-5 "  grid-list-xs>
            <v-row class="text-h4 myfont " justify="center"> A Bicycle For All </v-row>

            <v-row class=" pb-5 ">
                <v-col height="100" cols="6" md="3" lg="3"> 
                     
                                <v-card   class="transparent" @click="$router.push({name:'Catalog',params:{category:'mountain'}})">
                                <v-img class="white--text align-center" contain src="@/assets/mountainbike.jpg">
                                   
                                <div
                                    
                                    class="d-flex myfont transition-fast-in-fast-out  v-card--reveal headline white--text"
                                    style="height: 100%;!important"
                                >
                                    Mountain Bikes
                                </div>
                      
                                </v-img>
                                </v-card>
                     
                </v-col>

                 <v-col cols="6" md="3" lg="3"> 
                    
                                <v-card   @click="$router.push({name:'Catalog',params:{category:'kids'}})" class="transparent">
                                <v-img class="white--text align-center" contain src="@/assets/bikes4kids.jpg">
                                   
                                <div
                                    
                                    class="d-flex myfont transition-fast-in-fast-out  v-card--reveal headline white--text"
                                    style="height: 100%;!important"
                                >
                                    Bikes For Kids
                                </div>
                     
                                </v-img>
                                </v-card>
                    
                </v-col>
                 <v-col cols="6" md="3" lg="3"> 
                     
                                <v-card  @click="$router.push({name:'Catalog',params:{category:'road'}})" class="transparent">
                                <v-img class="white--text align-center" contain src="@/assets/roadbike.jpg">
                                    
                                <div
                                    
                                    class="d-flex myfont transition-fast-in-fast-out  v-card--reveal headline white--text"
                                    style="height: 100%;!important"
                                >
                                   Road Bikes 
                                </div>
                        
                                </v-img>
                                </v-card>
                    
                </v-col>
                   <v-col cols="6" md="3" lg="3"> 
                     
                                <v-card   @click="$router.push({name:'Catalog',params:{category:'lady'}})" class="transparent">
                                <v-img class="white--text align-center" contain src="@/assets/ladybird.webp">
                                    
                                <div
                                    
                                    class="d-flex myfont transition-fast-in-fast-out  v-card--reveal headline white--text"
                                    style="height: 100%;!important"
                                >
                                    Lady Bird
                                </div>
                        
                                </v-img>
                                </v-card>
                    
                </v-col>
            </v-row>
        </v-container>
    </v-card>
    
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');

.myfont
{
    font-family: 'Permanent Marker', cursive !important;

}
</style>  