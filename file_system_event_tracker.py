import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/Lenovo Franco/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Oye,{event.src_path} ha sido creado!")

    def on_deleated(self, event):
        print(f"Lo siento alguien lo borro,{event.src_path}")
    
    def on_modified(self, event):
        print(f"Hola,{event.src_path} ha sido modificado!")

    def on_moved(self, event):
        print(f"Alguien movio,{event.src_path} a {event.dest_path}!")
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive= True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Ejecutando...")
except KeyboardInterrupt:
    print("Detenido!")
    observer.stop()