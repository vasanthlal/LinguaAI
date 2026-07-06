from fastapi import FastAPI

app = FastAPI(
    title="LinguaAI API",
    description="Backend API for LinguaAI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to LinguaAI API"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }