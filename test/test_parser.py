import unittest
import os
from src.parser import json_to_midi

class TestParser(unittest.TestCase):
    def test_json_to_midi(self):
        json_data = {
            "notes": [
                {"note": 60, "duration": 500, "velocity": 64},
                {"note": 62, "duration": 500, "velocity": 64},
            ]
        }
        
        midi_file_path = json_to_midi(json_data)
        
        # Check if MIDI file was created
        self.assertTrue(os.path.exists(midi_file_path))
        
        # Clean up the generated MIDI file
        os.remove(midi_file_path)

if __name__ == '__main__':
    unittest.main()
