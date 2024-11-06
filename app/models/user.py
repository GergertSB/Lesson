from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *

class User(Base): # создаем таблицу БД
    __tablename__ = 'users' # с названием "продукты"
    # __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True) # далее создаём столбцы
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')

    # user_id = Column(Integer, ForeignKey('users.id')) # связь товара по категориям


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))

