from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.learning_profile import router as learning_profile_router

app = FastAPI(
    title="LinguaAI API",
)

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(learning_profile_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to LinguaAI API"
    }