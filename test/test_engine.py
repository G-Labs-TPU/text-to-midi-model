import unittest
from src.engine import process_message

class TestEngine(unittest.TestCase):
    def test_process_message(self):
        keywords = ["happy", "melody"]
        json_data = process_message(keywords)
        
        # Check if the response is in JSON format
        self.assertIsInstance(json_data, dict)
        
        # Check if 'notes' key is present in JSON data
        self.assertIn("notes", json_data)
        
        # Check if 'notes' contains expected structure
        for note in json_data["notes"]:
            self.assertIn("note", note)
            self.assertIn("duration", note)
            self.assertIn("velocity", note)

if __name__ == '__main__':
    unittest.main()
