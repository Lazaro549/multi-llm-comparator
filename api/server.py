from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

from src.core.router import MultiLLMRouter

from src.providers.openai_provider import OpenAIProvider
from src.providers.anthropic_provider import AnthropicProvider
from src.providers.google_provider import GoogleProvider


app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {"message": "Multi LLM Comparator API running 🚀"}


@app.post("/compare")
async def compare(request: PromptRequest):
    prompt = request.prompt

    providers = [
        OpenAIProvider(),
        AnthropicProvider(),
        GoogleProvider(),
    ]

    router = MultiLLMRouter(providers)

    results = await router.run(prompt)

    return results
