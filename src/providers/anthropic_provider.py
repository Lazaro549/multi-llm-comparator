from src.providers.base import BaseProvider


class AnthropicProvider(BaseProvider):

    def __init__(self):
        super().__init__("Claude")

    async def generate(self, prompt: str) -> str:
        import html
        return f"[Claude mock] {html.escape(prompt)}"
