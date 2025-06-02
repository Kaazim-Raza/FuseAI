from fastapi import FastAPI
from app.api import files, query

app = FastAPI(title="ChatGPT-like Document Q&A with Gemini API")

app.include_router(files.router)
app.include_router(query.router)
