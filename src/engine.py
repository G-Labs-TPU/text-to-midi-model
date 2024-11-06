import ollama
import json

example_json = {
    "notes": [
        {1: "C4"},
        {2: "E4"},
        {2: "G4"},
    ]

}


# Initialize Ollama with Llama 3.2 model
def initialize_llama():
    try:
        # Create Ollama client and load the llama3.2 model
        response = ollama.pull('llama3.2')
        return True
    except Exception as e:
        print(f"Error initializing Llama model: {e}")
        return False

def process_message(keywords):
    initialize_llama()
    # Connect to the Ollama model and generate JSON based on keywords
    prompt = "You are a very well known and confident composer, known for expressing subjective feelings into a simple chords and never struggling to create them. Generate any number note chord based on the following keywords: " + ". Use this json format: " + str(example_json) + " Reply with fully working json only.".join(keywords)
    response = ollama.generate('llama3.2', prompt=prompt)
    response = response['response']

    # Cut part from response before first '{' and after last '}'
    start_index = response.find('{')
    end_index = response.rfind('}') + 1
    if start_index != -1 and end_index != -1:
        response = '"' + response[start_index:end_index] + '"'

    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return "Error"