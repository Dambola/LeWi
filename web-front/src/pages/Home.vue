<template>
  <q-page class="row items-center justify-evenly" padding>
    <div id="welcome-home" class="text-center shadow-3 col-8">
      <div id="welcome-home-title">
        <span>
          <strong>
            Bem vindo ao LeWi!
          </strong>
        </span>
      </div>
      <div id="welcome-home-text">
        <small>Aplicativo de Suporte à Equipe de Louvor (v{{ version }})</small>
      </div>
      <div id="welcome-home-icon">
        <q-icon name="fas fa-users"></q-icon>
      </div>
    </div>
  </q-page>
</template>

<script>
import { version } from '../../package.json';

export default {
  name: 'Home',
  components: {},
  data() {
    return {
      version: version,
    };
  },
  methods : {}
}
</script>

<style lang="scss">
#welcome-home {
  background-color: $primary;
  color: white;
  padding: 20px 10px;
  border-radius: 5px;
  #welcome-home-title {
    font-size: 20px;
  }
  #welcome-home-icon {
    padding-top: 1px;
    font-size: 50px;
  }
}
</style>