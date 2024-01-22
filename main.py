import os
import webview
import threading
import watchfiles

from src.utils import Api

def create_and_delete_file():
  try:
    with open('./src/.nocontent', 'w') as file:
      file.write('No Content')
    
    os.remove('./src/.nocontent')
  except Exception as e:
    print(f"Erro: {e}")

def watch_and_reload(window, event):
  print('Assiste os arquivos ae')
  files = watchfiles.watch('./src/')
  for change in files:
    if not event.is_set():
      break
    
    window.evaluate_js('window.location.reload()')

if __name__ == '__main__':
  api = Api()
  window = webview.create_window(
    title = '.: OFX-Tools :.',
    url = './src/template.html',
    width=1200,
    height=660,
    js_api=api
  )

  thread_running = threading.Event()
  thread_running.set()
  reload_thread = threading.Thread(
    target=watch_and_reload,
    args=(window, thread_running)
  )
  reload_thread.start()
  
  # TODO: Resolver BUG do refresh
  webview.start(http_server=True, debug=True)

  thread_running.clear()
  create_and_delete_file()  
  reload_thread.join()

  print('exitted successfully!')
