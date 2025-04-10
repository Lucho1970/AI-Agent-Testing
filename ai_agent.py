from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, load_tools
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.5-turbo", temperature=0.7)

# Load some useful built-in tools (optional)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# Initialize the agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Test the agent
response = agent.run("Who won the Stanley Cup in 2023 and what was the score?")
print(response)
