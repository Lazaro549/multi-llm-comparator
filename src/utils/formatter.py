import html

def format_response(model: str, text: str) -> str:
    return f"[{html.escape(model)}] {html.escape(text)}"
