<template>
  <q-layout view="hHh LpR lFf">
    <q-header id="menu-header" elevated>
      <q-toolbar id="menu-toolbar">
        <q-toolbar-title class="text-center">
          <img 
            id="menu-logo" 
            src="../assets/logobordered.png" 
            class="vertical-middle"
          />
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-footer elevated>
      <q-tabs>
        <q-route-tab
          v-for="(item,index) in menuItems"
          :key="index"
          :icon="item.icon" 
          :label="item.title"
          :to="item.link"
          exact
        />
      </q-tabs>
    </q-footer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'MainLayout',
    data () {
      return {
        leftDrawerOpen: false,
        menuItems: [
          {
            title: 'Home',
            caption: 'Início',
            icon: 'fas fa-home',
            link: '/'
          },
          {
            title: 'Música',
            caption: 'Lista de Músicas',
            icon: 'fas fa-music',
            link: '/musica'
          }
        ]
      }
    },
    methods: {
    ...mapActions('permissions', ['reloadPermissions']),
  },
    mounted () {
      this.reloadPermissions(this.$axios);
    }
  }
</script>

<style lang="scss">
#menu-header {
  #menu-toolbar {
    height: 60px;
    #menu-logo {
      width: 90px; 
      padding-right: 15px;
      text-shadow: 1px 1px white;
    }
    #menu-text {
      font-size: 25px;
    }
  }
}
</style>