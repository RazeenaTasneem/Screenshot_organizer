
import os

SOURCE_DIR = r"C:\Users\nn981\OneDrive\รูปภาพ\Screenshots"
TARGET_DIR = r"C:\Users\nn981\OneDrive\รูปภาพ\Screenshots\Organised"

# Tesseract-OCR Configuration used by processor.py
# IMPORTANT: This path must point to your tesseract.exe installation
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

CATEGORIES = {
    "Coding/Python": [
        "def ", "if __name__ ==", "import os", "print(f", "elif ", "range(", "plt.", "pandas as"
    ],
    "Coding/Java": [
        "public static void", "System.out.print", "Scanner ", "new ArrayList", "@Override", "extends ", "implements "
    ],
    "Coding/C": [
        "#include <", "printf(", "scanf(", "malloc(", "struct ", "int main()", "free("
    ],
    "Web_Development": [
        "<!DOCTYPE html>", "document.get", "const ", "addEventListener", "href=", "class=", "style="
    ],
    "Logins_Security": [
        "password", "username", "confirm password", "otp", "sign in", "cvv", "expiry date", "login to"
    ],
    "College/KPRIET": [
        "kpriet", "internal test", "semester", "student id", "assignment", "course code", "marks"
    ]
}
DATETIME_FORMAT = "%Y-%m-%d-%H-%M-%S"