class CoachAgent:

    def get_message(
        self,
        progress: int,
        streak: int
    ):

        if streak >= 7:
            return (
                "🔥 لديك سلسلة إنجاز قوية، استمر."
            )

        if progress >= 80:
            return (
                "🚀 أنت قريب جداً من تحقيق هدفك."
            )

        if progress >= 50:
            return (
                "💪 تقدم رائع، واصل التنفيذ."
            )

        if progress >= 20:
            return (
                "📈 بداية جيدة، استمر بخطوات ثابتة."
            )

        return (
            "⚡ ابدأ اليوم بأصغر مهمة ممكنة."
        )
