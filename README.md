# Pydantic AI Weather Agent Using MCP

A conversational AI agent built with Pydantic AI that connects to a local weather MCP server. It uses Groq's Llama 3.3 70B model to understand natural language weather queries and fetches real weather data via the `get_weather` MCP tool.

## Prerequisites

- Python 3.10+
- Existing weather MCP server at `C:\Users\2403682\OneDrive - Cognizant\Desktop\MCP\mcp_server\weather.py`
- A Groq API key (get one at https://console.groq.com)

## Setup

1. Clone or copy this project folder
2. Create and activate the virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your key:
   ```
   GROQ_API_KEY=your_actual_key_here
   ```

## How to Run

```
venv\Scripts\python.exe pydantic_agent.py
```

## Modify the Query

Edit the `agent.run(...)` line in `pydantic_agent.py`:
```python
result = await agent.run("What is the weather in Mumbai?")
```

## Extend the Agent

- **Add more tools**: Connect additional MCP servers by adding more `MCPServerStdio` instances to `toolsets=[...]`
- **Change the model**: Replace `"groq:llama-3.3-70b-versatile"` with any supported model string
- **Make it interactive**: Wrap `agent.run(...)` in a `while True` loop with `input()` to chat continuously
