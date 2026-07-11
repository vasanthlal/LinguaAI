from fastapi import HTTPException
from openai import (
    APIError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)

from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
)


def ask_ai(message: str) -> str:
    """
    Send a message to OpenAI and return the AI response.
    """

    try:
        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )

        return response.choices[0].message.content

    except AuthenticationError:
        raise HTTPException(
            status_code=401,
            detail="Invalid OpenAI API key.",
        )

    except RateLimitError:
        raise HTTPException(
            status_code=429,
            detail="OpenAI API quota exceeded. Please check your billing and usage.",
        )

    except APIError:
        raise HTTPException(
            status_code=500,
            detail="OpenAI service is temporarily unavailable.",
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
