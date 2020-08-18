import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Catalog from '../views/Catalog'
import Product from '../views/Product'
import Checkout from '../views/Checkout'
import Admin from '../views/Admin'

import ContactUs from '../views/ContactUs'
import TrackOrder from '../views/TrackOrder'

import PrivacyPolicy from '../views/PrivacyPolicy'
import TermsAndConditions from '../views/TermsAndConditions'
import ReturnPolicy from  '../views/ReturnPolicy'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/catalog/:category?',
    name: 'Catalog',
    component: Catalog,
    props: (route) => ({ query: route.query.q })
  },
  {
    path: '/product/:id',
    name: 'Product',
    component: Product
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: Checkout
  },
  {
    path: '/admindsadasdas7d7asd897as89d7a89s7d94asd56a1sd61as66#!#$#%#$%^%^$%',
    name: 'Admin',
    component: Admin
  },
  {
    path: '/contactus',
    name: 'ContactUs',
    component: ContactUs
  },
  {
    path: '/privacypolicy',
    name: 'PrivacyPolicy',
    component: PrivacyPolicy
  },
  {
    path: '/terms',
    name: 'TermsAndConditions',
    component: TermsAndConditions
  },
  {
    path: '/returns',
    name: 'ReturnPolicy',
    component: ReturnPolicy
  },
  {
    path: '/about',
    name: 'AboutUs',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path : '/track/:status?/:id?',
    name : 'TrackOrder',
    component : TrackOrder
    
  }
  
]

const router = new VueRouter({
  mode:'history',
  routes,
  scrollBehavior() {
    document.getElementById('app').scrollIntoView();
}
})

export default router
