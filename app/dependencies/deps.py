from app.core.db import SessionLocal
from app.repository.task_repo import TaskRepository
from app.services.task_service import TaskService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_service():
    repo = TaskRepository()
    return TaskService(repo)