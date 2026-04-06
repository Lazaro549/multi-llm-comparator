from dataclasses import dataclass


@dataclass
class LLMResponse:
    model: str
    content: str
    latency: float = 0.0
    error: str | None = None
