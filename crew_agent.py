from crewai import Agent, Task, Crew
from crewai.mcp import MCPServerStdio
from dotenv import load_dotenv

load_dotenv()

# connect to your weather MCP server
server = MCPServerStdio(
    command=r"C:\path\to\venv\Scripts\python.exe",
    args=[r"C:\path\to\weather.py"]
)

# create agent WITH mcp server
agent = Agent(
    role="Weather Assistant",
    goal="Help users with weather information",
    backstory="You are a helpful assistant who knows about weather.",
    mcps=[server]          # ← give MCP server here (not toolsets!)
)

# create task
task = Task(
    description="What is the current weather in Chennai?",
    expected_output="Weather details for Chennai",
    agent=agent
)

# create crew and run
crew = Crew(
    agents=[agent],
    tasks=[task]
)

result = crew.kickoff()
print(result)
