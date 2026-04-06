from src.providers.base import BaseProvider


class GoogleProvider(BaseProvider):

    def __init__(self):
        super().__init__("Gemini")

    async def generate(self, prompt: str) -> str:
        import html
        return f"[Gemini mock] {html.escape(prompt)}"
