import os

# SOURCE_DIR = r"C:\Users\LENOVO\OneDrive\图片\Screenshots"
# TARGET_DIR = r"C:\Users\LENOVO\OneDrive\图片\Screenshots\Organised"

SOURCE_DIR = r"C:\Users\nn981\OneDrive\รูปภาพ\Screenshots"
TARGET_DIR = r"C:\Users\nn981\OneDrive\รูปภาพ\Screenshots\Organised"


# Tesseract-OCR Configuration used by processor.py
# IMPORTANT: This path must point to your tesseract.exe installation

# TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSERACT_PATH = r"C:\Users\nn981\AppData\Local\Programs\Tessaract_OCR\tesseract.exe"

# YOLO Configuration
# This will automatically download the model if not present
YOLO_MODEL_PATH = 'yolov8n.pt' 

CATEGORIES = {
    "Coding/Python": [
        "def ", "if __name__ ==", "import os", "print(f", "elif ", "range(", "plt.", "pandas as", "numpy as", "class "
    ],
    "Coding/Java": [
        "public static void", "System.out.print", "Scanner ", "new ArrayList", "@Override", "extends ", "implements ", "public class ", "private String"
    ],
    "Coding/Cpp": [ # Changed to Cpp to avoid special char issues in folders
        "#include <", "std::cout", "using namespace std;", "int main()", "vector<", "class ", "public:"
    ],
    "Coding/C": [
        "#include <stdio.h>", "printf(", "scanf(", "malloc(", "struct ", "free("
    ],
    "Coding/HTML_Web": [
        "<!DOCTYPE html>", "document.get", "const ", "addEventListener", "href=", "class=", "style=", "<div>", "<span>", "<html>"
    ],
    "Logins_Security": [
        "password", "username", "confirm password", "otp", "sign in", "cvv", "expiry date", "login to"
    ],
    "College/KPRIET": [
        "kpriet", "internal test", "semester", "student id", "assignment", "course code", "marks"
    ]
}

# Object Detection Categories (YOLO Class -> Folder Name)
OBJECT_CATEGORIES = {
    "person": "Objects/People",
    "bicycle": "Objects/Vehicles",
    "car": "Objects/Vehicles",
    "motorcycle": "Objects/Vehicles",
    "airplane": "Objects/Vehicles",
    "bus": "Objects/Vehicles",
    "train": "Objects/Vehicles",
    "truck": "Objects/Vehicles",
    "boat": "Objects/Vehicles",
    "traffic light": "Objects/City_Elements",
    "fire hydrant": "Objects/City_Elements",
    "stop sign": "Objects/City_Elements",
    "parking meter": "Objects/City_Elements",
    "bench": "Objects/City_Elements",
    "bird": "Objects/Animals",
    "cat": "Objects/Animals",
    "dog": "Objects/Animals",
    "horse": "Objects/Animals",
    "sheep": "Objects/Animals",
    "cow": "Objects/Animals",
    "elephant": "Objects/Animals",
    "bear": "Objects/Animals",
    "zebra": "Objects/Animals",
    "giraffe": "Objects/Animals",
    "backpack": "Objects/Personal_Items",
    "umbrella": "Objects/Personal_Items",
    "handbag": "Objects/Personal_Items",
    "tie": "Objects/Personal_Items",
    "suitcase": "Objects/Personal_Items",
    "frisbee": "Objects/Sports",
    "skis": "Objects/Sports",
    "snowboard": "Objects/Sports",
    "sports ball": "Objects/Sports",
    "kite": "Objects/Sports",
    "baseball bat": "Objects/Sports",
    "baseball glove": "Objects/Sports",
    "skateboard": "Objects/Sports",
    "surfboard": "Objects/Sports",
    "tennis racket": "Objects/Sports",
    "bottle": "Objects/Kitchen_Dining",
    "wine glass": "Objects/Kitchen_Dining",
    "cup": "Objects/Kitchen_Dining",
    "fork": "Objects/Kitchen_Dining",
    "knife": "Objects/Kitchen_Dining",
    "spoon": "Objects/Kitchen_Dining",
    "bowl": "Objects/Kitchen_Dining",
    "banana": "Objects/Food",
    "apple": "Objects/Food",
    "sandwich": "Objects/Food",
    "orange": "Objects/Food",
    "broccoli": "Objects/Food",
    "carrot": "Objects/Food",
    "hot dog": "Objects/Food",
    "pizza": "Objects/Food",
    "donut": "Objects/Food",
    "cake": "Objects/Food",
    "chair": "Objects/Furniture",
    "couch": "Objects/Furniture",
    "potted plant": "Objects/Nature",
    "bed": "Objects/Furniture",
    "dining table": "Objects/Furniture",
    "toilet": "Objects/Furniture",
    "tv": "Objects/Tech_Devices",
    "laptop": "Objects/Tech_Devices",
    "mouse": "Objects/Tech_Devices",
    "remote": "Objects/Tech_Devices",
    "keyboard": "Objects/Tech_Devices",
    "cell phone": "Objects/Tech_Devices",
    "microwave": "Objects/Appliances",
    "oven": "Objects/Appliances",
    "toaster": "Objects/Appliances",
    "sink": "Objects/Appliances",
    "refrigerator": "Objects/Appliances",
    "book": "Objects/Books_Paper",
    "clock": "Objects/Household_Items",
    "vase": "Objects/Household_Items",
    "scissors": "Objects/Office_supplies",
    "teddy bear": "Objects/Toys",
    "hair drier": "Objects/Personal_Care",
    "toothbrush": "Objects/Personal_Care"
}
DATETIME_FORMAT = "%Y-%m-%d-%H-%M-%S"