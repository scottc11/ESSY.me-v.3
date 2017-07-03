import React, { Component } from 'react';

class ProjectList extends Component {
  constructor(props) {
    super(props);

    this.state = { curProj: 'jkl' };
  }


  render() {
    return (
      <div>
        <div onClick={ event => this.setState({ curProj: 'selected something' }) }>The List!</div>
        <h5>{this.state.curProj}</h5>
      </div>
    );
  }

  onSelectProject(event) {
  }

}

export default ProjectList;
