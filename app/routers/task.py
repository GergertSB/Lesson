from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from typing import Annotated
from app.backend.db_depends import get_db
from app.models.task import Task
from app.models.user import User
from app.schemas import CreateTask, UpdateTask

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(get_db: Annotated[Session, Depends(get_db)]):
    tasks = get_db.scalars(select(Task).where(Task.is_active == True)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(get_db: Annotated[Session, Depends(get_db)], user_id: int):
    task = get_db.scalars(select(Task).where(Task.id == user_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не был найден'
        )
    return task

@router.post('/create')
async def create_task(get_db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = get_db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Такого пользователя не существует'
        )
    get_db.execute(insert(Task).values(title=create_task.title,
                                       content=create_task.content,
                                       priority=create_task.priority,
                                       user_id=create_task.user_id))
    get_db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }
@router.put('/update')
async def update_task(get_db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = get_db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не был найден'
        )
    get_db.execute(update(Task).where(Task.id == task_id).values(
        title=create_task.title,
        content=create_task.content,
        priority=create_task.priority,
        user_id=create_task.user_id))
    get_db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Пользователь не был найден!'}

@router.delete('/delete')
async def delete_task(get_db: Annotated[Session, Depends(get_db)], task_id: int):
    task = get_db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Такой записи не существует'
        )
    get_db.execute(update(Task).where(Task.id == task_id).values(is_active=False))
    get_db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Такой записи не существует'}