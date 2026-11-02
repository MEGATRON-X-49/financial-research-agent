# Financial Research Agent

An AI-powered financial research assistant built using Python, Agno, Ollama and Next.js. The agent uses a locally hosted LLM and financial data tools to answer stock market and financial research queries.

## Features

- Interactive conversational interface.
- Local LLM inference using Ollama and Llama 3.2.
- Financial data retrieval using Yahoo Finance.
- Stock price lookup and historical market data.
- Company fundamentals and financial analysis.
- AI-powered explanations of financial concepts.
- Agent backend powered by Agno AgentOS.
- No paid LLM API required.

## Architecture

```text
             User
              |
              v
       Next.js Agent UI
        localhost:3000
              |
              v
       Agno AgentOS
        localhost:7777
              |
              v
       Financial Agent
              |
        +-----+------+
        |            |
        v            v
      Ollama      Yahoo Finance
        |            |
        v            v
    Llama 3.2     Market Data
        |
        v
   AI-generated response
```

##  Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Backend development |
| Agno | AI agent framework |
| Ollama | Local LLM runtime |
| Llama 3.2 3B | Language model |
| FastAPI | Backend API |
| Next.js | Frontend |
| Yahoo Finance | Financial data |
| yfinance | Financial data integration |

##  Prerequisites

- Python 3.12
- Node.js and npm
- Ollama
- Git

##  Installation and Setup

### 1. Clone the repository

```bash
git clone git clone https://github.com/MEGATRON-X-49/financial-research-agent.git
cd financial-research-agent
```

### 2. Set up Python environment

```bash
python -m venv venv
```

Activate on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start Ollama

Make sure Ollama is installed and running.

```bash
ollama run llama3.2:3b
```

### 4. Start AgentOS backend

```bash
python -m uvicorn agent_os:app --reload --port 7777
```

Backend API documentation:

http://localhost:7777/docs

### 5. Start frontend

Open another terminal:

```bash
cd agent-ui
npm install
npm run dev
```

Open the application:

http://localhost:3000

##  Example Queries

- What is the current stock price of Tesla?
- Compare NVIDIA and AMD.
- Analyse Reliance Industries.
- Explain important financial ratios.
- Retrieve historical stock market information.

## Privacy and Cost

The language model runs locally through Ollama. No paid OpenAI or Gemini API is required for inference.
Financial market information is retrieved through Yahoo Finance. Data availability and delays depend on the source.

##  Project Objective

To understand and implement practical agentic AI concepts, including LLM integration, tool calling, external data retrieval, backend APIs and conversational interfaces.

##  Author

Kamal Mudiraj

