export function reloadMusics ({ commit }, restApi) {
  restApi.get('music').then(response => {
    if (response.data) {
      commit('reloadMusics', response.data);
    }
  });
};