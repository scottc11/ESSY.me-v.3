import React from 'react';
import ReactDOM from 'react-dom';

import ProjectList from './components/project_list.js'
import ProjectListItem from './components/project_list_item.js'

// make the component
const App = () => {
  return (
    <div>
      <ProjectList />
      <ProjectListItem />
    </div>
  );
}

// load the components generated html and put it in the DOM
ReactDOM.render(<App />, document.querySelector('#app') )
