from agno.models.groq import Groq
from agno.models.message import Message
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.tavily import TavilyTools

load_dotenv()
print('dotenv loaded')
print('Groq class:', Groq)
print('Message class:', Message)
m = Groq(id='llama-3.3-70b-versatile')
print('Groq instance created:', type(m))
