/**
 * @jsx React.DOM
 */

var React = require('React');
var ReactPropTypes = require('ReactPropTypes');
var SimpleClock = require('SimpleClock');

var SimpleClockApp = React.createClass({
  propTypes: {
    runAtServer: ReactPropTypes.bool.isRequired,
    requestData: ReactPropTypes.object.isRequired
  },

  render: function() {
    var startTime = this.props.requestData.time;
    return (
      <SimpleClock startTime={startTime}/>
    );
  }
});

module.exports = SimpleClockApp;
