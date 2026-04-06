import asyncio

from src.core.router import MultiLLMRouter
from src.core.comparator import ResponseComparator

from src.providers.openai_provider import OpenAIProvider
from src.providers.anthropic_provider import AnthropicProvider
from src.providers.google_provider import GoogleProvider


async def main():
    print("🚀 Multi LLM Comparator\n")

    prompt = input("Enter your prompt: ").strip()

    if not prompt:
        print("❌ Prompt cannot be empty.")
        return

    providers = [
        OpenAIProvider(),
        AnthropicProvider(),
        GoogleProvider(),
    ]

    router = MultiLLMRouter(providers)
    comparator = ResponseComparator()

    print("\n⏳ Generating responses...\n")

    results = await router.run(prompt)

    comparator.display(results)


if __name__ == "__main__":
    asyncio.run(main())
