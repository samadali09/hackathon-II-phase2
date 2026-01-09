from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

# Base model with shared properties
class TaskBase(SQLModel):
    title: str = Field(max_length=200, index=True)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)

# Model for the database table
class Task(TaskBase, table=True):
    __tablename__ = "tasks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # FIX: We removed foreign_key="users.id"
    # We just store the user_id as a string so we know who owns the task
    user_id: str = Field(index=True)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# Model for creating a new task (Request Body)
class TaskCreate(TaskBase):
    pass

# Model for updating a task (Request Body)
class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None

# Model for returning task data (Response)
class TaskRead(TaskBase):
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime