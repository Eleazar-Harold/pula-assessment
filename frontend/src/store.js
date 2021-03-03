/*jshint esversion: 6 */
import Vue from 'vue';
import Vuex from 'vuex';
import { api } from './axios.api';

Vue.use(Vuex);
export default new Vuex.Store({
    state: {
        accessToken: null,
        ApiData: '',
    },
    mutations: {
        updateStorage(state, { access }) {
            state.accessToken = access;
        },
        destroyToken(state) {
            state.accessToken = null;
        }
    },
    getters: {
        loggedIn(state) {
            return state.accessToken != null;
        }
    },
    actions: {
        userLogout(context) {
            if (context.getters.loggedIn) {
                context.commit('destroyToken');
            }
        },
        userLogin(context, usercredentials) {
            return new Promise((resolve, reject) => {
                api.post('token/obtain/', {
                    username: usercredentials.username,
                    password: usercredentials.password
                })
                    .then(response => {
                        context.commit('updateStorage', { access: response.data.token });
                        resolve();
                    })
                    .catch(err => {
                        reject(err);
                    });
            });
        },
        userRegister(context, usercredentials) {
            return new Promise((resolve, reject) => {
                api.post('token/generate/', {
                    username: usercredentials.username,
                    password: usercredentials.password,
                    password2: usercredentials.password2,
                    email: usercredentials.email,
                    first_name: usercredentials.first_name,
                    last_name: usercredentials.last_name
                })
                    .then(response => {
                        context.commit('updateStorage', { access: response.data.token });
                        resolve();
                    })
                    .catch(err => {
                        reject(err);
                    });
            });
        }
    }
});