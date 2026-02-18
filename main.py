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


        # Wait a bit for the file to be fully written
        time.sleep(2)
        
        print(f"Processing: {os.path.basename(file_path)}")
        try:
            category = processor.get_category(file_path)
            if category == "Unprocessed_Errors":
                print(f"Warning: Could not categorize {os.path.basename(file_path)}. Moving to 'Unprocessed_Errors'.")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            category = "Unprocessed_Errors"
        
        dest_folder = os.path.join(config.TARGET_DIR, category)
        try:
            os.makedirs(dest_folder, exist_ok=True)
            
            timestamp = datetime.now().strftime(config.DATETIME_FORMAT)
            new_filename = f"{timestamp}.png"
            dest_path = os.path.join(dest_folder, new_filename)
            
            shutil.move(file_path, dest_path)
            print(f"Organized: {new_filename} -> {category}\n")
        except Exception as e:
            print(f"Movement Error for {file_path}: {e}")

if __name__ == "__main__":

    if not os.path.exists(config.TARGET_DIR):
        os.makedirs(config.TARGET_DIR)

    if not os.path.exists(config.TESSERACT_PATH):
        print(f"ERROR: Tesseract unsupported or not found at: {config.TESSERACT_PATH}")
        print("Please install Tesseract-OCR and update the path in config.py.")
        print("Download: https://github.com/UB-Mannheim/tesseract/wiki")
        input("Press Enter to exit...")
        exit(1)

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