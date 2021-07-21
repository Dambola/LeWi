<template>
  <q-page class="row items-center justify-evenly" padding>
    <list-music 
      :musics="getMusics"
      @select="selectMusic"
    />
    <detail-music
      v-model="showDetail" 
      :music="selectedMusic"
      :editable="canEditMusic"
      :removable="canRemoveMusic"
      @close="closeDetail"
    />
  </q-page>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Music',
  components: {
    'list-music' : require('components/music/List.vue').default,
    'detail-music' : require('components/music/Detail.vue').default,
  },
  computed: {
    ...mapGetters('musics', ['getMusics']),
    ...mapGetters('permissions', ['getPermissions']),
    canEditMusic () {
      return this.$perms.music.add in this.getPermissions;
    },
    canRemoveMusic () {
      return this.$perms.music.remove in this.getPermissions;
    },
  },
  data() {
    return {
      showDetail: false,
      selectedMusic: {}
    };
  },
  methods: {
    ...mapActions('musics', ['reloadMusics']),
    closeDetail () {
      this.showDetail = false;
    },
    selectMusic (music) {
      this.selectedMusic = music;
      this.showDetail = true;
    }
  },
  mounted () {
    this.reloadMusics();
  }
}
</script>