import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import { connect } from 'react-redux';
import * as actions from '../actions';

class App extends Component {
  componentDidMount = () => {
    this.getStatus();
  };

  getStatus = () => {
    axios
      .get('/api')
      .then(res => {
        const { status } = res.data;
        console.log(status);
        this.props.updateStatus(status);
      })
      .catch(err => {
        this.props.updateStatus('Offline');
      });
  };

  render() {
    return (
      <div className="App">
        <p>Current status: {this.props.status}</p>
        <button onClick={this.getStatus}>Update</button>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  status: state.status,
});

export default connect(
  mapStateToProps,
  actions
)(App);
