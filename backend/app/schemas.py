# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    notes: str | None = None
    due_date: datetime | None = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = None
    notes: str | None = None
    due_date: datetime | None = None
    completed: bool | None = None

class TodoRead(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True
