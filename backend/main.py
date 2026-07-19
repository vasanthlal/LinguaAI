from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.learning_profile import router as learning_profile_router
from app.api.language import router as language_router
from app.api.course import router as course_router
from app.api.lesson import router as lesson_router
from app.api.quiz import router as quiz_router
from app.api.question import router as question_router
from app.api.answer_option import router as answer_option_router
from app.api.quiz_attempt import router as quiz_attempt_router

from app.core.error_handlers import register_exception_handlers

app = FastAPI(
    title="LinguaAI API",
    description="""
## LinguaAI Backend API

LinguaAI is an AI-powered language learning platform.

### Features

- User Authentication
- AI Chat Assistant
- Language Management
- Course Management
- Lesson Management
- Quiz Management
- Question Management
- Answer Option Management

### Version

v1.1.0
""",
    version="1.1.0",
    contact={
        "name": "Vasanthlal",
        "email": "your-email@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

# Register global exception handlers
register_exception_handlers(app)

# Register API routers
app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(learning_profile_router)
app.include_router(language_router)
app.include_router(course_router)
app.include_router(lesson_router)
app.include_router(quiz_router)
app.include_router(question_router)
app.include_router(answer_option_router)
app.include_router(quiz_attempt_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to LinguaAI API",
        "version": "1.1.0",
        "status": "Running",
    }