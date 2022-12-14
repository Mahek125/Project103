import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#path for the directory to track
from_dir = "C:/Users/mitul/Desktop/Mahek Projects/sampleFolder"

#event handler class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"{event.src_path} has been created")

    def on_deleted(self,event):
        print(f"{event.src_path} has been deleted")

    def on_modified(self, event):
        print(f"{event.src_path} has been modified")

    def on_moved(self, event):
        print(f"{event.src.path} has been moved or renamed")

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    Observer.stop()