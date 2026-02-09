import pytesseract
from PIL import Image
import config
import os

pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH

def get_category(image_path):
    try:
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img).lower()

        for category, keywords in config.CATEGORIES.items():
            for word in keywords:
                if word.lower() in extracted_text:
                    return category
        
        return "General"

    except Exception as e:
        return "Unprocessed_Errors"