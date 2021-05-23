import Vue from 'vue'
import axios from 'axios'
import Router from '../router'

const api = axios.create({
	baseURL: JSON.parse(process.env.API_URL),
	withCredentials: true, 
	headers: {
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*'
	}
});

api.interceptors.response.use(
	(response) => {
		return response
	},

	(error) => {
		const response = error.response;
		if (401 === response.status && response.data.mustReload) {
			localStorage.removeItem('login');
			localStorage.removeItem('email');

			const router = Router();
			router.push({ path: '/login' });
		}

		return Promise.reject(error)
	}
);

Vue.prototype.$axios = api;

export { api };