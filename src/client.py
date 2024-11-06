import discord
import json
from engine import process_message  # Assuming the Engine component is in engine.py
from parser import json_to_midi     # Assuming the Parser component is in parser.py

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Avoid responding to bot's own messages
    if message.author == client.user:
        return

    # Process the message and generate a JSON response from the engine
    keywords = message.content.split()  # Extract keywords from the message
    json_data = process_message(keywords)  # Get JSON data from the Engine

    # Convert JSON to MIDI file
    midi_file_path = json_to_midi(json_data)

    # Send MIDI file as a response
    await message.channel.send(file=discord.File(midi_file_path))

client.run(TOKEN)
