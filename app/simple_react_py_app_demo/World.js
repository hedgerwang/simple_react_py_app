/**
 * @jsx React.DOM
 */

var React = require('React');

var World = React.createClass({
  render: function() {
    return (
      <button class="World_root" onClick={this._onClick}>
        World
      </button>
    );
  },

  _onClick: function() {
    alert('hi');
  }
});

module.exports = World;
