from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import asyncio

from src.core.router import MultiLLMRouter

from src.providers.openai_provider import OpenAIProvider
from src.providers.anthropic_provider import AnthropicProvider
from src.providers.google_provider import GoogleProvider


app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("El prompt no puede estar vacío")
        if len(v) > 10000:
            raise ValueError("El prompt excede el límite de caracteres")
        return v.strip()


@app.get("/")
def root():
    return {"message": "Multi LLM Comparator API running 🚀"}


@app.post("/compare")
async def compare(request: PromptRequest):
    import html
    prompt = html.escape(request.prompt)

    providers = [
        OpenAIProvider(),
        AnthropicProvider(),
        GoogleProvider(),
    ]

    router = MultiLLMRouter(providers)

    results = await router.run(prompt)

    return results
