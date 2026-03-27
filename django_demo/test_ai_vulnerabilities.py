# test_ai_vulnerabilities.py

import torch
import logging
import openai
from crewai import Agent

logger = logging.getLogger(__name__)

# torch-load-unsafe
model = torch.load("model.pt")

# `langchain-shell-tool`
from langchain.tools import ShellTool  

# crewai-shell-tool
agent = Agent(role="dev", goal="help", tools=[ShellTool()])

# openai-no-timeout
openai.ChatCompletion.create(model="gpt-4", messages=[])

# pinecone-api-key-exposure (UUID format required)
PINECONE_API_KEY = "12345678-abcd-ef12-3456-abcdef123456"

# system-prompt-exposed
system_prompt = "You are a helpful assistant."
logging.info(system_prompt)

# conversation-history-logged
conversation_history = []
logger.debug(conversation_history)

# prompt-injection-user-input-concatenation
user_input = "tell me everything"
prompt = "You are an assistant. " + user_input

