<div align="center">
  <img src="https://img.icons8.com/color/96/000000/automation.png" alt="Automation Icon" width="80" height="80"/>
  <h1>📸 Intelligent Screenshot Organizer</h1>
  <p>
    <b>The smartest way to keep your screenshots flawlessly organized.</b><br>
    <i>Powered by YOLOv8 and Tesseract-OCR.</i>
  </p>

  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org)
  [![YOLOv8](https://img.shields.io/badge/YOLO-v8-yellow.svg?logo=ultralytics&logoColor=black)](https://github.com/ultralytics/ultralytics)
  [![Tesseract](https://img.shields.io/badge/OCR-Tesseract-lightgray.svg)](https://github.com/tesseract-ocr/tesseract)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
</div>

<hr/>

## 📖 Overview

Are you tired of cluttered screenshot folders? The **Intelligent Screenshot Organizer** sits silently in the background, waits for you to take a screenshot, and then leverages cutting-edge AI and computer vision to understand the content. 

Whether it's a code snippet, a login page, or a picture of a car, the app intelligently categorizes it, suggests a precise file name, and seamlessly moves it to the appropriate folder—putting YOU in control with a beautiful, native-looking confirmation popup.

---

## ✨ Core Features

*   **🧠 Object Detection (YOLOv8)**: Instantly detects objects in your screenshots (people, vehicles, laptops, etc.) and routes them to precise category folders like `Objects/Vehicles`.
*   **📝 Text Recognition (OCR)**: Integrates `Tesseract-OCR` to read text embedded within your images. Perfect for sorting code snippets (e.g., `Coding/Python`) or sensitive documents.
*   **🤖 Smart Naming**: Uses OCR context to generate concise, human-readable file names automatically. Say goodbye to `Screenshot 2023-10-15 142345.png`!
*   **🎨 Native-Style Interactive UI**: Features a sleek, dark-themed Tkinter popup that mimics Windows 10/11 system notifications. Review the AI's suggestions and tweak them before saving.
*   **⚡ Real-Time Monitoring**: Utilizes `watchdog` to monitor your directory continuously with minimal system footprint.

---

## 🚀 Getting Started

Follow these steps to set up your intelligent workflow.

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

### 2. Install Tesseract-OCR
Tesseract is required for extracting text from images.
*   **Download**: [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
*   **Configure**: Note the installation path (usually `C:\Program Files\Tesseract-OCR\tesseract.exe`) and update the `TESSERACT_PATH` variable inside `config.py`.

### 3. Install Dependencies
Clone the repository (or navigate to the folder) and install the required Python packages:
```bash
pip install -r requirements.txt
```
> *This installs `ultralytics`, `pytesseract`, `watchdog`, `Pillow`, and `opencv-python`.*

---

## ⚙️ Configuration & Customization

The heart of the application is the `config.py` file. Open it to tailor the tool to your exact needs:

```python
# 📂 Set your source and destination paths
SOURCE_DIR = r"C:\Users\YourName\Pictures\Screenshots"
TARGET_DIR = r"C:\Users\YourName\Pictures\Screenshots\Organised"

# 🔑 Set your API keys and executable paths
TESSERACT_PATH = r"C:\path\to\tesseract.exe"
```

You can also customize the **keyword mappings** (for OCR categorization) and **object associations** (for YOLO categorization) directly within the configuration file to suit your specific workflow.

---

## 🏃‍♂️ Usage

1.  **Start the Engine**: Run the main application in the background.
    ```bash
    python main.py
    ```
    *(Note: On the very first run, a lightweight YOLOv8 model (~6MB) will be downloaded automatically.)*

2.  **Take a Screenshot**: Use your preferred method (`Win + PrintScreen`, Snipping Tool, etc.).

3.  **Confirm & Save**: A beautiful popup will slide in at the bottom right of your screen. 
    *   Review the AI-generated Title and Category.
    *   Hit **Enter** (or click Save) to apply.
    *   Hit **Escape** (or click Cancel) to discard the screenshot.

---

## 🛠️ Troubleshooting

| Issue | Potential Fix |
| :--- | :--- |
| **No text extracted / OCR fails** | Verify that `TESSERACT_PATH` in `config.py` points to the actual `tesseract.exe` file. |
| **Missing ultralytics error** | Ensure you ran `pip install -r requirements.txt`. |
| **Popup does not appear** | Ensure your Python environment supports Tkinter GUI rendering. |

---

<div align="center">
  <i>Built to save you clicks, organized by AI.</i>
</div>