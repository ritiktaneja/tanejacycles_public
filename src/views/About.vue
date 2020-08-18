<template>
  <v-card class="grey lighten-4">
    <v-container>
      <h1>About Us</h1>
      <v-row justify="center"  class=" text-center ">
        <v-col lg="6"  md="6" class="primary--text ">
      
      <span>
        Taneja Cycle Works is the leading wholesaler and retailer in the cycling world in Uttrakhand since 1962.<br>
        We, at Taneja Cycles believe more in building relations with our customers rather than just dealing with them, and 'take pride in their ride'.
      </span>
      <br>
      <span>
      Check us out to get the guranteed best deals in the town and the state on leading bicycle brands.
      </span>
      <br>
      <span>
      Think Globally and cycle locally with Taneja Cycle Works.
      </span>
        </v-col>
        <v-col  v-if="false">
          <v-timeline>
            <v-timeline-item v-for="(item,index) in timeline" :key="index">
            <template v-slot:opposite>
              <span
                class="headline font-weight-bold primary--text"
              >
                {{item.year}}
              </span>
            </template>
            <v-card>
              <v-card-title>
               {{item.title}}
              </v-card-title>
              <v-card-text>
                {{item.desc}}
              </v-card-text>
            </v-card>
            </v-timeline-item>
          </v-timeline>
        </v-col>
      </v-row>

      <span class="text-h4">Our Team</span>

      <v-row>
        <v-col cols="12" md="3" lg="3" v-for="(t,index) in team" :key="index">
          <v-card class="transparent">
              <v-card-title primary-title>
                {{t.name}}
              </v-card-title>
              <v-card-subtitle>
                {{t.position}}
              </v-card-subtitle>
              <v-card-text>
                {{t.desc}}
              </v-card-text>
          </v-card>
          
        </v-col>
      </v-row>

    
    </v-container>
  </v-card>
</template>

<script>
export default {
  data : function(){
    return {
      timeline : [
        {
          year:1962,
          title:'Founded',
          'desc':''
        },
        {
          year : 2005,
          title: 'First Dealership',
          desc : ''
        }
      ],
      team : [
        {
          name:'JS Taneja',
          position:'Proprietor'
        },
          {
          name:'Bharat Taneja',
          position:'Head - R&D'
        },
         {
          name:'Gaurav Taneja',
          position:'Head - Sales & Operations'
        }, 
        {
          name:'Ritik Taneja',
          position:'Head - Marketing '
        }
      ]
    }
  }
}
</script>
