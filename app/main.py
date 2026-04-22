from fastapi import FastAPI
from app.api.task_routes import router
from app.core.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


   