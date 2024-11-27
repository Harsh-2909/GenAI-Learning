from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from secret import OPENAI_API_KEY
import os
# Setting the API key as an environment variable from env.py file instead of .env as we already have a .env folder here and i am too lazy to create another .env file
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI()


def open_ai_call(user_prompt: str, system_prompt: str = "You are a helpful assistant.") -> ChatCompletion:
    completions = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )
    return completions


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    completions = open_ai_call(prompt)
    print("Response:", completions.choices[0].message.content)
    print("Token Usage:", completions.usage.total_tokens if completions.usage else 0)
