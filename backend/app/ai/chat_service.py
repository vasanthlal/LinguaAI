from app.ai.client import ask_ai


def get_ai_response(message: str) -> str:
    """
    Get a response from the AI model.
    """

    response = ask_ai(message)

    return response