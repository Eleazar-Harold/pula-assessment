/*jshint esversion: 6 */
import Vue from 'vue';
import VueRouter from 'vue-router';
import Farm from './views/Farm';
import Login from './views/Login';
import Logout from './views/Logout';
import Harvest from './views/Harvest';
import Register from './views/Register';
import Resource from './views/Resource';

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/farm',
            name: 'farms',
            component: Farm,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/',
            name: 'login',
            component: Login,
        },
        {
            path: '/logout',
            name: 'logout',
            component: Logout,
        },
        {
            path: '/signup',
            name: 'signup',
            component: Register,
        },
        {
            path: '/harvest',
            name: 'harvests',
            component: Harvest,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/resource',
            name: 'resources',
            component: Resource,
            meta: {
                requiresLogin: true
            }
        },
    ]
});