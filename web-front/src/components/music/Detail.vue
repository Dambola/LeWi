<template>
  <q-dialog 
    :value="value"
    :full-width="true"
    @hide="hide"
  >
    <q-card 
      v-if="target === 'detail'"
    >
      <!-- Header Session -->
      <q-card-section class="row">
        <div class="text-h6">Música</div>
        <q-space />
        <q-btn flat round dense v-close-popup icon="close" />
      </q-card-section>

      <!-- Music Session -->
      <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col q-mr-sm">
            <div class="row">
              <span class="text-subtitle2">Nome:</span>
            </div>
            <div class="row">
              <small>{{ music.name }}</small>
            </div>
          </div>
          <div class="col">
            <div class="row">
              <span class="text-subtitle2">Autor:</span>
            </div>
            <div class="row">
              <small>{{ music.author }}</small>
            </div>
          </div>
        </div>

        <!-- Type Session -->
        <div class="row q-mt-sm">
          <div class="col">
            <div class="row">
              <div class="col"><span class="text-subtitle2">Tipo:</span></div>
            </div>
            <div class="row text-center">
              <div class="col">
                <small>{{ music.type1 || "-" }}</small>
              </div>
              <div class="col">
                <small>{{ music.type2 || "-" }}</small>
              </div>
              <div class="col">
                <small>{{ music.type3 || "-" }}</small>
              </div>
            </div>
          </div>
        </div>

        <!-- Actions Session -->
        <div class="row text-center q-pt-lg">
          <div class="col">
            <q-btn
              icon="fas fa-trash-alt"
              size="sm"
              class="q-mx-md text-white bg-red-6"
              v-if="removable"
              @click="target = 'remove'"
            />
            <q-btn
              icon="fas fa-edit"
              size="sm"
              class="q-mx-md text-white bg-yellow-6"
              v-if="editable"
              @click="openEdit"
            />
            <!-- <q-btn 
                icon="fas fa-external-link-square-alt" 
                size="sm" 
                class="q-mx-md text-white bg-green-13" 
            /> -->
          </div>
        </div>
      </q-card-section>
    </q-card>

    <q-card
      v-if="target === 'edit'"
    >
      <q-card-section class="row">
        <div class="text-h6">Editar música</div>
        <q-space />
        <q-btn 
          flat
          round
          dense
          v-close-popup
          icon="close"
        />
      </q-card-section>
      <form @submit.prevent="submitEditForm">
        <q-card-section class="q-pt-none">
          <div class="row">
            <q-input
              v-model="musicToSubmit.name"
              label="Nome da Música"
              class="col"
              ref="name"
              :rules="[val => !!val || 'Nome da música é necessário']"
            />
          </div>
          <div class="row">
            <q-input
              v-model="musicToSubmit.author"
              label="Autor da Música"
              class="col"
            />
          </div>
          <div class="row">
            <q-select 
              v-model="musicToSubmit.type1" 
              :options="options"
              label="Tipo 1" 
              class="col"
            />
          </div>
          <div class="row" v-if="musicToSubmit.type1">
            <q-select 
              v-model="musicToSubmit.type2" 
              :options="options"
              label="Tipo 2"
              class="col"
              clearable
            />
          </div>
          <div class="row" v-if="musicToSubmit.type2">
            <q-select 
              v-model="musicToSubmit.type3" 
              :options="options"
              label="Tipo 3" 
              class="col"
              clearable 
            />
          </div>

        </q-card-section>

        <q-card-actions align="right">
          <q-btn 
            label="Cancelar" 
            color="red"
            @click="reset"
          />
          <q-btn 
            label="Salvar" 
            color="primary"
            type="submit"
          />
        </q-card-actions>
      </form>
    </q-card>

    <q-card
      v-if="target === 'remove'"
    >
      <q-card-section class="row">
        <div class="text-h6">Deletar música</div>
        <q-space />
        <q-btn 
          flat
          round
          dense
          v-close-popup
          icon="close"
        />
      </q-card-section>

      <q-card-section class="row">
        <div class="row q-mt-sm">
          Você tem certeza que quer deletar a música <br>
          <strong>{{ music.name }}</strong> <span>-</span> 
          <strong>{{ music.author }}</strong> ?
        </div>
      </q-card-section>

      <q-card-actions align="right">
          <q-btn 
            label="Cancelar" 
            color="red"
            @click="reset"
          />
          <q-btn 
            label="Deletar" 
            color="primary"
            @click="submitDeleteMusic"
          />
        </q-card-actions>
      
    </q-card>
  </q-dialog>
</template>

<script>
  import { mapActions } from 'vuex';

  export default {
    props: {
      music: {
        type: Object
      },
      editable: {
        type: Boolean,
        default: false
      },
      removable: {
        type: Boolean,
        default: false
      },
      value: {
        type: Boolean,
        required: true
      }
    },
    data() {
      return {
        target: 'detail',
        options: [
          'Adoração',
          'Bíblico',
          'Clamor',
          'Comunhão',
          'Declaração',
          'Exaltação',
          'Fé',
          'Gratidão',
          'Profecia',
          'Restauração',
          'Transformação'
        ],
        musicToSubmit: null
      };
    },
    methods: {
      ...mapActions('musics', ['updateMusic', 'deleteMusic']),
      hide () {
        this.reset();
        this.$emit('close');
      },
      reset () {
        this.target = 'detail';
        this.musicToSubmit = null;
      },
      openEdit () {
        this.target = 'edit';
        console.log(this.music);
        this.musicToSubmit = {
          'id': this.music.id,
          'name': this.music.name,
          'author': this.music.author,
          'type1': this.music.type1,
          'type2': this.music.type2,
          'type3': this.music.type3,
        };
      },
      submitEditForm () {
        this.$refs.name.validate();
        if (!this.$refs.name.hasError){
          this.submitEditMusic();
        }
      },
      submitEditMusic () {
        const payload = {
          old: this.music,
          new: this.musicToSubmit
        };
        
        this.updateMusic(payload).then( _ => {
          this.hide();
        });
      },
      submitDeleteMusic () {
        const payload = {
          id: this.music.id,
          name: this.music.name,
          author: this.music.author
        };

        this.deleteMusic(payload).then(_ => {
          this.hide();
        })
      }
    }
  };
</script>