import pytest
import asyncio
from src.core.router import MultiLLMRouter
from src.providers.base import BaseProvider


class MockProvider(BaseProvider):
    def __init__(self, name: str, response: str):
        super().__init__(name)
        self._response = response

    async def generate(self, prompt: str) -> str:
        await asyncio.sleep(0.1)
        return f"{self._response}: {prompt}"


@pytest.mark.asyncio
async def test_router_returns_all_provider_results():
    providers = [
        MockProvider("A", "Response A"),
        MockProvider("B", "Response B"),
    ]

    router = MultiLLMRouter(providers)
    result = await router.run("test prompt")

    assert "A" in result
    assert "B" in result
    assert result["A"].startswith("Response A")
    assert result["B"].startswith("Response B")
