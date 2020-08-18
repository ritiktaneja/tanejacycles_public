<template>
    <v-dialog
      v-model="dialog"
      width="700"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          small
          text
          dark
          v-bind="attrs"
          v-on="on"
        >
          Size Chart
        </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline grey lighten-4"
          primary-title
        >
          Size Chart
          <div class="ml-auto"><v-btn text color="primary" @click="dialog=false"> <v-icon>mdi-close</v-icon></v-btn> </div>
        </v-card-title>

        <v-card-text>
        <v-simple-table>
          <thead>
            <tr>
              <th>Wheel Size</th>
              <th>Age Group</th>
              <th>Suitable Height</th>
            </tr>
          </thead>
          <tbody>
          <tr v-for="(s,index) in sizeChart" :key="index">
           <td>
             {{s.wheel_size}}
           </td>
           <td>
             {{s.riderAge}}
           </td>
           <td>
             {{s.riderHeight}}
           </td>
          </tr>
          </tbody>
        </v-simple-table>
        </v-card-text>

        <v-divider></v-divider>

       
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  methods: {

  },
  data : function(){
    return{
      sizeChart :[],
      dialog:false
    }
  },
  mounted (){
  let sizes = this.$store.state.SizeEnums;
    let getSize = this.$store.state.SizeChart;
    
    Object.keys(sizes).map(size=>{
      this.sizeChart.push(getSize(size))   
    })

  }
}
</script>
