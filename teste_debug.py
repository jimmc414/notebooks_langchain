import sys
sys.path.append('../')

from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChain
from langchain.agents import initialize_agent, Tool
import os
import openai


llm = OpenAI( n=3, best_of=5, logprobs = 2)
result = llm.generate("Tell me a joke")
print(result.generations)