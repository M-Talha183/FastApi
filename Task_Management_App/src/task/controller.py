from src.task.dtos import TaskSchema
from src.task.models import TaskModel
from sqlalchemy.orm import Session


#  *********** create task ***********
def create_task(body:TaskSchema , db:Session):
    data = body.model_dump()
    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Task created successfully!", "task": new_task}

# *********** get all tasks ***********
def get_all_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return {"tasks": tasks}
