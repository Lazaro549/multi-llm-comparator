import os
from src.providers.base import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self):
        super().__init__("OpenAI")

    async def generate(self, prompt: str) -> str:
        # TODO: integrar OpenAI SDK real
        return f"[OpenAI mock] {prompt}"
