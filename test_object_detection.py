import unittest
from unittest.mock import patch, MagicMock
import processor
import config

class TestObjectDetection(unittest.TestCase):
    @patch('processor.detect_objects')
    @patch('processor.pytesseract.image_to_string')
    @patch('processor.Image.open')
    def test_vehicle_detection(self, mock_image_open, mock_ocr, mock_detect):
        # Setup mocks
        mock_detect.return_value = ['car']
        mock_ocr.return_value = "some random text"
        
        # Run function
        category = processor.get_category("dummy_path.jpg")
        
        # Verify
        self.assertEqual(category, "Objects/Vehicles", "Should be categorized as Objects/Vehicles based on 'car' detection")
        print(f"Test 1 Passed: Detected 'car' -> Category '{category}'")

    @patch('processor.detect_objects')
    @patch('processor.pytesseract.image_to_string')
    @patch('processor.Image.open')
    def test_fallback_to_ocr(self, mock_image_open, mock_ocr, mock_detect):
        # Setup mocks: No relevant object detected
        mock_detect.return_value = ['person'] # person is in config now
        
        # Run function
        category = processor.get_category("dummy_path.jpg")
        
        # Verify
        self.assertEqual(category, "Objects/People", "Should be categorized as Objects/People based on 'person' detection")
        print(f"Test 2 Passed: Detected 'person' -> Category '{category}'")

    @patch('processor.detect_objects')
    @patch('processor.pytesseract.image_to_string')
    @patch('processor.Image.open')
    def test_no_object_match(self, mock_image_open, mock_ocr, mock_detect):
        # Setup mocks: Object not in config
        mock_detect.return_value = ['unknown_object'] 
        mock_ocr.return_value = "def my_function():"
        
        # Run function
        category = processor.get_category("dummy_path.jpg")
        
        # Verify
        self.assertEqual(category, "Coding/Python", "Should fall back to OCR and detect Python code")
        print(f"Test 3 Passed: No object match -> Fallback to OCR -> Category '{category}'")

if __name__ == '__main__':
    unittest.main()
