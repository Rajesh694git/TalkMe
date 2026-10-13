from fastapi import FastAPI

from sqlalchemy import text

from app.database import engine

app = FastAPI(
    title="TalkMe",
    description="Voice-first feedback intelligence platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/health/db")
def database_health_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "ok", "result": result.scalar()}