import httpx
from typing import Optional

GEMINI_API_URL = "https://api.gemini.example.com/v1/query"  # replace with actual URL
GEMINI_API_KEY = "your_gemini_api_key_here"  # Put in env vars or config in real app

async def query_gemini_api(query: str, context: str) -> str:
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "query": query,
        "context": context
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(GEMINI_API_URL, json=json_data, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from Gemini API")
