import subprocess
import sys
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class App():
    def do_GET(self):
        if self.path == "/":
            self.handle_home()
        elif self.path == "/about":
            self.handle_about()
        else:
            self.handle_404()

    def do_POST(self):
        if self.path == "/submit":
            self.handle_submit()
        else:
            self.handle_404()


def run_server():
    server = HTTPServer(("localhost", 8000), App)
    print("🌐 Server running at http://localhost:8000")
    server.serve_forever()


# --- Watchdog Auto-Reloader ---


class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None
        self.restart_server()

    def restart_server(self):
        if self.process:
            print("🔁 Restarting server...")
            self.process.kill()
        print("🚀 Starting server...")
        self.process = subprocess.Popen([sys.executable, self.script_path])

    def on_any_event(self, event):
        if event.src_path.endswith(".py") and event.src_path != __file__:
            print(f"📁 Change detected: {event.src_path}")
            self.restart_server()


def start_watcher():
    script_path = os.path.abspath(__file__)
    event_handler = ReloadHandler(script_path)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()
    print("👀 Watching for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Exiting watcher...")
        observer.stop()
        if event_handler.process:
            event_handler.process.kill()
    observer.join()
