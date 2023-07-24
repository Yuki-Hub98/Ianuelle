import openai
import os
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

openai.api_key = os.environ.get("CHAT_GPT_KEY")

def get_chat_gpt_response(question: str) -> str:
    response_from_chat_gpt = openai.Completion.create(
        model = "text-davinci-003",
        prompt = question,
        max_token = 100
    )
    if response_from_chat_gpt:
        choices: List(Dict(str, Any)) = response_from_chat_gpt.get("choices")
        if choices and len(choices) > 0:
            text: str = choices[0].get("text")
            return text
    return None