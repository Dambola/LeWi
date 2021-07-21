import Vue from 'vue'

const perms = {
	music: {
		add: 'ADD_MUSIC',
		remove: 'REM_MUSIC',
		edit: 'EDT_MUSIC',
	},
}

Vue.prototype.$perms = perms;

export { perms };