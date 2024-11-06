from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///taskmanager.db', echo=True) # движок для работы с БД (с сылкой на неё)

SessionLocal = sessionmaker(bind=engine) # создание сессии (связи) с БД (через наш движок)

class Base(DeclarativeBase): # класс нашей Базы Данных (БД)
    pass

class User(Base): # создаём таблицу
    __tablename__ = 'user' # с названием Юзер

    id = Column(Integer, primary_key=True) # далее название столбцов с указанием типа данных
    username = Column(String)
    password = Column(String)
