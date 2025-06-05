from fastapi import FastAPI
from app.api import files, query
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title="ChatGPT-like Document Q&A with Gemini API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(files.router)
app.include_router(query.router)
