from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import models, schemas
from ..users.models import User
from ..devices.models import Dog
from ..dependencies import get_current_user
from ..logging_config import app_logger

router = APIRouter()

@router.post("/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    dog = db.query(Dog).filter(Dog.id == task.dog_id).first()
    if not dog:
        app_logger.warning(f"Task creation failed: Dog not found for dog_id {task.dog_id}")
        raise HTTPException(status_code=404, detail="Dog not found")
    
    new_task = models.Task(description=task.description, status="pending", dog_id=task.dog_id, user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    app_logger.info(f"Task created successfully: {new_task.description} by user {user.id}")
    return new_task

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user.id).first()
    if not db_task:
        app_logger.warning(f"Task update failed: Task not found or not authorized for task_id {task_id}")
        raise HTTPException(status_code=404, detail="Task not found or not authorized")
    
    db_task.status = task.status
    db.commit()
    db.refresh(db_task)
    app_logger.info(f"Task updated successfully: {db_task.description} by user {user.id}")
    return db_task

@router.get("/", response_model=list[schemas.TaskResponse])
def list_tasks(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(models.Task.user_id == user.id).all()
    app_logger.info(f"Tasks listed for user {user.id}")
    return tasks
