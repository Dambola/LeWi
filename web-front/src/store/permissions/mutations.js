// const mutations = {
//   // updateMusic (state, payload) {
//   //   Object.assign(state.musics[payload.id], payload);
//   // },

//   // deleteMusic (state, id) { 
//   //   Vue.delete(state.musics, id);
//   // },

//   // createMusic (state, payload) {
//   //   Vue.set(state.musics, payload.id, payload.music);
//   // }
// };

export function reloadPermissions (state, permissions) {
  state.permissions = permissions;
}