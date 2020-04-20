var searchField = new Vue({
  el: "#root",
  vuetify: new Vuetify(),
  data: {
    search: null,
    suggestions: [],
    quotes: null
  },
  template:`<div>
  <input id="search" v-model="search" v-on:input="callOMDB" placeholder="Pulp Fiction..."></input>
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
  <div id='quotes'>
    <p v-for='quote in quotes' :key='quote.id'><span v-html="quote"></span></p>
  </div>
</div>`,
  methods:{
    callOMDB: function(){
      axios({
        method: "get",
        url: "http://www.omdbapi.com/?apikey=d0b356ff&s=" + this.search,
      }).then((response) => (this.suggestions = response.Search));
    },
    parseChoice: function(itemid){
      axios({
        method: 'post',
        url: '/monkeyList',
        data: {
          ID: itemid
        }})
        .then(jsonData => this.quotes=jsonData.quotes)
    }
  }
});