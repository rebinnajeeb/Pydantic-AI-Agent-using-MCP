"""
Pydantic AI agent connected to the weather MCP server.
Uses Claude Haiku to process natural language queries
and calls the get_weather MCP tool to fetch real weather data.
"""
import asyncio
from pathlib import Path
from dotenv import dotenv_values
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset, StdioTransport
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

_env = dotenv_values(Path(__file__).parent / ".env")
_api_key = _env.get("ANTHROPIC_API_KEY")

server = MCPToolset(
    StdioTransport(
        command=r"C:\Users\2403682\OneDrive - Cognizant\Desktop\MCP\mcp_server\venv\Scripts\python.exe",
        args=[
            r"C:\Users\2403682\OneDrive - Cognizant\Desktop\MCP\mcp_server\weather.py"
        ],
    ),
    init_timeout=30.0,
)

model = AnthropicModel(
    "claude-haiku-4-5-20251001",
    provider=AnthropicProvider(api_key=_api_key),
)

agent = Agent(
    model=model,
    toolsets=[server],
)

async def main():
    async with agent:
        result = await agent.run("What is the current weather in Chennai?")
        print("\n=== Agent Response ===")
        print(result.output)
        print("======================\n")

if __name__ == "__main__":
    asyncio.run(main())
