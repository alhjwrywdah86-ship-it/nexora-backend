from app.models.goal import Goal
class GoalRepository:

    def create(
        self,
        db,
        goal
    ):
        db.add(goal)
        db.commit()
        db.refresh(goal)

        return goal

    def get_by_user(
        self,
        db,
        user_id
    ):
        return (
            db.query(Goal)
            .filter(
                Goal.user_id == user_id
            )
            .all()
        )
