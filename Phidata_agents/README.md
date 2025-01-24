# Project: Custom AI Agent Framework
This project revolves around creating and utilizing AI-powered agents integrated with various tools to perform specialized tasks, such as managing financial data, extracting information from the web, and combining multiple agents into teams to achieve more sophisticated workflows.
## Overview
This repository includes multiple Python scripts that demonstrate how to create, configure, and operate AI agents using the `phi` framework. Each script defines distinct agents or agent teams and provides examples of functionality such as retrieving stock data, summarizing company fundamentals, performing web searches, and more.
Key features include:
- **Custom AI agents** with configurable models and tools.
- **Team-based architecture** to combine agents for collaborative tasks.
- Integration with **tools like DuckDuckGo and YFinance** for web search and stock analysis.
- Persistent **storage for agent interactions** using SQLite.

### File Structure
1. **`agent_teams.py` **
    - Defines individual agents (`web_agent`, `finance_agent`) and a combined `agent_team`.
    - Agents use the `Groq` model with tools like DuckDuckGo and YFinance.
    - Demonstrates collaborative tasks by summarizing and comparing stock data for companies like Tesla (TSLA) and Nvidia (NVDA).

2. **`playground.py` **
    - Sets up a web-based playground using the `Playground` class, allowing interactions with the AI agents in a UI.
    - Defines agents for finance and web search tasks, uses the `OpenAIChat` model (`gpt-4o`), and enables persistent storage through SQLite.
    - Runs a development server to interact with the agents in real-time.

3. **`simple_groq_agent.py` **
    - A minimal script showcasing how to create and use a single agent with the `Groq` model.
    - Uses a simplified interaction that answers general AI-related queries.

4. **`finance_agent.py` **
    - Focuses on a dedicated finance agent utilizing the `OpenAIChat` model and YFinance tools.
    - Demonstrates financial data analysis with improved formatting (e.g., tables) and debugging capabilities.

## Getting Started
### Prerequisites
To run this project, ensure you have the following installed:
1. **Python 3.8 or later**
2. **Dependencies** (listed in `requirements.txt`):
    - `phi` (Core framework for agent management)
    - `dot-env` (For environment variable management)
    - Database packages for SQLite (if using storage)

3. **Other tools**:
    - A web browser for interacting with the Playground UI.

### Installation Steps
1. Clone the repository:
``` bash
   git clone <repository-url>
   cd <repository-directory>
```
1. Create a virtual environment:
``` bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate       # Windows
```
1. Install dependencies:
``` bash
   pip install -r requirements.txt
```
1. Set up environment variables:
    - Create a `.env` file in the root directory with relevant keys for the tools (e.g., `DuckDuckGo` or `YFinance`).

## Usage
### Running Agents
You can run individual files based on your use case. Here's a brief guide:
1. **Agent Teams (`agent_teams.py`)**:
``` bash
   python agent_teams.py
```
This script launches agent interactions focusing on web searches and financial data comparison. The results are displayed in the console with helpful tables and source references.
1. **Playground Application (`playground.py`)**:
``` bash
   python playground.py
```
Launches a web-based playground where you can interact with agents dynamically.
1. **Simple Agent (`simple_groq_agent.py`)**:
``` bash
   python simple_groq_agent.py
```
This script is perfect for a quick demonstration of an AI-agents answering simple queries.
1. **Finance Agent (`finance_agent.py`)**:
``` bash
   python finance_agent.py
```
Provides a dedicated agent for financial data analysis. It retrieves stock prices, analysts' recommendations, and company fundamentals, presenting them in a tabular format.
## Key Components
### 1. **Agents**
- **Web Agent**: Enables web searches and fetches summarized responses using tools like DuckDuckGo.
- **Finance Agent**: Provides finance-focused data, such as stock prices, fundamentals, recommendations, etc.
- **Agent Team**: Combines agents for collaborative or complementary tasks.

### 2. **Models**
- **Groq (`llama-3.3-70b-versatile`)**: Used in individual scripts for general-purpose AI tasks.
- **OpenAIChat (`gpt-4o`)**: Provides conversational capabilities and powers agents in the Playground.

### 3. **Tools**
- **DuckDuckGo**: Fetches search results and website summaries.
- **YFinance**: Handles financial data, such as stock prices, recommendations, and company information.

## Customization
- **Adding a new tool**: Tools can be added to an agent by initializing instances of tools compatible with the `phi` framework and appending them to the `tools` list.
- **Changing Models**: Replace `Groq` or `OpenAIChat` with the desired model in scripts to adapt agents to your specific needs.
- **Enable/Disable Features**: Modify agent parameters like `show_tool_calls`, `markdown`, or `debug_mode` to customize behavior.

## Future Improvements
1. **Additional Tools**:
    - Explore integrating more tools for AI agents, such as natural language processing, sentiment analysis, or web scraping libraries.

2. **Enhanced UI**:
    - Improve the Playground interface with more interaction options and analytics.

3. **API Access**:
    - Provide APIs to interact with agents programmatically.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.
## Acknowledgments
- Thanks to the `phi` framework for simplifying agent development.
- Special thanks to contributors and tool creators like `YFinance` and `DuckDuckGo`.
