import json
from app.services.gemini_service import ask_gemini


class ExecutionEngine:

    async def build_plan(self, goal: str):
        prompt = f"""
أنت مخطط ذكي. بناءً على الهدف التالي، أنشئ خطة عمل.
الهدف: {goal}

أعد الرد بصيغة JSON فقط بدون أي نص إضافي، بهذا الشكل بالضبط:
{{
  "goal": "{goal}",
  "estimated_days": رقم,
  "tasks": [
    {{"title": "...", "description": "...", "priority": "high|medium|low"}}
  ]
}}
"""
        try:
            raw_text = await ask_gemini(prompt)
            cleaned = raw_text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
            plan = json.loads(cleaned)
            return plan
        except (json.JSONDecodeError, ValueError) as e:
            return {
                "goal": goal,
                "error": f"تعذر إنشاء الخطة: {str(e)}",
                "estimated_days": 0,
                "tasks": []
            }
