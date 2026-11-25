import os

import httpx

BASE_URL = (
    "https://generativelanguage.googleapis.com"
    "/v1beta/models/gemini-2.5-flash:generateContent"
)


class GeminiError(Exception):
    pass


async def ask_gemini(prompt: str) -> str:

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise GeminiError(
            "GEMINI_API_KEY غير مضبوط في البيئة"
        )

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    headers = {"x-goog-api-key": api_key}

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                BASE_URL,
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            data = response.json()

    except httpx.HTTPError:
        raise GeminiError("تعذر الاتصال بخدمة Gemini")

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]

    except (KeyError, IndexError, TypeError):
        raise GeminiError("رد غير متوقع من Gemini")
