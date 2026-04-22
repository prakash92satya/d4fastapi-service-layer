from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    priority = Column(String)  # low, medium, high