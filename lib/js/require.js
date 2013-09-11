var require = require;
var provide = provide;

(function() {
  if (typeof require !== 'undefined') {
    return;
  }

  var definedModules = {};
  var exportedModules = {}
  var global = this;
  if (!global) {
    if (typeof window !== 'undefined') {
      global = window;
    } else {
      global = {};
    }
  }

  require = function(name) {
    var fn = definedModules[name];
    if (!fn) {
      throw new Error('Module "' + name + '" is undefined');
    }

    if (!exportedModules[name]) {
      var module = {};
      fn(global, module);
      if (!module.exports) {
        throw new Error('Module "' + name + '" has no exports');
      }
      exportedModules[name] = module.exports;
    }

    return exportedModules[name];
  };

  define = function(name, fn) {
    if (!definedModules[name]) {
      definedModules[name] = fn;
    }
  };
})();
