# AI Agent Chatbot Project
## Overview
AI Agent Chatbot is a FastAPI-based project that combines LangGraph with LangChain and Streamlit to build an interactive AI chatbot. This project allows users to specify their desired AI model and interact with the chatbot through a user-friendly interface. It leverages external tools like **TavilySearchResults** for search functionality and integrates multiple large language models like `"llama3-70b-8192"` and `"mixtral-8x7b-32768"`.
## Features
- **FastAPI Backend**:
    - Endpoint (`/chat`) to handle AI interaction and processing.
    - Dynamic model selection.
    - Supports ReAct agents built using LangGraph.

- **Streamlit Frontend UI**:
    - Simple and intuitive interface to communicate with the LangGraph agent.
    - Input fields for system prompt, model selection, and user messages.
    - View AI responses in a structured format.

- **Model Support**:
    - Predefined list of models: `"llama3-70b-8192"` and `"mixtral-8x7b-32768"`.

- **Docker Support**:
    - Ready-to-deploy Docker container with FastAPI and Streamlit servers.

## Installation and Setup
### 1. Clone the Repository
``` bash
git clone <repository-url>
cd <repository-directory>
```
### 2. Environment Setup
#### Using `pip`:
1. Create a virtual environment (recommended):
``` bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
```
1. Install dependencies:
``` bash
   pip install -r requirements.txt
```
1. Set up environment variables:
Create a `.env` file with the following content (substitute placeholder values):
``` 
   GROQ_API_KEY=<your_groq_api_key>
   TAVILY_API_KEY=<your_tavily_api_key>
```
#### Using Docker (Optional):
1. Build the Docker image:
``` bash
   docker build -t langgraph-agent .
```
1. Run the container:
``` bash
   docker run -p 8000:8000 -p 8501:8501 langgraph-agent
```
## Usage
### 1. Run the Application
Start the backend and frontend locally:
``` bash
# Run FastAPI server
python app.py

# Run Streamlit UI
streamlit run ui.py --server.port 8501
```
### 2. Access the Application
Open the Streamlit UI in your browser at `http://127.0.0.1:8501`.
### 3. Interact with the LangGraph Agent
1. **Define the AI Agent**: Enter a system prompt to customize the agent's behavior.
2. **Select a Model**: Choose from predefined models (`"llama3-70b-8192"`, `"mixtral-8x7b-32768"`).
3. **Send Messages**: Enter one or more messages for interaction and submit.

### 4. View the Response
The responses from the agent are displayed in a structured format in the UI.
## File Structure
``` plaintext
.
├── app.py             # FastAPI backend for AI interaction
├── ui.py              # Streamlit frontend for user interface
├── Dockerfile         # Containerization file for both FastAPI and Streamlit
├── requirements.txt   # Dependency file for Python packages
├── .env               # Environment variable definitions
├── README.md          # Project documentation
```
## API Documentation
### Endpoint: `/chat`
- **Method**: POST
- **Description**: Handles chat interaction with the LangGraph agent.
- **Request Body**:
``` json
  {
    "system_prompt": "Agent description",
    "model_name": "llama3-70b-8192",
    "messages": ["Hello, how are you?"]
  }
```
- **Response**: JSON object containing the bot's output or error details:
``` json
  {
    "error": "Invalid model name. Please select a valid model."
  }
```
## Deployment
- **Local Machine**: Run the backend and frontend as described above.
- **Docker**: Build and run the containerized app:
``` bash
  docker build -t langgraph-agent .
  docker run -p 8000:8000 -p 8501:8501 langgraph-agent
```
- **Cloud Deployment**: Use platforms like AWS, GCP, or Azure to deploy the Docker container or host the app.

## Contributing
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

We welcome contributions to enhance functionality or fix issues.
## License
This project is licensed under the terms specified by the repository.
## Acknowledgments
- [FastAPI]()
- [Streamlit]()
- [LangGraph]()
- [LangChain]()

Feel free to adapt this README to match your project's specific needs!
