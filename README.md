# Study Buddy App

A local study companion that demonstrates the effectiveness of different prompting techniques using Ollama, Flask, and React.

## Project Overview

This application was built to explore and compare the practical effects of three fundamental prompting techniques in AI interactions:

- **One-Shot Prompting**: Single example-based learning
- **Few-Shot Prompting**: Multiple example-based learning  
- **Chain of Thought**: Step-by-step reasoning approach

## Features

- Local AI integration using Ollama
- Interactive React frontend
- Flask backend API
- Three distinct prompting techniques to choose from
- Real-time comparison of prompting effectiveness
- Local processing (no external API calls required)

## Tech Stack

- **Frontend**: React
- **Backend**: Flask (Python)
- **AI Engine**: Ollama
- **Architecture**: Client-Server with REST API

## Prerequisites

Before running this application, make sure you have:

- Python 3.8+
- Node.js 16+
- Ollama installed and running locally
- A compatible language model downloaded in Ollama (e.g., llama2, mistral)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/aarshitaacharya/study-buddy-prompt-engg.git
cd study-buddy-prompt-engg
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

### 4. Ollama Setup
```bash
# Install and start Ollama (if not already done)
# Download a model (example with llama2)
ollama pull llama2

# Verify Ollama is running
ollama list
```

## Running the Application

### Start the Backend (Flask)
```bash
cd backend
python app.py
```
The Flask server will start on `http://localhost:5050`

### Start the Frontend (React)
```bash
cd frontend
npm start
```
The React app will start on `http://localhost:3000`

## How to Use

1. **Select a Prompting Technique**: Choose between One-Shot, Few-Shot, or Chain of Thought
2. **Enter Your Question**: Type in any study-related question or topic
3. **Compare Results**: Try the same question with different techniques to see how responses vary
4. **Analyze Effectiveness**: Observe how each technique affects the AI's reasoning and response quality

## Prompting Techniques Explained

### One-Shot Prompting
Provides the AI with a single example to understand the desired response format and style.

### Few-Shot Prompting  
Uses multiple examples to give the AI a better understanding of the expected output pattern.

### Chain of Thought
Encourages the AI to break down complex problems into step-by-step reasoning processes.

## Project Structure

```
study-buddy-app/
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── ...
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json       # Node.js dependencies
│   └── ...
└── README.md
```

## Configuration

### Backend Configuration
- Modify `app.py` to change Ollama connection settings
- Update model selection in the backend code
- Adjust API endpoints as needed

### Frontend Configuration
- Update API endpoint URLs in React components
- Customize UI components and styling
- Modify prompting technique implementations

## Results & Observations

This project demonstrates:
- How different prompting techniques affect AI response quality
- The trade-offs between response speed and thoroughness
- Practical applications of prompt engineering concepts
- Local AI deployment benefits and limitations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- [Ollama](https://ollama.ai/) for providing local AI model hosting
