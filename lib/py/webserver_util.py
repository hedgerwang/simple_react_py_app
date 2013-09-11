# System
import cgi
import execjs

# Lib
import app_config
import haste

REACT_JS_SERVER_RENDER_CODE = '''
function render() {
  %(js)s;
  var React = require('React');
  var Component = require('%(module_name)s');
  var delimiter = '%(delimiter)s';
  var callback = function(html) {
    throw new Error(delimiter + html + delimiter);
  };
  var props = {runAtServer: true, requestPath: '%(request_path)s'}
  React.renderComponentToString(Component(props), callback);
}
'''

REACT_JS_BROWSER_RENDER_CODE = '''
<script src="/%(module_name)s.js"></script>
<script>
(function() {
  var React = require('React');
  var Component = require('%(module_name)s');
  var props = {runAtServer: false, requestPath: '%(request_path)s'}
  React.renderComponent(Component(props), document.body);
})();
</script>
'''

HTML_PAGE = '''
<!doctype HTML>
<html>
<head>
<meta charset="utf-8" />
<meta version="%(version)s" />
<title>%(module_name)s</title>
<link href="/%(module_name)s.css" rel="stylesheet" type="text/css" />
</head>
<body>
%(server_render_html)s
%(browser_render_html)s
</body>
</html>
'''

_supported_file_type = {
  'css': 'text/css',
  'gif': 'image/gif',
  'html': 'text/html',
  'ico': 'image/vnd.microsoft.icon',
  'jpg': 'image/jpg',
  'js': 'application/javascript',
  'png': 'image/png',
}

def should_reload():
  return False

def render_at_server(module_name, request_path, haste_data):
  delimiter = '~' * 10
  js = REACT_JS_SERVER_RENDER_CODE % {
    'delimiter': delimiter,
    'request_path': request_path,
    'module_name': cgi.escape(module_name),
    'js': haste_data.get('js'),
  }
  ctx = execjs.compile(js)
  try:
    ctx.call('render')
    return 'None'
  except Exception as error :
    # Hack to get render HTML from `React.renderComponentToString`
    text = str(error.message)
    parts = text.split(delimiter)
    if len(parts) == 3:
      return parts[1]
    else:
      return text

def render_at_browser(module_name, request_path):
  return  REACT_JS_BROWSER_RENDER_CODE % {
    'request_path': request_path,
    'module_name': cgi.escape(module_name),
  }

def get_request_file_type(path):
  idx = path.find('?')
  if idx > -1:
    path = path[0:idx]
  idx = path.rfind('.')
  if idx > -1:
    path = path[idx + 1:]
  if path in _supported_file_type:
    return path
  else:
    return None

def get_module_name(path):
  idx = path.find('/')
  if idx == 0:
    path = path[1:]
  idx = path.find('/')
  if idx > -1:
    path = path[0:idx]
  idx = path.find('?')
  if idx > -1:
    path = path[0:idx]
  idx = path.find('.')
  if idx > -1:
    path = path[0:idx]
  return path

def handle_get(path, query_params):
  content = 'not supported'
  file_type = get_request_file_type(path) or 'html'
  mime = _supported_file_type.get(file_type) or 'text/plain'
  module_name = get_module_name(path)

  if file_type == 'js':
    data = haste.require_module_js(module_name)
    content = data.get('js')
  elif file_type == 'css':
    data = haste.require_module_css(module_name)
    content = data.get('css')
  elif file_type == 'html':
    data = haste.require_module_js(module_name)
    content = HTML_PAGE % {
      'module_name': cgi.escape(module_name),
      'browser_render_html': render_at_browser(module_name, path),
      'server_render_html': render_at_server(module_name, path, data),
      'version': cgi.escape(app_config.VERSION)
    }

  return {
    'mime': mime,
    'content': content
  }
