# genai_translate_agent
Agent to detect language of any given input text using the `langdetect` library to provide input for LLM to translate

## 🚀 Features

- Detects the language of a given input string.
- Returns ISO 639-1 language codes (e.g., `en`, `fr`, `ar`).
- Can be used in a multi-step language translation pipeline.

Install Steps:

#1 Register Agent
.\genai.exe register_agent --name detect_language --description "This agent detects language"

#2 Create Virtual ENV
uv venv
uv sync

#3 Install Dependencies
pip install langdetect

#4 (Optional) test the module
.\.venv\Scripts\python.exe -c "from langdetect import detect; print(detect('bonjour tout le monde'))"
Expected Output: fr

#5 Run Agents (AgentOS)
.\genai.exe run_agents
