from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.contents import ChatHistory, ChatMessageContent, AuthorRole
import os
from dotenv import load_dotenv

class HomeAssistant:
    def __init__(self):
        load_dotenv(r'C:\Users\knguyen2\azure.env')

        base_url = os.getenv("AZURE_OPENAI_ENDPOINT")
        api_key = os.getenv("AZURE_OPENAI_KEY")
        deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        self.kernel = Kernel()
        self.kernel.add_service(
            AzureChatCompletion(
                base_url=base_url,
                api_key=api_key,
                deployment_name=deployment_name
            )
        )

        self.agent = ChatCompletionAgent(
            name="HomeAssistant",
            kernel=self.kernel
        )

        self.history = ChatHistory()  # Maintain your own chat history

    async def call(self, user_message: str) -> str:
        self.history.add_message(ChatMessageContent(role=AuthorRole.USER, content=user_message))

        async for response in self.agent.invoke(self.history):  # ✅ pass history here
            self.history.add_message(response)
            return str(response)
