<template>
<v-card flat class="text-center ">
      <span class="mt-0 pt-0 headline secondary--text text-center font-weight-light">Add Shipping Address</span>
         <v-divider width="60%" class="mx-auto my-2"></v-divider>
    <v-container grid-list-xs>
    <v-form ref="form" @submit.prevent="">
        <v-row>
            <v-text-field
                name="name"
                label="Full Name"
                id="name"
                :rules='[...required]'
                v-model="user.name"
            ></v-text-field>
        </v-row>
         <v-row>
            <v-text-field
                name="email"
                :rules='[...required,...emailRules]'
                label="Email Address"
                id="email"
                class="mr-4"
                v-model="user.email"
            ></v-text-field>
               <v-text-field
                name="phone"
                type="number"
                :rules='[...required,...phoneRules]'
                label="Contact Number"
                id="phone"
                v-model="user.phone"
            ></v-text-field>
        </v-row>
        <v-row>
               <v-text-field
                name="addr1"
                :rules='[...required]'
                label="Address Line 1"
                id="addr1"
                class="mr-4"
                v-model="user.addr1"
            ></v-text-field>
               <v-text-field
                name="addr2"
                :rules='[...required]'
                label="Address Line 2"
                id="addr2"
                v-model="user.addr2"
            ></v-text-field>
        </v-row>
          <v-row>
               <v-text-field
                name="locality"
                label="Landmark"
                class="mr-4"
                id="landmark"
                v-model="user.landmark"
            ></v-text-field>
               <v-text-field
                name="phone2"
              type="number"
              
                label="Optional Contact Number"
                id="phone2"
                v-model="user.phone2"
            ></v-text-field>
        </v-row>
        <v-row>
            <v-text-field
                name="city"
                label="City"
                class="mr-4"
                id="city"
                value="Dehradun"
                disabled
            ></v-text-field>
               <v-text-field
                name="State"
                label="State"
                id="state"
                value="Uttrakhand"
                disabled
            ></v-text-field>
        </v-row>
       <v-row>
           <v-btn color="secondary" @click="$emit('goBack')" text>Back</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="validateForm()" text>Next</v-btn>
        </v-row>
    
    </v-form>
      </v-container>
    </v-card>
</template>

<script>
export default {
    data : function(){
        return {
            user : {},
            required:[v=>!!v || 'This Field is required'],
            emailRules: [ 
                v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
              ],
            phoneRules : [
                v=> /^\d{10}$/.test(v) || 'Please enter a valid 10 digit mobile number'
            ]
        }
    },
    mounted()
    {
        if(localStorage.user)
        this.user = JSON.parse(localStorage.user)
    },
    methods : {
        validateForm(){
               if( this.$refs.form.validate())
               {
                   this.$store.commit('ADD_SHIPPING_DETAILS',this.user)
                   this.$emit('stepCompleted')
               }
        }
    }
    
}
</script>