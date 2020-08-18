<template>

<v-form class="mt-5" ref='form' @submit.prevent=""> 
    <v-row class="mx-auto">
       
        <v-select

            :items="product.color"
            v-model="selectedColor"
            outlined
            @click="$emit('colorSelected',selectedColor)"
            dense
            :rules="[v=>!!v||'Please select a color']"
            label="Select Color"
        ></v-select>

         <v-select
        v-if="typeof product.size == 'object' && product.size.length>1"
            :items="product.size"
            :rules="[v=>!!v || 'Please select a size']"
            v-model="selectedSize"
            label="Select Color"
        ></v-select>
    </v-row>
</v-form>
    
</template>
<script>
export default {
    props : {
        product : {
            type:Object,
            required:true
        }
    },
    data : function()
    {
        return{
            selectedColor:'' ,
            selectedSize : '',
        }
    },

    methods : {
        validateVariables(){
            this.$ref.form.validate()
        }
    }
}
</script>