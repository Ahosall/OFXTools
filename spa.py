import webview
import threading
import watchfiles

from src.utils import Api

def watch_and_reload(window, event):
  for change in watchfiles.watch('src/', stop_event=event):
    window.evaluate_js('window.location.reload()')

if __name__ == '__main__':
  api = Api()
  print(api)
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
    target = watch_and_reload,
    args = (window, thread_running)
  )
  reload_thread.start()
  
  webview.start(window, debug=True)

  thread_running.clear()
  reload_thread.join()

  print('exitted successfully!')
