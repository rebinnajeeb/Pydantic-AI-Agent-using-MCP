from crewai import Agent, Task, Crew, LLM
from crewai.mcp import MCPServerStdio
from dotenv import load_dotenv

load_dotenv()

# define the LLM
llm = LLM(
    model="groq/llama-3.3-70b-versatile",  # ← groq model
    api_key="your_groq_api_key_here"        # ← or put in .env
)

# connect to your weather MCP server
server = MCPServerStdio(
    command=r"C:\path\to\venv\Scripts\python.exe",
    args=[r"C:\path\to\weather.py"]
)

# create agent WITH llm
agent = Agent(
    role="Weather Assistant",
    goal="Help users with weather and general questions",
    backstory="You are a helpful assistant. Use weather tool when needed.",
    mcps=[server],
    llm=llm             # ← give LLM here
)

print("🤖 Chat with me! (type 'quit' to exit)")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "quit":
        break

    task = Task(
        description=user_input,
        expected_output="A helpful answer",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task]
    )

    result = crew.kickoff()
    print(f"Bot: {result}")
