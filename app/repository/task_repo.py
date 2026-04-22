from sqlalchemy.orm import Session
from app.models.task import Task

class TaskRepository:

    def create(self, db: Session, task):
        db_task = Task(**task.dict())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    def get(self, db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    def delete(self, db: Session, task):
        db.delete(task)
        db.commit()

    def get_all(self, db):
       return db.query(Task).all()