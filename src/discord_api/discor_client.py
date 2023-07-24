import os
from dotenv import load_dotenv
from discord.client import Client
from discord.flags import Intents
from discord.message import Message
from openai_api.openapi_conector import get_chat_gpt_response

load_dotenv()

bot_caller: str  = "/manu"

discord_token = os.environ.get("DISCORD_TOKEN")

class CustomDiscordClient(Client):
    async def on_ready(self):
        print(f"{self.user} Esta conectado")

    async def on_menssage(self, message: Message):
        message_content: str = message.content
        if bot_caller in message_content:
            prompt: str = message_content.split(bot_caller)[1]
            print(f"****** Prompt message: {prompt} ******")
            chat_gpt_response: str = get_chat_gpt_response(question = prompt)
            if chat_gpt_response:
                await message.channel.send(content = chat_gpt_response)

intents = Intents.default()
intents.message_content = True
custom_discord_client: CustomDiscordClient = CustomDiscordClient(intents=intents)
