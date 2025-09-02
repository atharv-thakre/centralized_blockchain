# app/models.py
from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    roll_no = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    marks = Column(Integer, nullable=False)

class Block(Base):
    __tablename__ = "blocks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    index = Column(Integer, nullable=False, unique=True)
    timestamp = Column(String, nullable=False)  # ISO string
    data = Column(Text, nullable=False)         # JSON string of action/data
    previous_hash = Column(String, nullable=False)
    hash = Column(String, nullable=False)
