import os

# SETTINGS
PAGES_PATH = 'src/pages/'

def extends(entry):
  replaces = [
    ('-', '/'),
    ('#', ':'),
    ('home', ''),
    ('.route.html', ''),
  ]

  for r in replaces:
    entry = entry.replace(r[0], r[1])
  return f'/{entry}'

def getRoutes():
  _routes = []
  paths = [f'{root}/{file}'.replace('//', '/').replace('\\', '/') for root, folders, files in os.walk(PAGES_PATH) for file in files]

  for path in paths:
    if path.endswith('route.html'):
      with open(f'{path}', 'r+', encoding='utf-8') as f:
        threat = path.replace(PAGES_PATH, '').replace('/', '-')
        _routes.append({
          'path': extends(threat), 
          'doc': f.read()
        })
  return _routes

class Api:
  def routes(self):
    return getRoutes()