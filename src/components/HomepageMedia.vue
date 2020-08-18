<template>

        <v-parallax height="500" contain :src="images[0]">
            <v-row align="center" justify="center">
                <v-col cols="12" class=" text-center">
                    <span v-if="$vuetify.breakpoint.smAndDown" id="tagline" class="text-h2 font-weight-regular">Paddle Away!</span>
                    <span v-else id="tagline" class="text-h2 font-weight-regular">A solution to ride your health problems</span>
                    <br>
                    <v-btn @click="$router.push({name:'Catalog'})" color="orange" class="white--text" > Explore Now </v-btn>
                </v-col>
            </v-row>

        </v-parallax>
</template>

<script>
export default {
    data:function(){
        return {
           
        }
    },
    computed:{
        images()
        {
            return [require('@/assets/home-slider1.jpg')]
        }
    }
    
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');

#tagline
{
    font-family: 'Permanent Marker', cursive !important;

}
</style>  