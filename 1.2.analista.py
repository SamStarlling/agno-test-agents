from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
# from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.agent import Agent
from agno.db.sqlite import SqliteDb

load_dotenv()

# Setup the SQLite database
db = SqliteDb(db_file="tmp/data.db")

# Setup a basic agent with the SQLite database
agent = Agent(db=db)

agent = Agent(
  model=OpenAIChat(id="gpt-4.1-mini"),
  tools=[YFinanceTools()],
  instructions="Use tabelas para mostrar a informação final. Não inclkua códigos ou explicações, apenas a resposta em tabelas.",
  db=db,
  add_history_to_context=True,
  num_history_runs=3
)

agent.print_response("Qual a cotação atual da petrobras?", session_id="petrobras_session", user_id="analista_petrobras")
agent.print_response("Qual a cotação atual da vale?", session_id="vale_session", user_id="analista_petrobras")
agent.print_response("Que empresas consultamos as cotações?", session_id="petrobras_session", user_id="analista_empresas")