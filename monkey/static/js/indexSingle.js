class App extends React.Component {

  state = {
    suggestions : [],
    quotes: []
  }

  getSuggestions = query => {
    fetch(`http://www.omdbapi.com/?apikey=d0b356ff&s=${query}`)
      .then(response => response.json())
      .then((jsonData) => {
        let suggestions = []

        jsonData.Search.map(result => {
          let temp = {
            title: result.Title,
            year: result.Year,
            id: result.imdbID,
            poster: result.Poster,
          }
          suggestions.push(temp)
        })

        this.setState({
          suggestions
        })
    })
  }

  getQuotes = id => {
    let pootang = JSON.stringify({
      ID: id,
    });
    axios({
      method: 'post',
      url: '/monkeyList',
      data: pootang})
      .then(res => {
        this.setState({
          quotes: res.data.quotes
        })
      })
  }

  render() {
    return(
      <div>
        <Home name={this.state.name} getSuggestions={this.getSuggestions} suggestions={this.state.suggestions} getQuotes={this.getQuotes}/>
            <Result quotes={this.state.quotes}/> 
        
      </div>
    )
  }
}

class Result extends React.Component {
  render() {
    return(
        <div>
          {/* {this.props.quotes.length === 0 ? (
            ""
          ) : (
            <div> */}
              {this.props.quotes.map(line => (
                <div dangerouslySetInnerHTML={{__html: line}} />
              ))}
            {/* </div>
          )} */}
          
        </div>
    )
  }
}

class Home extends React.Component {  
  render() {
    return (
      <div>
        <h1>{this.props.name}</h1>
        <TitleForm getSuggestions={this.props.getSuggestions}/>
        <Suggestions suggestions={this.props.suggestions} getQuotes={this.props.getQuotes}/>
      </div>
    )
  }
}

class Suggestions extends React.Component {
  render() {
    return (
      <div>
        <div className="suggestions_container" >
        {this.props.suggestions.map((suggestion, index) => (
          <div className="suggestion" key={index} onClick={() => this.props.getQuotes(suggestion.id) } >
            <img className="suggestion_poster" src={suggestion.poster} alt={suggestion.name}/>
            <h5 className="suggestion_title">{suggestion.title} ({suggestion.year})</h5>
          </div>
        ))}
        </div>
      </div>
    )
  }
}

class TitleForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {query: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({query: event.target.value});
    this.props.getSuggestions(event.target.value);
  }

  handleSubmit(event){
    event.preventDefault();
  }

  render() {
    return (
    <input type="text" id ='search' placeholder="Pulp Fiction" value={this.state.value} onChange={this.handleChange} />
    );
  }
}

ReactDOM.render(<App />, document.getElementById('root'));