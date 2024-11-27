from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
# from typing import List
from llm_logic import open_ai_call

app = FastAPI()

class Prompt(BaseModel):
    user_prompt: str
    system_prompt: str = "You are a helpful assistant."

@app.post("/chat")
async def chat(prompt: Prompt):
    completions = open_ai_call(user_prompt=prompt.user_prompt, system_prompt=prompt.system_prompt)
    return JSONResponse(content={"response": completions.choices[0].message.content, "token_usage": completions.usage.total_tokens if completions.usage else 0})

