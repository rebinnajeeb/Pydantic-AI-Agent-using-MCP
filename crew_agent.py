from crewai import Agent, Task, Crew
from crewai.mcp import MCPServerStdio
from dotenv import load_dotenv

load_dotenv()

# connect to your weather MCP server
server = MCPServerStdio(
    command=r"C:\path\to\venv\Scripts\python.exe",
    args=[r"C:\path\to\weather.py"]
)

# create agent
agent = Agent(
    role="Weather Assistant",
    goal="Help users with weather and general questions",
    backstory="You are a helpful assistant. Use weather tool when needed.",
    mcps=[server]
)

print("🤖 Chat with me! (type 'quit' to exit)")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "quit":
        break

    # task is now dynamic — whatever user types!
    task = Task(
        description=user_input,        # ← user question goes here
        expected_output="A helpful answer",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task]
    )

    result = crew.kickoff()
    print(f"Bot: {result}")
