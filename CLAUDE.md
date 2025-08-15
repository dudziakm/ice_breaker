# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ice Breaker is a LangChain-based application that generates personalized conversation starters and summaries about notable personalities. It demonstrates multiple LLM integration approaches (local Ollama and OpenAI).

## Development Commands

### Environment Setup
```bash
# Install dependencies using pipenv
pipenv install

# Activate virtual environment
pipenv shell

# Run a specific implementation
python ice_breaker.py      # Ollama/Llama3 version
python ice_breaker_2.py    # OpenAI GPT-3.5 version
```

### Code Formatting
```bash
# Format code with Black
pipenv run black .
```

## Architecture & Key Components

### Core Files Structure
- **ice_breaker.py**: Main Ollama implementation using local Llama3 model. Creates LangChain pipeline with PromptTemplate → ChatOllama → StrOutputParser.
- **ice_breaker_2.py**: OpenAI variant using GPT-3.5-turbo with similar chain structure.
- **ice_breaker_1.py**: Environment testing script for verifying API key loading.

### LangChain Pattern
All implementations follow the chain pattern:
```python
chain = prompt | model | parser
```
Components are connected via pipe operators to create processing pipelines.

### Environment Configuration
The project uses `.env` file for API keys:
- `OPENAI_API_KEY`: Required for ice_breaker_2.py
- Local Ollama models don't require API keys but need Ollama running locally

### Model Integration Approaches
1. **Ollama (Local)**: Uses `ChatOllama` from `langchain-ollama` for offline LLM capabilities
2. **OpenAI (Cloud)**: Uses `ChatOpenAI` from `langchain-openai` for GPT models

When modifying LLM interactions, maintain consistency with the existing chain pattern and ensure proper environment variable handling through python-dotenv.