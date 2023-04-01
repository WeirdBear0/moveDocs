import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sourceDir = "C:/Users/ayush/Downloads"

print("press any key to stop the observer")

class FileWatcher(FileSystemEventHandler):
    def on_created (self, event):
        print(f"{event.src_path} has been created!")
    def on_modified (self, event):
        print(f"{event.src_path} has been modified!")
    def on_moved (self, event):
        print(f"{event.src_path} has been moved or renamed!")
    def on_deleted (self, event):
        print(f"{event.src_path} has been deleted!")

fileWatcher = FileWatcher()
observer = Observer()
observer.schedule(fileWatcher, sourceDir, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("observer stopped")
    observer.stop()