<template>
    <div @click="$router.push({path:'/'})" id="companyLogo" class=""  :class="{'display-1':$vuetify.breakpoint.lgAndUp,'headline mt-3':$vuetify.breakpoint.smAndDown}">
       <span class=" font-italic primary--text">Taneja </span>
       <span class=" font-italic">Cycles</span> 
        <v-icon  class="primary--text mx-2 font-italic" :large="$vuetify.breakpoint.lgAndUp" >mdi-bike</v-icon>
    </div>
</template>
<script>
export default {
    
    
      
    

}
</script>

<style  scoped>
@import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');

#companyLogo
{
    font-family: 'Permanent Marker', cursive !important;

}

</style>