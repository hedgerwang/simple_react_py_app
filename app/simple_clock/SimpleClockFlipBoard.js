
/**
 * @jsx React.DOM
 */

var React = require('React');
var ReactPropTypes = require('ReactPropTypes');

var SimpleClockFlipBoard = React.createClass({
  propTypes: {
    value: ReactPropTypes.string.isRequired
  },

  /**
   * @return {object}
   */
  getInitialState: function() {
    return {
      from: this.props.value,
      to: this.props.value
    }
  },

  /**
   * @param {object} nextProps
   */
  componentWillReceiveProps: function(nextProps) {
    clearTimeout(this._animationTimer);
    this.setState({
      from: this.state.to,
      to: nextProps.value
    });
    this._animationTimer = setTimeout(this._finishAnimation, 700);
  },

  componentWillUnmount: function() {
    clearTimeout(this._animationTimer);
    delete this._animationTimer;
  },

  render: function() {
    var from = this.state.from;
    var to = this.state.to;
    var animating = this._isAnimating();

    var classNames = [
      'SimpleClockFlipBoard_root ',
      animating && 'animating',
      from === to && 'animationComplete',
      this.props.className
    ];

    if (!animating) {
      from = to;
    }

    return (
      <div class={classNames.join(' ')}>
        <div class="SimpleClockFlipBoard_p1">{from}</div>
        <div class="SimpleClockFlipBoard_p2">{from}</div>
        <div class="SimpleClockFlipBoard_p3">{to}</div>
        <div class="SimpleClockFlipBoard_p4">{to}</div>
        <div class="SimpleClockFlipBoard_p0">{to}</div>
      </div>
    );
  },

  _isAnimating: function() {
    return (this.state.from !== this.state.to) &&
      this.isMounted() &&
      ('-webkit-transform' in this.getDOMNode().style);
  },

  _finishAnimation: function() {
    this.setState({
      from: this.state.to,
      to: this.state.to
    });
  }
});

module.exports = SimpleClockFlipBoard;
