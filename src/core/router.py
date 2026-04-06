import asyncio
from typing import List, Dict
from src.providers.base import BaseProvider


class MultiLLMRouter:
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
