import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

import axios from 'axios'


import VueAnalytics from 'vue-analytics';
Vue.use(VueAnalytics, {
  id: 'UA-171696572-1',
  router
})

import VueMeta from 'vue-meta'
Vue.use(VueMeta)

Vue.prototype.$http = axios
Vue.config.productionTip = false

new Vue({
  router,
  store,
 
  vuetify,
  render: h => h(App)
}).$mount('#app')
