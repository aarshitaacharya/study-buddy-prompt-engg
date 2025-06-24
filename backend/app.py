from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Ollama configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def clean_markdown_text(text):
    """Clean markdown formatting from text"""
    # Remove bold formatting (*text* or **text**)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    
    # Remove italic formatting (_text_)
    text = re.sub(r'_(.*?)_', r'\1', text)
    
    # Remove code formatting (`code`)
    text = re.sub(r'`(.*?)`', r'\1', text)
    
    # Remove headers (## Header)
    text = re.sub(r'^#{1,6}\s*', '', text, flags=re.MULTILINE)
    
    # Clean up multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()



def create_prompt(message, technique='zero-shot'):
    """Create prompts based on different techniques"""
    
    if technique == 'zero-shot':
        return f"""You are a helpful study buddy. Help the student learn about: {message}

            Please provide a clear, educational explanation that is:
            - Easy to understand
            - Accurate and informative
            - Encouraging and supportive

            Topic: {message}"""
    
    elif technique == 'few-shot':
        return f"""You are a helpful study buddy. Here are examples of how I help students:

            Example 1:
            Student: "Explain gravity"
            Study Buddy: "Gravity is the force that attracts objects toward each other. Think of it like an invisible rope pulling things together. On Earth, gravity pulls everything toward the center, which is why things fall down instead of floating away. The more massive an object is, the stronger its gravitational pull. That's why the Moon orbits Earth, and Earth orbits the Sun!"

            Example 2:
            Student: "What is photosynthesis?"
            Study Buddy: "Photosynthesis is how plants make their own food using sunlight! Here's the simple version: Plants take in carbon dioxide from the air and water from their roots, then use sunlight as energy to combine them into sugar (glucose) and oxygen. The equation is: 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂. Think of plants as little solar-powered food factories!"

            Now help this student:
            Student: "{message}"
            Study Buddy:"""
    
    elif technique == 'chain-of-thought':
        return f"""You are a helpful study buddy. When explaining complex topics, break them down step-by-step with clear reasoning.

            For the topic "{message}", please:
            1. First, identify the key components or concepts involved
            2. Explain each component step by step
            3. Show how they connect or work together
            4. Provide a clear conclusion or summary
            5. Use phrases like "Let's think through this step by step" and "Here's why this happens"

            Topic to explain: {message}"""
    
    else:
        return f"Help the student learn about: {message}"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Get the message and technique from the frontend
        data = request.get_json()
        user_message = data.get('message', '')
        technique = data.get('technique', 'zero-shot')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Create prompt based on selected technique
        prompt = create_prompt(user_message, technique)

        # Call Ollama
        ollama_payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(OLLAMA_URL, json=ollama_payload)
        
        if response.status_code == 200:
            ollama_response = response.json()
            ai_message = ollama_response.get('response', 'Sorry, I got an empty response.')
            
            return jsonify({
                'response': ai_message,
                'technique_used': technique,
                'status': 'success'
            })
        else:
            return jsonify({
                'error': f'Ollama returned status code: {response.status_code}',
                'status': 'error'
            }), 500
            
    except requests.exceptions.ConnectionError:
        return jsonify({
            'error': 'Could not connect to Ollama. Make sure Ollama is running.',
            'status': 'error'
        }), 500
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Study Buddy backend is running'
    })

if __name__ == '__main__':
    print("Starting Study Buddy backend...")
    print("Make sure Ollama is running: ollama serve")
    print(f"Using model: {MODEL_NAME}")
    app.run(debug=True, port=5050)