/**
 * @jsx React.DOM
 */

var React = require('React');
var ReactPropTypes = require('ReactPropTypes');
var SimpleClockDigits = require('SimpleClockDigits');

var SimpleClock = React.createClass({

  propTypes: {
    startTime: ReactPropTypes.number.isRequired
  },

  /**
   * @return {object}
   */
  getInitialState: function() {
    var startTime = this.props.startTime;
    return {
      time: startTime,
      timeOffset: (new Date()) - startTime
    };
  },

  /**
   * @param {object}
   */
  componentWillReceiveProps: function(nextProps) {
    var startTime = nextProps.startTime;
    this.setState({
      time: startTime,
      timeOffset: (new Date()) - startTime
    });
  },

  componentDidMount: function() {
    this._timer = setInterval(this._tick, 1000);
  },

  componentWillUnmount: function() {
    clearInterval(this._timer);
    delete this._timer;
  },

  /**
   * @return {object}
   */
  render: function() {
    var date = new Date(this.state.time);
    var hours = date.getHours();
    var ampm = hours < 12 ? 'AM' : 'PM'
    return (
      <div class="SimpleClock_root">
        <SimpleClockDigits
          label={ampm}
          value={date.getHours()}
        />
        <SimpleClockDigits value={date.getMinutes()} />
        <SimpleClockDigits value={date.getSeconds()} />
      </div>
    );
  },

  _tick: function() {
    this.setState({
      time: (new Date()) - this.state.timeOffset
    });
  }
});

module.exports = SimpleClock;
