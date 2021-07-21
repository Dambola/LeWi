import Vue from 'vue'
import { uuid } from 'vue-uuid'; 

// const mutations = {
//   // createMusic (state, payload) {
//   //   Vue.set(state.musics, payload.id, payload.music);
//   // }
// };

export function updateMusic (state, payload) {
  Object.assign(state.musics[payload.id], payload);
};

export function deleteMusic (state, id) {
  Vue.delete(state.musics, id);
};

export function reloadMusics (state, musics) {
  musics.forEach((music) => {
    const key = uuid.v1();
    music['id'] = key;
    Vue.set(state.musics, key, music);
  });
}