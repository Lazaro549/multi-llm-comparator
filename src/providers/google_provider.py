from src.providers.base import BaseProvider


class GoogleProvider(BaseProvider):

    def __init__(self):
        super().__init__("Gemini")

    async def generate(self, prompt: str) -> str:
        return f"[Gemini mock] {prompt}"
