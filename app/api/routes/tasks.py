from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.repositories.task_repository import (
    TaskRepository
)

from app.services.task_service import (
    TaskService
)


router = APIRouter()

service = TaskService()
repo = TaskRepository()


@router.patch(
    "/tasks/{task_id}/complete"
)
def complete_task(
    task_id: str,
    db: Session = Depends(get_db)
):

    task = repo.get_by_id(
        db,
        task_id
    )
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return service.complete_task(
        db,
        task
    )
