import pytest
from src.providers.openai_provider import OpenAIProvider
from src.providers.anthropic_provider import AnthropicProvider
from src.providers.google_provider import GoogleProvider


@pytest.mark.asyncio
async def test_openai_provider_mock():
    provider = OpenAIProvider()
    result = await provider.generate("hello")

    assert "OpenAI" in result


@pytest.mark.asyncio
async def test_anthropic_provider_mock():
    provider = AnthropicProvider()
    result = await provider.generate("hello")

    assert "Claude" in result


@pytest.mark.asyncio
async def test_google_provider_mock():
    provider = GoogleProvider()
    result = await provider.generate("hello")

    assert "Gemini" in result
