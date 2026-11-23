class PlannerAgent:

    def generate_plan(
        self,
        goal_title: str,
        goal_description: str = ""
    ):

        tasks = [

            {
                "title": "Research",
                "description":
                    f"Research the goal: {goal_title}"
            },

            {
                "title": "Planning",
                "description":
                    f"Create execution strategy for {goal_title}"
            },

            {
                "title": "Execution",
                "description":
                    f"Start implementing {goal_title}"
            },

            {
                "title": "Review",
                "description":
                    f"Evaluate progress of {goal_title}"
            }
        ]

        return tasks
