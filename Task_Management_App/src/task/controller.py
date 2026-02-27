from fastapi import HTTPException

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
# *********** get task by id ***********
def get_task_by_id(task_id:int, db:Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task retrieved successfully!", "task": task}


def update_task(task_id:int, body:TaskSchema, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
 
    body_update = body.model_dump()
    for field,value in body_update.items():
        setattr(one_task, field, value)
    
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    
    return {"Status":"task update Succesfully ","data":one_task}
    
    
    
def delet_task(task_id:int, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(one_task)
    db.commit()
    
    return {"Status":"task delete Succesfully "}