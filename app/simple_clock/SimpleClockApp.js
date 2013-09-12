/**
 * @jsx React.DOM
 */

var React = require('React');
var SimpleClock = require('SimpleClock');

var SimpleClockApp = React.createClass({
  render: function() {
    return (
      <SimpleClock startTime={(new Date()).getTime()}/>
    );
  }
});

module.exports = SimpleClockApp;
