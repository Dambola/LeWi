<template>
  <q-layout view="hHh Lpr lff">
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
      <q-tabs v-model="tab">
        <q-tab
          icon="fas fa-sign-in-alt"
          name="login"
          label="Login"
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
export default {
  name: 'MainLayout',
  data () {
    return {
      tab : 'login'
    }
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