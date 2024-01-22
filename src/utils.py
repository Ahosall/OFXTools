import os
import json
import ctypes

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
  return f'/{entry[:-1] if not entry == "" and entry[-1] == "/" else entry}'

def getRoutes():
  _routes = []
  paths = [f'{root}/{file}'.replace('//', '/').replace('\\', '/') for root, folders, files in os.walk(PAGES_PATH) for file in files]

  for path in paths:
    if path.endswith('route.html'):
      with open(f'{path}', 'r+', encoding='utf-8') as f:
        threat = path.replace(PAGES_PATH, '').replace('/', '-')
        lines = f.readlines()
        findScript = [line for line in lines if line.upper().startswith('<!-- ::')]
        script = findScript[0] if len(findScript) else None
        if script:
          with open("src/"+script.split("::")[1], 'r+', encoding='utf-8') as f:
            script = f.read()
        _routes.append({
          'path': extends(threat), 
          'doc': ''.join(lines),
          'script': script
        })
  return _routes

def getCompanies(config):
  _companies = []
  for path in list(config.keys()):
    for root, folders, files in os.walk(config[path]):
      for folder in folders:
        _companies.append(folder)
      break
  return _companies
class Api:
  def getUsername(self):
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = 3
 
    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)
 
    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    return {'user': nameBuffer.value}
  
  def getConfig(self):
    config = None
    try:
      with open('./config.json', 'r+') as f:
        config = json.loads(f.read())

      return config
    except Exception as e:
      print(e)
      return None
    
  def saveConfig(self, data: dict) -> bool:
    try:
      with open('./config.json', 'w+') as f:
        f.write(json.dumps(data))
      return True
    except Exception as e:
      print(e)
      return False
  
  def companies(self):
    return getCompanies(self.getConfig())

  def routes(self):
    return getRoutes()