from openai import OpenAI
from django.conf import settings

client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)


def ask_groq(message):

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=message,
    )

    return response.output_text