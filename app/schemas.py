# app/schemas.py
from pydantic import BaseModel

class StudentCreate(BaseModel):
    roll_no: str
    name: str
    marks: int

class StudentOut(BaseModel):
    id: int
    roll_no: str
    name: str
    marks: int

    class Config:
        orm_mode = True

class BlockOut(BaseModel):
    index: int
    timestamp: str
    data: str
    previous_hash: str
    hash: str

    class Config:
        orm_mode = True
