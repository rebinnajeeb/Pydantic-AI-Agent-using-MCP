import asyncio
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

load_dotenv()

server = MCPServerStdio(
    command=r"C:\Users\2403682\OneDrive - Cognizant\Desktop\MCP\mcp_server\venv\Scripts\python.exe",
    args=[
        r"C:\Users\2403682\OneDrive - Cognizant\Desktop\MCP\mcp_server\weather.py"
    ],
)

agent = Agent(
    model="groq:llama-3.3-70b-versatile",
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
