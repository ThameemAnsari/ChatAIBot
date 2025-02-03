from pydantic_ai import Agent
from openai import AsyncAzureOpenAI
from pydantic_ai.models.openai import OpenAIModel
import os
from dotenv import load_dotenv
from colorama import Fore
import openai
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI

load_dotenv()

# client = AsyncAzureOpenAI(
#     azure_endpoint=os.getenv('AZURE_OPENAI_EMBEDDINGS_ENDPOINT'),
#     api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
#     api_key=os.getenv('AZURE_OPENAI_API_KEY'),
# )

# # Create the Model
# model = OpenAIModel('gpt-4o-mini', openai_client=client)

# # Create the Agent
# agent = Agent(model=model)

# # Run the agent
# print(Fore.RED, agent.run_sync("What is the capital of the United States?").data)

llm = AzureChatOpenAI(
   azure_endpoint=os.getenv('AZURE_OPENAI_EMBEDDINGS_ENDPOINT'),    
   api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)