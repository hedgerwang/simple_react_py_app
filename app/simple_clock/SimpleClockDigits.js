
/**
 * @jsx React.DOM
 */

var React = require('React');
var ReactPropTypes = require('ReactPropTypes');
var SimpleClockFlipBoard = require('SimpleClockFlipBoard');

var SimpleClockDigits = React.createClass({
  propTypes: {
    value: ReactPropTypes.number.isRequired,
    label: ReactPropTypes.string
  },

  render: function() {
    var value = String(this.props.value);
    value = value.length < 2 ? '0' + value : value;
    value = value.length > 2 ? value.substr(0, 2) : value;
    return (
      <div class="SimpleClockDigits_root">
        <div class="SimpleClockDigits_label">{this.props.label}</div>
        <SimpleClockFlipBoard value={value} />
      </div>
    );
  }
});

module.exports = SimpleClockDigits;
