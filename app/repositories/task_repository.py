class TaskRepository:

    def create(
        self,
        db,
        task
    ):
        db.add(task)
        db.commit()
        db.refresh(task)

        return task

    def get_by_goal(
        self,
        db,
        goal_id
    ):
        return (
            db.query(Task)
            .filter(
                Task.goal_id == goal_id
            )
            .all()
        )
def get_by_id(
    self,
    db,
    task_id
):

    return (
        db.query(Task)
        .filter(
            Task.id == task_id
        )
        .first()
    )
