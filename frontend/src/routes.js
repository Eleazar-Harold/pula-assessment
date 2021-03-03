/*jshint esversion: 6 */
import Vue from 'vue';
import VueRouter from 'vue-router';
import Farm from './views/Farm';
import Login from './views/Login';
import Logout from './views/Logout';
import Harvest from './views/Harvest';
import Resource from './views/Resource';

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'farms',
            component: Farm,
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
            path: '/harvest',
            name: 'harvest',
            component: Harvest,
        },
        {
            path: '/resource',
            name: 'resource',
            component: Resource,
        },
    ]
});