import unittest
from unittest.mock import patch, AsyncMock
from src.client import client
from src.engine import process_message
from src.parser import json_to_midi

class TestClient(unittest.IsolatedAsyncioTestCase):
    @patch('src.client.process_message')
    @patch('src.client.json_to_midi')
    async def test_on_message(self, mock_json_to_midi, mock_process_message):
        # Setup mocks
        mock_process_message.return_value = {
            "notes": [
                {"note": 60, "duration": 500, "velocity": 64}
            ]
        }
        mock_json_to_midi.return_value = 'mock_output.mid'
        
        # Mock a message object
        message = AsyncMock()
        message.content = "generate melody"
        message.author = AsyncMock()
        message.author.bot = False  # Simulate a non-bot user message
        message.channel.send = AsyncMock()  # Mock the send method
        
        # Call the on_message event handler
        with patch.object(client, 'on_message', client.on_message):
            await client.on_message(message)
        
        # Assertions
        mock_process_message.assert_called_once_with(["generate", "melody"])
        mock_json_to_midi.assert_called_once_with(mock_process_message.return_value)
        message.channel.send.assert_called_once()

if __name__ == '__main__':
    unittest.main()
