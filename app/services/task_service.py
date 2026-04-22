from app.repository.task_repo import TaskRepository

class TaskService:

    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, db, task):
        return self.repo.create(db, task)

    def delete_task(self, db, task_id: int, user_role: str):
        task = self.repo.get(db, task_id)

        if not task:
            raise Exception("Task not found")

        # 🔥 Business Rule
        if task.priority == "high" and user_role != "manager":
            raise Exception("Only managers can delete high-priority tasks")

        self.repo.delete(db, task)
        return {"message": "Task deleted"}
    
    def get_all_tasks(self, db):
       return self.repo.get_all(db)