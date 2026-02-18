
import pytesseract
from PIL import Image
from ultralytics import YOLO
import config
import os
import cv2

# Initialize OCR
pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH

# Initialize YOLO Model
# This will load the model once when the module is imported
try:
    model = YOLO(config.YOLO_MODEL_PATH)
except Exception as e:
    print(f"Error loading YOLO model: {e}")
    model = None

def detect_objects(image_path):
    """
    Runs YOLO detection on the image.
    Returns a list of detected class names.
    """
    if model is None:
        return []
    
    try:
        results = model(image_path, verbose=False) # Run inference
        detected_classes = []
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                detected_classes.append(class_name)
        return list(set(detected_classes)) # Return unique detected objects
    except Exception as e:
        print(f"YOLO Detection Error: {e}")
        return []

def get_category(image_path):
    """
    Determines the category of the screenshot using YOLO and OCR.
    """
    try:
        # Step 1: YOLO Detection
        detections = detect_objects(image_path)
        print(f"DEBUG: Detections in {os.path.basename(image_path)}: {detections}")

        # Check if any detected object maps to a category
        for detection in detections:
            if detection in config.OBJECT_CATEGORIES:
                category = config.OBJECT_CATEGORIES[detection]
                print(f"DEBUG: Mapped object '{detection}' to category '{category}'")
                return category

        # Step 2: OCR Text Extraction
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img).lower()
        
        # Step 3: Keyword Matching for Categorization
        for category, keywords in config.CATEGORIES.items():
            for word in keywords:
                if word.lower() in extracted_text:
                    print(f"DEBUG: Matched keyword '{word}' for category '{category}'")
                    return category
        
        return "General"

    except Exception as e:
        print(f"Processing Error: {e}")
        return "Unprocessed_Errors"