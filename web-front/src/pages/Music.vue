<template>
  <q-page class="row items-center justify-evenly" padding>
    <list-music :musics="getMusics"/>
  </q-page>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Music',
  components: {
    'list-music' : require('components/music/List.vue').default,
  },
  computed: {
    ...mapGetters('musics', ['getMusics']),
  },
  data() {
    return {};
  },
  methods: {
    ...mapActions('musics', ['reloadMusics']),
  },
  mounted () {
    this.reloadMusics(this.$axios);
  }
}
</script>