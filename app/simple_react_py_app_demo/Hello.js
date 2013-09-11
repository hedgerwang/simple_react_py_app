/**
 * @jsx React.DOM
 */

var React = require('React');
var World = require('World');

var Hello = React.createClass({
  render: function() {

    return (
      <div class="Hello_root">
        <World />
        <hr />
        {this.props.runAtServer ? 'Rendered by Server' : 'Rendered by Browser'}
        <hr />
        {this.state.counter}
      </div>
    );
  },

  componentDidMount: function() {
    this._timer = setInterval(this._addCounter, 500);
  },

  componentWillUnmount: function() {
    clearInterval(this._timer);
    delete this._timer;
  },

  getInitialState: function() {
    return {
      counter: 0
    }
  },

  _addCounter: function() {
    this.setState({
      counter: this.state.counter + 1
    });
  }
});

module.exports = Hello;
