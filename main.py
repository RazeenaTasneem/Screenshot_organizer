import time
import os
import shutil
import queue
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import config
import processor
import ui_popup

# Queue to handle threading issues between Watchdog and Tkinter
event_queue = queue.Queue()

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            return

        # Wait a bit for the file to be fully written
        time.sleep(2)
        
        print(f"Detected: {os.path.basename(file_path)}")
        event_queue.put(file_path)

def process_screenshot(file_path):
    print(f"Processing: {file_path}")
    try:
        category, text = processor.analyze_screenshot(file_path)
        smart_name = processor.generate_smart_name(text, category)
        
        # Show UI Popup in Main Thread
        result = ui_popup.show_popup(file_path, smart_name, category)
        
        if not result["confirmed"]:
            print(f"User cancelled saving {os.path.basename(file_path)}. Deleting file.")
            if os.path.exists(file_path):
                os.remove(file_path)
            return
            
        final_name = result["name"]
        final_category = result["category"]
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        final_category = "Unprocessed_Errors"
        final_name = "error"
    
    dest_folder = os.path.join(config.TARGET_DIR, final_category)
    
    try:
        os.makedirs(dest_folder, exist_ok=True)
        
        timestamp = datetime.now().strftime("%H-%M-%S")
        new_filename = f"{final_name}-{timestamp}.png"
        dest_path = os.path.join(dest_folder, new_filename)
        
        shutil.move(file_path, dest_path)
        print(f"Organized: {new_filename} -> {dest_folder}\n")
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
            # Check for new items in the queue every half second
            try:
                file_path = event_queue.get(timeout=0.5)
                process_screenshot(file_path)
            except queue.Empty:
                pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()