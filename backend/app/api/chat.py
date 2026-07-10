from fastapi import APIRouter

from app.ai.chat_service import get_ai_response
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"],
)


@router.post(
    "/",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    response = get_ai_response(
        request.message,
    )

    return ChatResponse(
        response=response,
    )