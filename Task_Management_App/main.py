from fastapi import FastAPI
from src.utils.db import get_db
from src.utils.db import Base, engine
# from src.task.models import TaskModel
from src.task.routers import task_routes
from src.users.routers import user_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="My FastAPI Application")
app.include_router(task_routes)
app.include_router(user_router)