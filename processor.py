import pytesseract
from PIL import Image
from ultralytics import YOLO
import config
import os
import cv2
from google import genai

# Initialize Gemini Client
gemini_client = None
if config.GEMINI_API_KEY and config.GEMINI_API_KEY != "YOUR_GEMINI_API_KEY":
    try:
        gemini_client = genai.Client(api_key=config.GEMINI_API_KEY)
    except Exception as e:
        print(f"Error initializing Gemini Client: {e}")

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

def analyze_screenshot(image_path):
    """
    Determines the category of the screenshot and extracts text.
    Returns (category, extracted_text)
    """
    try:
        # Step 1: YOLO Detection
        detections = detect_objects(image_path)
        print(f"DEBUG: Detections in {os.path.basename(image_path)}: {detections}")

        category = None
        # Check if any detected object maps to a category
        for detection in detections:
            if detection in config.OBJECT_CATEGORIES:
                category = config.OBJECT_CATEGORIES[detection]
                print(f"DEBUG: Mapped object '{detection}' to category '{category}'")
                break

        # Step 2: OCR Text Extraction
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img).lower()
        
        if category:
            return category, extracted_text

        # Step 3: Keyword Matching for Categorization
        for cat, keywords in config.CATEGORIES.items():
            for word in keywords:
                if word.lower() in extracted_text:
                    print(f"DEBUG: Matched keyword '{word}' for category '{cat}'")
                    return cat, extracted_text
        
        return "General", extracted_text

    except Exception as e:
        print(f"Processing Error: {e}")
        return "Unprocessed_Errors", ""

def generate_smart_name(text, category):
    """
    Uses Gemini AI to generate a smart name based on the screenshot text.
    """
    import re
    
    def get_fallback():
        cat_safe = category.replace("/", "-").lower()
        if not text.strip():
            return f"{cat_safe}-snap"
        words = re.findall(r'[a-zA-Z0-9]+', text)
        if words:
            return "-".join(words[:3]).lower()
        return f"{cat_safe}-snap"

    if gemini_client is None:
        return get_fallback() # Fallback if no API key or failed to init
        
    try:
        prompt = f"Given this text extracted from a screenshot categorized as '{category}', suggest a short, descriptive file name (2-3 words max, separated by hyphens). Do not include the file extension, do not include markdown blocks, just return the raw text. Text: {text[:1000]}"
        response = gemini_client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt,
        )
        name = response.text.strip().lower()
        # Clean up any weird characters
        name = "".join(c for c in name if c.isalnum() or c == '-')
        if not name: 
            return get_fallback()
        return name
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return get_fallback()
