from agno.agent import Agent
from agno.tools.tavily import TavilyTools
# from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

def celsius_to_fh(temp_em_celsius: float) -> float:
  """
  Converte temperatura de Celsius para Fahrenheit.

  Args:
    temp_em_celsius (float): Temperatura em graus Celsius.

  Returns:
    float: Temperatura convertida em graus Fahrenheit.
  """
  return (temp_em_celsius * 9/5) + 32

agent = Agent(
  model=OpenAIChat(id="gpt-4.1-mini"),
  tools=[TavilyTools(), celsius_to_fh,],
  debug_mode=True,
)

agent.print_response("Use a ferramenta para pesquisar a temperatura de hoje no Rio de Janeiro em Fahrenheit.")