```python
import os
import asyncio
from typing import List, Dict

# Import providers (ajustar según tu estructura real)
# from src.providers.openai.openaiProvider import OpenAIProvider
# from src.providers.anthropic.anthropicProvider import AnthropicProvider
# from src.providers.google.googleProvider import GoogleProvider
# from src.providers.local.localProvider import LocalProvider


class BaseProvider:
    """Clase base para providers (mock/simple fallback)"""
    name: str = "base"

    async def generate(self, prompt: str) -> str:
        raise NotImplementedError


class MockProvider(BaseProvider):
    """Provider de prueba si no tenés APIs configuradas"""
    def __init__(self, name: str):
        self.name = name

    async def generate(self, prompt: str) -> str:
        await asyncio.sleep(0.5)
        return f"[{self.name}] Response to: {prompt}"


class MultiLLMRouter:
    """Envía el prompt a múltiples modelos en paralelo"""

    def __init__(self, providers: List[BaseProvider]):
        self.providers = providers

    async def run(self, prompt: str) -> Dict[str, str]:
        tasks = {
            provider.name: asyncio.create_task(provider.generate(prompt))
            for provider in self.providers
        }

        results = {}
        for name, task in tasks.items():
            try:
                results[name] = await task
            except Exception as e:
                results[name] = f"Error: {str(e)}"

        return results


class ResponseComparator:
    """Formatea la salida para comparación"""

    @staticmethod
    def display(results: Dict[str, str]):
        print("\n" + "=" * 60)
        print("🧠 Multi-LLM Comparison Results")
        print("=" * 60)

        for model, response in results.items():
            print(f"\n🔹 {model}")
            print("-" * 60)
            print(response)

        print("\n" + "=" * 60 + "\n")


async def main():
    print("🚀 Multi LLM Comparator\n")

    prompt = input("Enter your prompt: ").strip()

    if not prompt:
        print("❌ Prompt cannot be empty.")
        return

    # ⚡ Acá agregás tus providers reales
    providers: List[BaseProvider] = [
        MockProvider("GPT"),
        MockProvider("Claude"),
        MockProvider("Gemini"),
    ]

    router = MultiLLMRouter(providers)
    comparator = ResponseComparator()

    print("\n⏳ Generating responses...\n")

    results = await router.run(prompt)

    comparator.display(results)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
```
