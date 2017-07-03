import React from 'react';
import ReactDOM from 'react-dom';

import SearchBar from './components/project_list_item.js'

// make the component
const App = () => {
  return (
    <div>
      <SearchBar />
    </div>
  );
}

// load the components generated html and put it in the DOM
ReactDOM.render(<App />, document.querySelector('#app') )
