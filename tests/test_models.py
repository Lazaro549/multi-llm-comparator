from src.core.models import LLMResponse


def test_llm_response_dataclass():
    response = LLMResponse(
        model="GPT",
        content="Hello world",
        latency=1.23
    )

    assert response.model == "GPT"
    assert response.content == "Hello world"
    assert response.latency == 1.23
    assert response.error is None
