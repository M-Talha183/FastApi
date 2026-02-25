from fastapi import FastAPI
from src.utils.db import get_db
from src.utils.db import Base, engine
# from src.task.models import TaskModel
from src.task.routers import task_routes

Base.metadata.create_all(bind=engine)
app = FastAPI(title="My FastAPI Application")
app.include_router(task_routes)