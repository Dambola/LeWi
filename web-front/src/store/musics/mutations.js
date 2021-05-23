import Vue from 'vue'

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

export function reloadMusics (state, musics) {
  musics.forEach((music) => {
    const key = (music.name, music.author);
    console.log(key, music);
    Vue.set(state.musics, key, music);
  });
}