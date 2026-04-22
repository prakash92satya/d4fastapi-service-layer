from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskResponse
from app.dependencies.deps import get_db, get_task_service
from app.services.task_service import TaskService

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(db, task)


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    user_role: str,
    db: Session = Depends(get_db),
    service: TaskService = Depends(get_task_service)
):
    try:
        return service.delete_task(db, task_id, user_role)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks(
    db: Session = Depends(get_db),
    service: TaskService = Depends(get_task_service)
):
    return service.get_all_tasks(db)