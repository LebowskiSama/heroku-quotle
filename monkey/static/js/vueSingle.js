let source = {
  veronica: {
    search: null,
    suggestions: [],
  },
};

var searchField = new Vue({
  el: "#root",
  vuetify: new Vuetify(),
  data: {
    search: null,
    suggestions: [],
  },
  template:`<div>
  <input id="search" v-model="search" placeholder="Pulp Fiction..."></input>
  <v-container>
    <v-layout row wrap justify="space-between">
      <v-flex xs12 sm6 md4 lg3 v-for="item in suggestions" :key="item.imdbID">
        <v-card width="200" raised class="text-xs-center ma-3" @click="parseChoice(item.imdbID)">
        <img :src="item.Poster" height="300" width="200" contain></img>
        <v-card-subtitle justify-content>{{ item.Title }}</v-card-subtitle>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</div>`,
  updated: function () {
    axios({
      method: "get",
      url: "http://www.omdbapi.com/?apikey=d0b356ff&s=" + this.search,
    }).then((response) => (this.suggestions = response.Search));
  },
  methods:{
    parseChoice: function(itemid){
      axios({
        method: 'post',
        url: '/monkeyList',
        data: {
          ID: itemid
        }})
        .then(jsonData => console.log(jsonData.quotes))
    }
  }
});