<template>
<nav>
        <v-navigation-drawer
        v-model="filterDrawerComputed"
        :app="$vuetify.breakpoint.smAndDown"
       
        bottom
        height="auto"
        class="grey  lighten-3"
        >
        <v-list
        dense
        class="mb-5 pb-5"
        nav>
      
         
        <div class="text-h6 my-3 d-flex justify-space-between ">
            <span> Filter Products </span>
            
            <v-btn  v-if="$vuetify.breakpoint.mdAndDown" small text><v-icon @click="$emit('closeDrawer')" color="primary">mdi-close</v-icon></v-btn>
        </div>
        
        <v-divider class="my-1"></v-divider>

        <div class="mt-2">
            <span class="">Filter by Gears</span>
           <v-row>
            <v-col class="ma-1 pa-1" v-for="s in Object.keys(speed)" :key="s"><v-checkbox class="ma-0 pa-0"  :label="s" v-model="selectedSpeed" :value="speed[s]"></v-checkbox></v-col>
            </v-row>
        </div>

        <div class="mt-2">
            <span class="">Filter by Size</span>
           <v-row>
            <v-col class="ma-1 pa-1" v-for="s in Object.keys(size)" :key="s"><v-checkbox class="ma-0 pa-0"  :label="s" v-model="selectedSize" :value="size[s]"></v-checkbox></v-col>
            </v-row>
        </div>

         <div class="mt-2">
            <span class="">Filter by Price</span>
           <v-row>
            <v-col class="mt-3 pt-5">
                
                 <v-range-slider
            v-model="range"
            :max="max"
            :min="min"
            thumb-label="always"
            hide-details
            class="align-center pa-1"
          >
            
          </v-range-slider>

            </v-col>
            </v-row>
        </div>


        <div class="justify-center d-flex mb-5">
            <v-btn color="primary" v-if="$vuetify.breakpoint.mdAndUp" class="text-center" @click="filter()" outlined>Filter</v-btn>

             <v-btn  v-else color="blue"
             dark 
        fixed
        right
        @click="filter()"
        bottom
        fab
        >
        <v-icon>mdi-filter</v-icon>
        </v-btn>   

        </div>
        </v-list>
    </v-navigation-drawer>
</nav>
</template>
<script>
export default {
    props:{
        filterDrawer:{type:Boolean}
    },
    data: function(){
        return{
            selectedSpeed :[],
            selectedSize : [],
            speed : this.$store.state.SpeedEnums,
            size : this.$store.state.SizeEnums,
            min:0,
            max:50000,
            range:[0,50000]
        }
    },
    computed : {
        filterDrawerComputed :{
            get(){
                return this.filterDrawer
            },
            set(filterDrawer){
                return filterDrawer
            }
            
        }
    },
    methods:{
        filter()
        {
            let filterUrl = ""

            this.selectedSpeed.forEach(s=>{
                filterUrl+="speed="+s+"&"
            })
            this.selectedSize.forEach(s=>{
                filterUrl+="wheel_size="+s+"&"
            })
            filterUrl+="price__gt="+this.range[0]+"&"
            filterUrl+="price__lt="+this.range[1]+'&'
           
            this.$emit('filterData',filterUrl)
        }
    }
}
</script>