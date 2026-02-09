try:
    import watchdog
    import pytesseract
    import PIL
    print("All packages imported successfully.")
except ImportError as e:
    print(f"Import failed: {e}")
