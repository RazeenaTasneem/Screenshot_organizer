import time
import os
import shutil
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import config
import processor

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            return

        time.sleep(1)
        
        category = processor.get_category(file_path)
        
        dest_folder = os.path.join(config.TARGET_DIR, category)
        os.makedirs(dest_folder, exist_ok=True)
        
        timestamp = datetime.now().strftime(config.DATETIME_FORMAT)
        new_filename = f"{timestamp}.png"
        dest_path = os.path.join(dest_folder, new_filename)
        
        try:
            shutil.move(file_path, dest_path)
            print(f"Organized: {new_filename} -> {category}")
        except Exception as e:
            print(f"Movement Error: {e}")

if __name__ == "__main__":
    if not os.path.exists(config.TARGET_DIR):
        os.makedirs(config.TARGET_DIR)

    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, config.SOURCE_DIR, recursive=False)
    
    print(f"Monitoring: {config.SOURCE_DIR}")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()