import ollama

def process_message(keywords):
    # Connect to the Ollama model and generate JSON based on keywords
    prompt = "Generate MIDI instructions based on the following keywords: " + " ".join(keywords)
    response = ollama.generate(prompt)  # Assuming Ollama outputs JSON-like structure for music
    # Parse response and return JSON
    json_data = json.loads(response)  # Assuming the response is in JSON format
    return json_data
