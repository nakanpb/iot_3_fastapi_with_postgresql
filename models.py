from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database import Base

class Student(Base):
    __tablename__ = 'students'
    
    student_id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    birth_day = Column(String, index=True)
    age = Column(Integer, index=True)
    sex = Column(String, index=True)
    
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)
    tailde = Column(String, index=True)
    shortstory = Column(String, index=True)
    group = Column(String, index=True)

class Coffee(Base):
    __tablename__ = 'coffee'
    
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    type = Column(String, index=True)
    price = Column(Integer, index=True)
    
class Order(Base):
    __tablename__ = 'order'
    
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    user = Column(String, index=True) 
    count = Column(Integer, index=True)
    other = Column(String, index=True) 
    
    
