# app/routers/todos.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db import get_db
from .. import schemas, crud

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=list[schemas.TodoRead])
def list_all(db: Session = Depends(get_db)):
    return crud.list_todos(db)

@router.post("/", response_model=schemas.TodoRead, status_code=status.HTTP_201_CREATED)
def create(data: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, data)

@router.get("/{todo_id}", response_model=schemas.TodoRead)
def get_one(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(404, "Todo not found")
    return todo

@router.patch("/{todo_id}", response_model=schemas.TodoRead)
def patch(todo_id: int, data: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(404, "Todo not found")
    return crud.update_todo(db, todo, data)

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(404, "Todo not found")
    crud.delete_todo(db, todo)