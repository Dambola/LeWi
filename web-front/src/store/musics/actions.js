import { api } from '../../boot/axios';

export function deleteMusic ({ commit }, payload) {
  const data = {
    name: payload.name,
    author: payload.author
  };

  console.log(payload);

  api.delete('music', { data: data }).then(_ => {
    const musicId = payload.id;

    console.log(musicId);

    commit('deleteMusic', musicId);
  });
};

export function updateMusic ({ commit }, payload) {
  const data = {
    oldName: payload.old.name,
    oldAuthor: payload.old.author,
    name: payload.new.name,
    author: payload.new.author,
    type1: payload.new.type1,
    type2: payload.new.type2,
    type3: payload.new.type3
  }
  
  api.post('music', data).then(_ => {
    const newMusic = {
      id: payload.new.id,
      name: payload.new.name,
      author: payload.new.author,
      type1: payload.new.type1,
      type2: payload.new.type2,
      type3: payload.new.type3
    };

    commit('updateMusic', newMusic);
  });
};

export function reloadMusics ({ commit }) {
  api.get('music').then(response => {
    if (response.data) {
      commit('reloadMusics', response.data);
    }
  });
};