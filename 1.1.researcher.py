from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()
agent = Agent(
   model=OpenAIChat(id="gpt-4o-mini"),
  tools=[TavilyTools()],
)

agent.print_response("Quem é o presidente do Brasil?")