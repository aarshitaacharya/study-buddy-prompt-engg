from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

@app.route('/api/chat', methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'error': 'No message provided'})
        
        prompt = f"""You are a helpful study buddy. Help the student learn about: {user_message}

        Please provide a clear, short, educational explanation that is:
        - Easy to understand
        - Accurate and informative
        - Encouraging and supportive

        Topic: {user_message}"""

        ollama_payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=ollama_payload)
        if response.status_code == 200:
            ollama_response = response.json()
            ai_message = ollama_response.get('response', 'Sorry, I got an empty response')

            return jsonify({
                'response': ai_message,
                "status": 'success'
            })
        
        else:
            return jsonify({
                'error': f"Ollama returned a status code: {response.status_code}",
                "status": "error"
            }), 500
        
    except requests.exceptions.ConnectionError:
        return jsonify({
            'error': 'Could not connect to Ollama',
            'status': 'error'
        }), 500
    
    except Exception as e:
        return jsonify({
            'error': f"An error occurred: {str(e)}",
            "status": "error"
        }), 500
    

@app.route('/health', methods=["GET"])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Study Buddy backend is running'
    })

if __name__ == '__main__':
    print("Starting backend, check ollama running: ollama serve")
    print(f"Using backend: {MODEL_NAME}")
    app.run(debug=True, port=5050)
        

        