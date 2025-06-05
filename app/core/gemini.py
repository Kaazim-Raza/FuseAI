import httpx
from typing import Optional

GEMINI_API_KEY = "AIzaSyD5z_a96bkNGNlSnuYD0yC4eZVubJ8XAhw"  # Put in env vars or config in real app

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

async def query_gemini_api(query: str, context: str = "") -> str:
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"{context}\n\n{query}"}
                ]
            }
        ]
    }

    timeout = httpx.Timeout(30.0)  # 30 seconds total timeout

    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(GEMINI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
