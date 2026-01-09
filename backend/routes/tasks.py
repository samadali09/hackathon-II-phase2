from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

# Import from database.py (we deleted db.py, remember?)
from database import get_session
from models import Task, TaskCreate, TaskUpdate, TaskRead
from auth import get_current_user

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

# GET: List all tasks for the logged-in user
@router.get("/", response_model=List[TaskRead])
async def read_tasks(
    session: AsyncSession = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    statement = select(Task).where(Task.user_id == user_id)
    result = await session.execute(statement)
    return result.scalars().all()

# POST: Create a new task
@router.post("/", response_model=TaskRead)
async def create_task(
    task: TaskCreate,
    session: AsyncSession = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    db_task = Task.model_validate(task)
    db_task.user_id = user_id
    
    session.add(db_task)
    await session.commit()
    await session.refresh(db_task)
    return db_task

# PATCH: Update a task
@router.patch("/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    session: AsyncSession = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    result = await session.execute(statement)
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = task_update.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)

    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

# DELETE: Remove a task
@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    session: AsyncSession = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    result = await session.execute(statement)
    task = result.scalar_one_or_none()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
        
    await session.delete(task)
    await session.commit()
    return {"ok": True}