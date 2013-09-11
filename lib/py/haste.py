# system
from os import curdir, sep
from react import jsx
import os
import re

# lib
import app_config

RE_REQUIRE = re.compile(
  r'''[=\s]require\(["'](?P<path>[a-zA-Z0-9\/\.\$]+)["']\)[;\s\.]?'''
)

MODULE_TEXT_TEMPLATE = '''
define('%(module_name)s', function(global, module) {
  %(text)s
});
'''

_transformer = jsx.JSXTransformer()
_cached_text = {}

def _get_js_file_text(path):
  key = path + '@' + str(os.path.getmtime(path))
  if key in _cached_text:
    return _cached_text[key]
  text = _transformer.transform(path)
  _cached_text[key] = text
  return text

def _get_css_file_text(path):
  key = path + '@' + str(os.path.getmtime(path))
  if key in _cached_text:
    return _cached_text[key]
  f = open(curdir + sep + path)
  text = f.read()
  f.close()
  _cached_text[key] = text
  return text

def _extract_js_requires(text):
  requires = []
  for match in RE_REQUIRE.finditer(text) :
    requires.append(match.group('path'))
  return requires

def _build_module_text(module_name, text):
  if module_name.find('./') == 0:
    module_name = module_name[2:]

  text = text.replace('require("./', 'require("')
  text = text.replace('require(\'./', 'require(\'')

  return MODULE_TEXT_TEMPLATE %  {
    'module_name': module_name,
    'text': text
  };

def _get_module_path(module_name):
  for path in app_config.JS_MODULES_PATHS:
    test_path = path + module_name + '.js'
    if (os.path.isfile(test_path)):
      return os.path.relpath(test_path)
  return None

def _require_module(module_name, texts, paths, required, options):
  if module_name in required:
    return

  required[module_name] = True
  rel_path = _get_module_path(module_name)

  if rel_path:
    text = _get_js_file_text(rel_path)
    requires = _extract_js_requires(text)
    for another_module_name in requires:
      _require_module(another_module_name, texts, paths, required, options)
    if options.get('css'):
      css_path = rel_path.replace('.js', '.css')
      if os.path.isfile(css_path):
        texts.append(_get_css_file_text(css_path))
    else:
      texts.append(_build_module_text(module_name, text))
    paths.append(rel_path)


def require_module_js(module_name):
  texts = []
  paths = []
  required = {}
  options = {'css': False}
  _require_module(module_name, texts, paths, required, options)

  if len(texts) > 0:
    texts = [_get_js_file_text(app_config.JS_LIB_PATH + 'require.js')] + texts

  return {
    'paths': paths,
    'js': '\n'.join(texts)
  }

def require_module_css(module_name):
  texts = []
  paths = []
  required = {}
  options = {'css': True}
  _require_module(module_name, texts, paths, required, options)
  return {
    'paths': paths,
    'css': '\n'.join(texts)
  }

def test_jsx():
  print _get_js_file_text(_get_module_path('Hello'))

def test_require_module_paths():
  meta = require_module('Hello')
  print '\n'.join(meta.get('paths'))

def test_require_module_text():
  meta = require_module('Hello')
  print meta.get('js')

def main():
  # test_jsx()
  test_require_module_paths()

if __name__ == '__main__':
  main()
