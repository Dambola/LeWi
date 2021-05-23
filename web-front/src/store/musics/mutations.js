import Vue from 'vue'
import { uuid } from 'vue-uuid'; 

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
    const key = uuid.v1();
    Vue.set(state.musics, key, music);
  });
}