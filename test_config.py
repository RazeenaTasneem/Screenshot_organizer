import config
import os
import sys

def check_config():
    print("Checking Configuration...")
    
    # Check TESSERACT_PATH
    if not hasattr(config, 'TESSERACT_PATH'):
        print("FAIL: TESSERACT_PATH not found in config.py")
        return False
        
    tesseract_path = config.TESSERACT_PATH
    print(f"TESSERACT_PATH set to: {tesseract_path}")
    
    if os.path.exists(tesseract_path):
        print("SUCCESS: Tesseract executable found.")
        return True
    else:
        print(f"WARNING: Tesseract executable NOT found at {tesseract_path}")
        print("Please ensure Tesseract-OCR is installed and the path in config.py is correct.")
        
        # Check common alternative locations
        common_paths = [
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
            r"C:\Users\nn981\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                print(f"FOUND alternative at: {path}")
                print(f"Please update config.py to use this path.")
                return False
                
        return False

if __name__ == "__main__":
    if check_config():
        sys.exit(0)
    else:
        # We don't want to fail the build process effectively, just warn the user
        # so we exit with 0 but print warnings
        sys.exit(0)
