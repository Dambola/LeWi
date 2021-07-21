export function reloadPermissions ({ commit }, restApi) {
  restApi.get('permission').then(response => {
    if (response.data) {
      commit('reloadPermissions', response.data);
    }
  });
};