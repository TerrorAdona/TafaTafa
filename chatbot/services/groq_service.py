from openai import OpenAI
from django.conf import settings
import re

client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

def _clean_markdown(text: str) -> str:
    """Remove common markdown formatting characters for plain text display."""
    if not isinstance(text, str):
        return text
    # Remove asterisks and underscores used for italic/bold
    text = re.sub(r'[\*_]+', '', text)
    # Remove backticks used for code
    text = text.replace('`', '')
    # Remove tilde used for strikethrough
    text = text.replace('~', '')
    # Remove markdown headings markers (optional)
    text = re.sub(r'^\s*#+\s*', '', text, flags=re.MULTILINE)
    # Remove horizontal rules (---, ***, ___)
    text = re.sub(r'^\s*[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)
    # Collapse multiple newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()


def ask_groq(message):

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=message,
    )

    raw_answer = response.output_text
    cleaned_answer = _clean_markdown(raw_answer)
    return cleaned_answer