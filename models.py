import os
from dotenv import load_dotenv
import openai
import requests
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from pydantic_ai import Agent
from openai import AsyncAzureOpenAI
from pydantic_ai.models.openai import OpenAIModel
# from azure.ai.openai import OpenAIClient
# from azure.identity import DefaultAzureCredential

# Load environment variables from .env file
load_dotenv()

class Models:
    def __init__(self):

        # self.api_key = os.environ.get("AZURE_OPENAI_API_KEY")
        # self.endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
        # self.deployment_name = os.environ.get("AZURE_OPENAI_API_DEPLOYMENT_NAME")
        # self.api_version = os.environ.get("AZURE_OPENAI_API_VERSION")

        # # Initialize the OpenAI client
        # self.client = OpenAIClient(
        #     endpoint=self.endpoint,
        #     credential=DefaultAzureCredential()
        # )

    #     self.api_key = os.environ.get("TOGETHER_API_KEY")
    #     self.base_url = "https://api.together.xyz/v1"  # Replace with the actual base URL
    #    # Together AI embeddings configuration
    #     self.embeddings_together = {
    #         "api_key": self.api_key,
    #         "base_url": self.base_url,
    #         "model": "together-embed-text"  # Use the appropriate model name
    #     }

        

        # # Together AI chat model
        # self.model_together = TogetherChat(
        #     model="together-chat",  # Use the appropriate model name
        #     api_key=os.environ.get("TOGETHER_API_KEY"),
        #     temperature=0,
        #     max_tokens=None,
        #     timeout=None,
        #     max_retries=2,
        # )

    # Azure OpenAI embeddings
        self.embeddings_openai = AzureOpenAIEmbeddings(
            model="text-embedding-3-small",
            dimensions=1536,  # Can specify dimensions with new text-embedding-3 models
            azure_endpoint=os.environ.get("AZURE_OPENAI_EMBEDDINGS_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
            api_version=os.environ.get("AZURE_OPENAI_EMBEDDINGS_API_VERSION"),
        )

        self.model_openai = AzureChatOpenAI(
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


                
    #     client = AsyncAzureOpenAI(
    #     azure_endpoint=os.getenv('AZURE_OPENAI_EMBEDDINGS_ENDPOINT'),
    #     api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
    #     api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    #     )


    #     # Create the Model
    #     model = OpenAIModel('gpt-4o-mini', openai_client=client)

    #     # Create the Agent
    #     agent = Agent(model=model)

    #     self.model_openai =  AzureChatOpenAI(
    #        azure_endpoint=os.getenv('AZURE_OPENAI_EMBEDDINGS_ENDPOINT'),
    #     api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
    #     api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    #      model = model
    #     )

    # async def generate_chat_response(self, prompt):
    #     response = await self.client.chat_completions(
    #         deployment_name=self.model_openai.azure_deployment,
    #         messages=[{"role": "user", "content": prompt}],
    #         api_version=self.model_openai.api_version
    #     )
    #     return response.choices[0].message["content"]


    #    # Azure OpenAI chat model
    #     self.model_openai = AzureChatOpenAI(
    #         azure_deployment="gpt-35-turbo",
    #         azure_endpoint=os.environ.get("AZURE_OPENAI_EMBEDDINGS_ENDPOINT"),
    #         api_version="2023-06-01-preview",
    #         model="gpt-3.5-turbo",
    #         temperature=0,
    #         max_tokens=None,
    #         timeout=None,
    #         max_retries=2,
    #     )




# def generate_chat_response(self, prompt):
#         response = self.client.chat_completions(
#             deployment_name=self.model_openai.azure_deployment,
#             messages=[{"role": "user", "content": prompt}],
#             api_version=self.model_openai.api_version
#         )
#         return response.choices[0].message["content"]


# # Example usage
# if __name__ == "__main__":
#     models = Models()

#     prompt = "Hello, how are you?"
#     response = models.generate_chat_response(prompt)
#     print("Chat Response:", response)

# def get_embeddings(self, text):
#         url = f"{self.embeddings_together['base_url']}/embeddings"
#         headers = {
#             "Authorization": f"Bearer {self.embeddings_together['api_key']}",
#             "Content-Type": "application/json"
#         }
#         data = {
#             "model": self.embeddings_together['model'],
#             "text": text
#         }
#         response = requests.post(url, headers=headers, json=data)
#         return response.json()


