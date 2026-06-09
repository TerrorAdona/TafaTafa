from openai import OpenAI
from django.conf import settings
import re
import logging

logger = logging.getLogger(__name__)

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
    try:
        # Using chat.completions for more standard response structure
        # Trying mixtral-8x7b-32768 as Llama models may not be available
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": message}
            ],
            max_tokens=1024,
            temperature=0.7,
            stream=False
        )

        # Extract text from response
        raw_answer = response.choices[0].message.content
        cleaned_answer = _clean_markdown(raw_answer)
        return cleaned_answer
    except Exception as e:
        logger.error(f"Error calling Groq API: {str(e)}")
        # Re-raise to let the view handle the error response
        raise