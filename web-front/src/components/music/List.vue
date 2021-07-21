<template>
  <q-markup-table class="lam-table-music col-12" :wrap-cells="true">
    <thead>
      <tr>
        <th class="text-left relative-position"> Música </th>
        <th class="text-right"> Típos </th>
      </tr>
    </thead>

    <tbody>
      <tr 
        v-for="(music, index) in musics" 
        :key="index"
        @click="selectMusic(music)"
      >
        <td class="text-left">
          <div class="text-subtitle1">
            <strong>{{ music.name }}</strong>
          </div>
          <small>{{ music.author }}</small>
        </td>

        <td class="text-right">
          <div>{{ music.type1 }}</div>
          <div>{{ music.type2 }}</div>
          <div>{{ music.type3 }}</div>
        </td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<script>
  export default {
    props: {
      musics: {
        type: Object
      }
    },
    methods: {
      selectMusic (music) {
        this.$emit('select', music);
      }
    }
  }
</script>

<style lang="scss">
.lam-table-music {
  margin: 25px 0px;
  white-space: normal !important;
  thead > tr {
    background-color: $lam-music-header;
    color: white;
    th {
      font-size: 20px;
      font-weight: 1000;
      padding-top: 15px;
      padding-bottom: 15px;
    }
  }
  tbody > tr:nth-child(2n) { background-color: $lam-music-even; }
  tbody > tr:nth-child(2n+1) { background-color: $lam-music-odd ; }
  tbody > tr:hover { background-color: $lam-music-hover ; }
}
</style>