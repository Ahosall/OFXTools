import json
import ctypes
import webview
import threading
import watchfiles

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

def watch_and_reload(window, event):
  for change in watchfiles.watch('templates/', stop_event=event):
    window.evaluate_js('window.location.reload()')

if __name__ == '__main__':
  api = Api()
  window = webview.create_window(
    title = '.: OFX-Tools :.',
    url = './templates/index.html',
    width=1200,
    height=660,
    js_api=api
  )
  
  ## this handles stopping the watcher
  thread_running = threading.Event()
  thread_running.set()

  ## using a thread to watch
  reload_thread = threading.Thread(
    target = watch_and_reload,
    args = (window, thread_running)
  )
  reload_thread.start()
  
  ## start the webview app
  webview.start(window, debug=True)

  ## upon the webview app exitting, stop the watcher
  thread_running.clear()
  reload_thread.join()

  print('exitted successfully!')