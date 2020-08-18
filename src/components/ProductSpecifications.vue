<template>
    <v-card>
          <v-container grid-list-xs>
            <v-simple-table>
                <tbody>
                <tr class="font-weight-bold text-center text-capitalize" v-for="(s,index) in Object.keys(specifications)" :key="index"> 
                    <td >{{specifications[s]}} </td>
                    <td v-if="typeof product[s] == 'object'" > {{ product[s].join(',')   }} </td>
                    <td v-else> {{product[s]}}</td>
                </tr>
                </tbody>
            </v-simple-table>
        </v-container>
    </v-card>
</template>

<script>
export default {
    props : {
        product : {
            type : Object
        }
    },
    data : function(){
        return {
             specifications:{'frame':'Frame','frame_material':'Frame Material','fork':'Fork','saddle':'Saddle','rims':'Rims','gender':'Gender','brakes':'Brakes','color':'Colors Available'}
        }
    },
    mounted()
    {
        console.log(this.product)
    }   
}
</script>