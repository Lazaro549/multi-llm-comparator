import os
from src.providers.base import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self):
        super().__init__("OpenAI")

    async def generate(self, prompt: str) -> str:
        # TODO: integrar OpenAI SDK real
        import html
        return f"[OpenAI mock] {html.escape(prompt)}"
