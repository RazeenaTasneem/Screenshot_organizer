# Intelligent Screenshot Organizer

Organizes screenshots into folders based on their content using **YOLO** (Object Detection) and **OCR** (Text Recognition).

## Features
- **Object Detection**: Uses YOLOv8 to analyze image content.
- **Text Recognition**: Uses Tesseract-OCR to read text from the image.
- **Auto-Categorization**: Sorts screenshots into folders like `Coding/Python`, `Coding/Java`, `Web_Development`, etc.

## Setup

1.  **Install Tesseract-OCR**:
    - Download and install from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
    - Ensure the path in `config.py` matches your installation:
      ```python
      TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
      ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the organizer:
    ```bash
    python main.py
    ```
    *Note: On the first run, it will automatically download the YOLOv8 model (~6MB).*

2.  Take a screenshot. It will be automatically moved from your Screenshots folder to the `Organised` folder.

## Troubleshooting
- **YOLO Error**: Ensure `ultralytics` is installed.
- **OCR Error**: Ensure Tesseract is installed and the path in `config.py` is correct.