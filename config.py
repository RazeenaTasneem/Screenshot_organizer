
import os

SOURCE_DIR = r"C:\Users\LENOVO\OneDrive\图片\Screenshots"
TARGET_DIR = r"C:\Users\LENOVO\OneDrive\图片\Screenshots\Organised"


# Tesseract-OCR Configuration used by processor.py
# IMPORTANT: This path must point to your tesseract.exe installation
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
DATETIME_FORMAT = "%Y-%m-%d-%H-%M-%S"