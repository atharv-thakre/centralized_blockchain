# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from sqlalchemy.orm import Session
from app import models, schemas, blockchain
from app.database import SessionLocal, engine, Base
from fastapi.staticfiles import StaticFiles
from typing import List

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Blockchain Demo")

# serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ensure genesis block exists on startup
@app.on_event("startup")
def startup():
    db = SessionLocal()
    blockchain.create_genesis_block(db)
    db.close()

@app.get("/", response_class=HTMLResponse)
def index():
    return FileResponse("static/index.html")

@app.post("/students", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # check unique roll_no
    existing = db.query(models.Student).filter(models.Student.roll_no == student.roll_no).first()
    if existing:
        raise HTTPException(status_code=400, detail="Roll number already exists")
    stu = models.Student(roll_no=student.roll_no, name=student.name, marks=student.marks)
    db.add(stu)
    db.commit()
    db.refresh(stu)

    # add block to blockchain recording this creation
    data_obj = {
        "action": "create_student",
        "student": {
            "id": stu.id,
            "roll_no": stu.roll_no,
            "name": stu.name,
            "marks": stu.marks
        }
    }
    blockchain.add_block(db, data_obj)
    return stu

@app.get("/students", response_model=List[schemas.StudentOut])
def list_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

@app.get("/blockchain", response_model=List[schemas.BlockOut])
def view_blockchain(db: Session = Depends(get_db)):
    blocks = db.query(models.Block).order_by(models.Block.index.asc()).all()
    return blocks

@app.get("/validate")
def validate_chain(db: Session = Depends(get_db)):
    valid = blockchain.is_chain_valid(db)
    return {"valid": valid}
