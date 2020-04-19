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
  template:`
  <div>
    <input id="search" v-model="search"></input>
  </div>`,
  updated: function () {
    axios({
      method: "get",
      url: "http://www.omdbapi.com/?apikey=d0b356ff&s=" + this.search,
    }).then((response) => (this.suggestions = response.Search));
  }
});