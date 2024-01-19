import webview
import threading
import watchfiles

from src.utils import Api

def watch_and_reload(window, event):
  print(window, 'Watch Load', event)
  for change in watchfiles.watch('./src/'):
    print("Atualizae")
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
  webview.start(None, window,  http_server=True, debug=True)

  thread_running.clear()
  reload_thread.join()

  print('exitted successfully!')
