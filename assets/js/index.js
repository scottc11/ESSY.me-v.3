var React = require('react');
var ReactDOM = require('react-dom');

var Hello = React.createClass({
  render: () => {
    return (
      <h1>
      Hello, React!
      </h1>
    )
  }
})

ReactDOM.render(<Hello />, document.getElementById('container'));
