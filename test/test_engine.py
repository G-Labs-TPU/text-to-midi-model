import unittest
from src.engine import process_message

def test_process_message(self):
    keywords = ["happy", "melody"]
    json_data = process_message(keywords)
    
    print("Chord received:",json_data)

    # Check if the response is in JSON format
    self.assertIsInstance(json_data, dict)
    
    # # Check if 'notes' key is present in JSON data
    # self.assertIn("notes", json_data)
    
    # # Check if 'notes' contains expected structure
    # for note in json_data["notes"]:
    #     self.assertIn("note", note)


class TestEngine(unittest.TestCase):
    def test_process_message(self):
        keywords = ["happy", "melody"]
        test_process_message(keywords)

    def test_process_message_sad(self):
        keywords = ["sad", "gloomy"]
        test_process_message(keywords)
       
    def test_process_message_energic(self):
        keywords = ["epic", "superior"]
        test_process_message(keywords)
        
    def test_process_message_lil_baby(self):
        keywords = ["4pf", "nardo wick"]
        test_process_message(keywords)
        
if __name__ == '__main__':
    unittest.main()
