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
  <input id="search" v-model="search"></input>
  <v-container>
  <v-row justify="space-between">
  <v-col cols="auto">
  <img v-for="item in suggestions" :key="item.imdID" :src=item.Poster height="300" width="200" contain></img>
  </v-col>
  </v-row>
  </v-container>
</div>`,
  updated: function () {
    axios({
      method: "get",
      url: "http://www.omdbapi.com/?apikey=d0b356ff&s=" + this.search,
    }).then((response) => (this.suggestions = response.Search));
  }
});