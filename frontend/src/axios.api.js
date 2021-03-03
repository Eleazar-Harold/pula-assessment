/*jshint esversion: 6 */
import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:4000/api/v1/',
    timeout: 1000,
});

export {
    api
};