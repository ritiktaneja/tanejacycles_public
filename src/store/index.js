import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const BACKENDURL = process.env.BACKENDURL  || 'https://tanejacycles.com/api/'
const BACKENDBASE = process.env.BACKENDBASE || 'https://tanejacycles.com'

const SpeedEnums = {
  'Single Speed':'speedsingle',
  '6 Speed' :'speed6',
  '7 Speed' :'speed7',
  '12 Speed' :'speed12',
  '18 Speed' :'speed18',
  '21 Speed' : 'speed21',
  '24 Speed' : 'speed24',
}
const SizeEnums ={ 
  '12T' : 'size12', 
  '14T' : 'size14',
  '16T' : 'size16',
  '18T' : 'size18',
  '20T' : 'size20',
  '24T' :'size24',
  '26T' :'size26',
  '27.5T':'size275',
  '29T':'size29'
} 



export default new Vuex.Store({
  state: {
    cart : [
          ],
    user : {

    },
    grand_total: 0,
    BACKENDURL:BACKENDURL,
    BACKENDBASE : BACKENDBASE,
    SpeedEnums : SpeedEnums,
    SizeEnums : SizeEnums,
    SizeChart : (size)=>{
      switch (size)
      {
        case '12T':
        case '14T':  
          return {wheel_size:size,riderAge:'2-5yrs',riderHeight:"2'6'' - 3'0''  "}
        case '16T':
          return {wheel_size:size,riderAge:'4-6yrs',riderHeight:"3'0'' - 3'6''"}
        case '18T':
          return {wheel_size:size,riderAge:'5-9yrs',riderHeight:"3'6'' - 4'0''"}
        case '20T':
        case '24T':
          return {wheel_size:size,riderAge:'6-11yrs',riderHeight:"4'0'' - 4'6''"}
        case '26T':
        case '27.5T':
        case '29T':
          return {wheel_size:size,riderAge : '11+yrs',riderHeight:"5'6'' and Above"}
        default :
          return {riderAge :'NA', riderHeight : 'NA'}
        
      }
    }
  
  },

  mutations: {
    ADD_TO_CART(state,product)
    {

      state.cart.push({...product,cartId:Date.now()})
      localStorage.cart = JSON.stringify(state.cart)
      console.log('Product Added!')
    },
    REMOVE_FROM_CART(state,product)
    {
     state.cart= state.cart.filter(x=> {
     
        return (x.cartId!==product.cartId)
      })
      localStorage.cart = JSON.stringify(state.cart)
      
    },
    ADD_SHIPPING_DETAILS(state,user)
    {
      localStorage.user = JSON.stringify(user)
      state.user=user
    },
    UPDATE_CART_ON_LOAD(state,cart)
    {
      state.cart = cart
    },
    UPDATE_GRAND_TOTAL(state,amount)
    {
      state.grand_total = amount
    },
    ERROR_OCCURRED(state,e)
    { 
      console.log("Error from store")

      axios.post(state.BACKENDURL+'error/',{...state,error:e})
      
    }
  },
  actions: {
  },
  modules: {
  }
})
